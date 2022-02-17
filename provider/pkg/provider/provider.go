// Copyright 2016-2020, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/url"
	"strings"
	"time"

	jsonpatch "github.com/evanphx/json-patch"
	"github.com/frezbo/pulumi-provider-talos/provider/pkg/constants"
	"github.com/pulumi/pulumi/pkg/v3/resource/provider"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource/plugin"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/retry"
	machineapi "github.com/talos-systems/talos/pkg/machinery/api/machine"
	"github.com/talos-systems/talos/pkg/machinery/client"
	clientconfig "github.com/talos-systems/talos/pkg/machinery/client/config"
	"github.com/talos-systems/talos/pkg/machinery/config"
	"github.com/talos-systems/talos/pkg/machinery/config/configpatcher"
	"github.com/talos-systems/talos/pkg/machinery/config/encoder"
	"github.com/talos-systems/talos/pkg/machinery/config/types/v1alpha1"
	"github.com/talos-systems/talos/pkg/machinery/config/types/v1alpha1/bundle"
	"github.com/talos-systems/talos/pkg/machinery/config/types/v1alpha1/generate"
	"github.com/talos-systems/talos/pkg/machinery/config/types/v1alpha1/machine"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"gopkg.in/yaml.v3"

	pulumirpc "github.com/pulumi/pulumi/sdk/v3/proto/go"
	talosnet "github.com/talos-systems/net"
	talosconstants "github.com/talos-systems/talos/pkg/machinery/constants"

	pbempty "github.com/golang/protobuf/ptypes/empty"
)

type talosProvider struct {
	host    *provider.HostClient
	name    string
	version string
}

func makeProvider(host *provider.HostClient, name, version string) (pulumirpc.ResourceProviderServer, error) {
	// Return the new provider
	return &talosProvider{
		host:    host,
		name:    name,
		version: version,
	}, nil
}

// Call dynamically executes a method in the provider associated with a component resource.
func (k *talosProvider) Call(ctx context.Context, req *pulumirpc.CallRequest) (*pulumirpc.CallResponse, error) {
	return nil, status.Error(codes.Unimplemented, "Call is not yet implemented")
}

// Construct creates a new component resource.
func (k *talosProvider) Construct(ctx context.Context, req *pulumirpc.ConstructRequest) (*pulumirpc.ConstructResponse, error) {
	return nil, status.Error(codes.Unimplemented, "Construct is not yet implemented")
}

// CheckConfig validates the configuration for this provider.
func (k *talosProvider) CheckConfig(ctx context.Context, req *pulumirpc.CheckRequest) (*pulumirpc.CheckResponse, error) {
	return &pulumirpc.CheckResponse{Inputs: req.GetNews()}, nil
}

// DiffConfig diffs the configuration for this provider.
func (k *talosProvider) DiffConfig(ctx context.Context, req *pulumirpc.DiffRequest) (*pulumirpc.DiffResponse, error) {
	return &pulumirpc.DiffResponse{}, nil
}

// Configure configures the resource provider with "globals" that control its behavior.
func (k *talosProvider) Configure(_ context.Context, req *pulumirpc.ConfigureRequest) (*pulumirpc.ConfigureResponse, error) {
	return &pulumirpc.ConfigureResponse{}, nil
}

// Invoke dynamically executes a built-in function in the provider.
func (k *talosProvider) Invoke(ctx context.Context, req *pulumirpc.InvokeRequest) (*pulumirpc.InvokeResponse, error) {
	tok := req.GetTok()
	if tok == "talos:index:getKubeConfig" {
		inputs := req.Args.AsMap()

		endpoints := []string{inputs["endpoint"].(string)}
		nodes := []string{inputs["node"].(string)}
		talosconfig := inputs["talosConfig"].(string)
		timeout := int(inputs["timeout"].(float64))

		delay := constants.TalosGetKubeConfigResourceDelayBetweenRetries
		maxDelay := constants.TalosGetKubeConfigResourceMaxDelayBetweenRetries

		kubeconfigUnTyped, err := talosClusterOperation(ctx, nodes, endpoints, talosconfig, delay, maxDelay, timeout, "kubeconfig")
		if err != nil {
			return nil, err
		}
		kubeconfig := kubeconfigUnTyped.(string)

		outputs := map[string]interface{}{
			"kubeconfig": kubeconfig,
		}

		outputProperties, err := plugin.MarshalProperties(
			resource.NewPropertyMapFromMap(outputs),
			plugin.MarshalOptions{},
		)
		if err != nil {
			return nil, err
		}

		return &pulumirpc.InvokeResponse{
			Return: outputProperties,
		}, nil
	}
	return nil, fmt.Errorf("unknown Invoke token '%s'", tok)
}

// StreamInvoke dynamically executes a built-in function in the provider. The result is streamed
// back as a series of messages.
func (k *talosProvider) StreamInvoke(req *pulumirpc.InvokeRequest, server pulumirpc.ResourceProvider_StreamInvokeServer) error {
	tok := req.GetTok()
	return fmt.Errorf("unknown StreamInvoke token '%s'", tok)
}

// Check validates that the given property bag is valid for a resource of the given type and returns
// the inputs that should be passed to successive calls to Diff, Create, or Update for this
// resource. As a rule, the provider inputs returned by a call to Check should preserve the original
// representation of the properties as present in the program inputs. Though this rule is not
// required for correctness, violations thereof can negatively impact the end-user experience, as
// the provider inputs are using for detecting and rendering diffs.
func (k *talosProvider) Check(ctx context.Context, req *pulumirpc.CheckRequest) (*pulumirpc.CheckResponse, error) {
	urn := resource.URN(req.GetUrn())
	ty := urn.Type()

	// Obtain new resource inputs. This is the new version of the resource(s) supplied by the user as
	// an update.
	newResInputs := req.GetNews()
	news, err := plugin.UnmarshalProperties(newResInputs, plugin.MarshalOptions{
		KeepUnknowns: true,
		SkipNulls:    true,
	})
	if err != nil {
		return nil, errors.Unwrap(fmt.Errorf("%w: %s", err, "check failed because malformed resource inputs"))
	}

	if err != nil {
		return nil, errors.Unwrap(fmt.Errorf("%w: %s", err, "check failed because malformed resource inputs"))
	}

	newInputs := news.Mappable()

	switch ty {
	case "talos:index:clusterSecrets":
		if configVersionUnTyped, ok := newInputs["configVersion"]; ok && !news["configVersion"].IsComputed() {
			configVersion := configVersionUnTyped.(string)

			if configVersion != constants.TalosMachineConfigVersion {
				return nil, fmt.Errorf("configVersion must be %s", constants.TalosMachineConfigVersion)
			}
		}

		if talosVersionUnTyped, ok := newInputs["talosVersion"]; ok && !news["talosVersion"].IsComputed() {
			talosVersion := talosVersionUnTyped.(string)

			_, err = config.ParseContractFromVersion(talosVersion)
			if err != nil {
				return nil, fmt.Errorf("invalid talos-version: %w", err)
			}
		}
	case "talos:index:clusterConfig":
		if clusterEndpointUnTyped, ok := newInputs["clusterEndpoint"]; ok && !news["clusterEndpoint"].IsComputed() {
			clusterEndpoint := clusterEndpointUnTyped.(string)

			u, err := url.Parse(clusterEndpoint)
			if err != nil {
				if !strings.Contains(clusterEndpoint, "/") {
					// not a URL, could be just host:port
					u = &url.URL{
						Host: clusterEndpoint,
					}
				} else {
					return nil, fmt.Errorf("failed to parse the cluster endpoint URL: %w", err)
				}
			}
			if u.Scheme == "" {
				if u.Port() == "" {
					return nil, fmt.Errorf("no scheme and port specified for the cluster endpoint URL\ntry: %q", fixControlPlaneEndpoint(u))
				}

				return nil, fmt.Errorf("no scheme specified for the cluster endpoint URL\ntry: %q", fixControlPlaneEndpoint(u))
			}

			if u.Scheme != "https" {
				return nil, fmt.Errorf("the control plane endpoint URL should have scheme https://\ntry: %q", fixControlPlaneEndpoint(u))
			}

			if err = talosnet.ValidateEndpointURI(clusterEndpoint); err != nil {
				return nil, fmt.Errorf("error validating the cluster endpoint URL: %w", err)
			}
		}
	case "talos:index:nodeBootstrap":
	default:
		return nil, fmt.Errorf("unknown resource type '%s'", ty)
	}

	return &pulumirpc.CheckResponse{Inputs: req.News, Failures: nil}, nil
}

// Diff checks what impacts a hypothetical update will have on the resource's properties.
func (k *talosProvider) Diff(ctx context.Context, req *pulumirpc.DiffRequest) (*pulumirpc.DiffResponse, error) {
	urn := resource.URN(req.GetUrn())
	ty := urn.Type()

	olds, err := plugin.UnmarshalProperties(req.GetOlds(), plugin.MarshalOptions{KeepUnknowns: true, SkipNulls: true})
	if err != nil {
		return nil, err
	}

	news, err := plugin.UnmarshalProperties(req.GetNews(), plugin.MarshalOptions{KeepUnknowns: true, SkipNulls: true})
	if err != nil {
		return nil, err
	}

	d := olds.Diff(news)

	replaces := make([]string, 0)
	changes := pulumirpc.DiffResponse_DIFF_NONE

	switch ty {
	case "talos:index:clusterSecrets":
		changed := false
		if d.Changed("talosVersion") {
			changed = true
			replaces = append(replaces, "talosVersion")
		}

		if d.Changed("configVersion") {
			changed = true
			replaces = append(replaces, "configVersion")
		}

		if changed {
			changes = pulumirpc.DiffResponse_DIFF_SOME
		}
	case "talos:index:clusterConfig":
		changed := false

		for _, k := range d.ChangedKeys() {
			property := string(k)

			switch property {
			case "controlplaneConfig", "workerConfig", "talosConfig":
				continue
			default:
				changed = true
				replaces = append(replaces, property)
			}
		}

		if changed {
			changes = pulumirpc.DiffResponse_DIFF_SOME
		}
	case "talos:index:nodeBootstrap":
		changed := false

		for _, k := range d.ChangedKeys() {
			property := string(k)

			switch property {
			case "timeout":
				continue
			default:
				changed = true
				replaces = append(replaces, property)
			}
		}

		if changed {
			changes = pulumirpc.DiffResponse_DIFF_SOME
		}
	default:
		return nil, fmt.Errorf("unknown resource type '%s'", ty)
	}

	return &pulumirpc.DiffResponse{
		Changes:  changes,
		Replaces: replaces,
	}, nil
}

// Create allocates a new instance of the provided resource and returns its unique ID afterwards.
func (k *talosProvider) Create(ctx context.Context, req *pulumirpc.CreateRequest) (*pulumirpc.CreateResponse, error) {
	urn := resource.URN(req.GetUrn())
	ty := urn.Type()

	inputs, err := plugin.UnmarshalProperties(req.GetProperties(), plugin.MarshalOptions{
		KeepUnknowns: true,
		SkipNulls:    true,
	})
	if err != nil {
		return nil, err
	}

	inputsMap := inputs.Mappable()

	genOptions := make([]generate.GenOption, 0)
	outputs := make(map[string]interface{})
	var id string

	switch ty {
	case "talos:index:clusterSecrets":
		id = "secrets"

		if talosVersionUnTyped, ok := inputsMap["talosVersion"]; ok {
			talosVersion := talosVersionUnTyped.(string)
			var versionContract *config.VersionContract

			versionContract, err = config.ParseContractFromVersion(talosVersion)
			if err != nil {
				return nil, fmt.Errorf("invalid talos-version: %w", err)
			}
			genOptions = append(genOptions, generate.WithVersionContract(versionContract))
			outputs["talosVersion"] = talosVersion
		}

		if configVersionUnTyped, ok := inputsMap["configVersion"]; ok {
			configVersion := configVersionUnTyped.(string)

			outputs["configVersion"] = configVersion
		}

		secretsBundle, err := generate.NewSecretsBundle(generate.NewClock(), genOptions...)
		if err != nil {
			return nil, err
		}

		outputs["secrets"] = secretsBundle

	case "talos:index:clusterConfig":
		id = "config"

		outputs = map[string]interface{}{
			"clusterName":       inputsMap["clusterName"].(string),
			"clusterEndpoint":   inputsMap["clusterEndpoint"].(string),
			"dnsDomain":         inputsMap["dnsDomain"].(string),
			"installDisk":       inputsMap["installDisk"].(string),
			"installImage":      inputsMap["installImage"].(string),
			"kubernetesVersion": inputsMap["kubernetesVersion"].(string),
			"persist":           inputsMap["persist"].(bool),
			"clusterDiscovery":  inputsMap["clusterDiscovery"].(bool),
			"docs":              inputsMap["docs"].(bool),
			"examples":          inputsMap["examples"].(bool),
		}
		if registryMirrorsArrayUnTyped, ok := inputsMap["registryMirrors"]; ok {
			registryMirrorsUnTyped := registryMirrorsArrayUnTyped.([]interface{})

			outputs["registryMirrors"] = make([]string, len(registryMirrorsUnTyped))

			for i, registryMirrorUnTyped := range registryMirrorsUnTyped {
				registryMirror := registryMirrorUnTyped.(string)

				outputs["registryMirrors"].([]string)[i] = registryMirror
				components := strings.SplitN(registryMirror, "=", 2)
				if len(components) != 2 {
					return nil, fmt.Errorf("invalid registry mirror spec: %q", registryMirror)
				}

				genOptions = append(genOptions, generate.WithRegistryMirror(components[0], components[1]))
			}
		}

		if kubespanUnTyped, ok := inputsMap["kubespan"]; ok {
			kubespan := kubespanUnTyped.(bool)

			if kubespan {
				genOptions = append(genOptions, generate.WithNetworkOptions(
					v1alpha1.WithKubeSpan(),
				))
			}
			outputs["kubespan"] = kubespan
		}

		if additionalSANsUnTyped, ok := inputsMap["additionalSans"]; ok {
			additionalSANs := additionalSANsUnTyped.([]string)

			genOptions = append(genOptions, generate.WithAdditionalSubjectAltNames(additionalSANs))
			outputs["additionalSans"] = additionalSANs
		}

		if talosVersionUnTyped, ok := inputsMap["talosVersion"]; ok {
			talosVersion := talosVersionUnTyped.(string)
			outputs["talosVersion"] = talosVersion
		}

		if configVersionUnTyped, ok := inputsMap["configVersion"]; ok {
			configVersion := configVersionUnTyped.(string)
			outputs["configVersion"] = configVersion
		}

		genOptions = append(genOptions,
			generate.WithInstallDisk(inputsMap["installDisk"].(string)),
			generate.WithInstallImage(inputsMap["installImage"].(string)),
			generate.WithDNSDomain(inputsMap["dnsDomain"].(string)),
			generate.WithPersist(inputsMap["persist"].(bool)),
			generate.WithClusterDiscovery(inputsMap["clusterDiscovery"].(bool)),
		)

		commentsFlags := encoder.CommentsDisabled

		if inputsMap["docs"].(bool) {
			commentsFlags |= encoder.CommentsDocs
		}

		if inputsMap["examples"].(bool) {
			commentsFlags |= encoder.CommentsExamples
		}

		configBundleOpts := []bundle.Option{
			bundle.WithInputOptions(
				&bundle.InputOptions{
					ClusterName: inputsMap["clusterName"].(string),
					Endpoint:    inputsMap["clusterEndpoint"].(string),
					KubeVersion: strings.TrimPrefix(inputsMap["kubernetesVersion"].(string), "v"),
					GenOptions:  genOptions,
				},
			),
		}

		addConfigPatch := func(configPatchesUnTyped map[string]interface{}, configOpt func(jsonpatch.Patch) bundle.Option) error {
			var result jsonpatch.Patch

			if patchesUntyped, ok := configPatchesUnTyped["patches"]; ok {
				patchesUntyped := patchesUntyped.([]interface{})
				patches := make([]map[string]interface{}, len(patchesUntyped))

				for i, patchAsMapUntyped := range patchesUntyped {
					patches[i] = patchAsMapUntyped.(map[string]interface{})
				}

				patchBytes, err := json.Marshal(patches)
				if err != nil {
					return fmt.Errorf("error marshalling patch: %w", err)
				}
				p, err := jsonpatch.DecodePatch(patchBytes)
				if err != nil {
					return fmt.Errorf("error parsing patch: %w", err)
				}
				result = append(result, p...)
			}

			if filePatchesUnTyped, ok := configPatchesUnTyped["patchFiles"]; ok {
				patchesUnTyped := filePatchesUnTyped.([]interface{})

				for _, patchUntyped := range patchesUnTyped {
					asset := patchUntyped.(*resource.Asset)

					patchBytes, err := asset.Bytes()
					if err != nil {
						return fmt.Errorf("error reading patch file: %w", err)
					}
					p, err := configpatcher.LoadPatch(patchBytes)
					if err != nil {
						return fmt.Errorf("error parsing patch file: %w", err)
					}
					result = append(result, p...)
				}
			}

			configBundleOpts = append(configBundleOpts, configOpt(result))
			return nil
		}

		if patchesUnTyped, ok := inputsMap["configPatches"]; ok {
			configPatchesUnTyped := patchesUnTyped.(map[string]interface{})

			if err := addConfigPatch(configPatchesUnTyped, bundle.WithJSONPatch); err != nil {
				return nil, err
			}
			outputs["configPatches"] = configPatchesUnTyped
		}

		if patchesControlPlaneUnTyped, ok := inputsMap["configPatchesControlPlane"]; ok {
			configPatchesControlPlaneUnTyped := patchesControlPlaneUnTyped.(map[string]interface{})

			if err := addConfigPatch(configPatchesControlPlaneUnTyped, bundle.WithJSONPatchControlPlane); err != nil {
				return nil, err
			}
			outputs["configPatchesControlPlane"] = configPatchesControlPlaneUnTyped
		}

		if patchesWorkerUnTyped, ok := inputsMap["configPatchesWorker"]; ok {
			configPatchesWorkerUnTyped := patchesWorkerUnTyped.(map[string]interface{})

			if err := addConfigPatch(configPatchesWorkerUnTyped, bundle.WithJSONPatchWorker); err != nil {
				return nil, err
			}
			outputs["configPatchesWorker"] = configPatchesWorkerUnTyped
		}

		options := bundle.Options{}

		for _, opt := range configBundleOpts {
			if err := opt(&options); err != nil {
				return nil, err
			}
		}

		if options.InputOptions == nil {
			return nil, fmt.Errorf("no WithInputOptions is defined")
		}

		var secretsBundle *generate.SecretsBundle

		bytes, err := json.Marshal(inputsMap["secrets"])
		if err != nil {
			return nil, fmt.Errorf("error marshaling secrets: %w", err)
		}

		if err := json.Unmarshal(bytes, &secretsBundle); err != nil {
			return nil, fmt.Errorf("error unmarshaling secrets: %w", err)
		}

		secretsBundle.Clock = generate.NewClock()

		input, err := generate.NewInput(
			options.InputOptions.ClusterName,
			options.InputOptions.Endpoint,
			options.InputOptions.KubeVersion,
			secretsBundle,
			options.InputOptions.GenOptions...,
		)
		if err != nil {
			return nil, err
		}
		outputs["secrets"] = inputsMap["secrets"]

		bundle := &v1alpha1.ConfigBundle{}

		for _, configType := range []machine.Type{machine.TypeInit, machine.TypeControlPlane, machine.TypeWorker} {
			var generatedConfig *v1alpha1.Config

			generatedConfig, err = generate.Config(configType, input)
			if err != nil {
				return nil, err
			}

			switch configType {
			case machine.TypeInit:
				bundle.InitCfg = generatedConfig
			case machine.TypeControlPlane:
				bundle.ControlPlaneCfg = generatedConfig
			case machine.TypeWorker:
				bundle.WorkerCfg = generatedConfig
			case machine.TypeUnknown:
				fallthrough
			default:
				return nil, fmt.Errorf("unreachable code")
			}
		}

		if err := bundle.ApplyJSONPatch(options.JSONPatch, true, true); err != nil {
			return nil, fmt.Errorf("error patching configs: %w", err)
		}

		if err := bundle.ApplyJSONPatch(options.JSONPatchControlPlane, true, false); err != nil {
			return nil, fmt.Errorf("error patching control plane configs: %w", err)
		}

		if err := bundle.ApplyJSONPatch(options.JSONPatchWorker, false, true); err != nil {
			return nil, fmt.Errorf("error patching worker config: %w", err)
		}

		controlPlaneConfig, err := bundle.ControlPlaneCfg.EncodeString(encoder.WithComments(commentsFlags))
		if err != nil {
			return nil, err
		}
		outputs["controlplaneConfig"] = controlPlaneConfig

		workerConfig, err := bundle.WorkerCfg.EncodeString(encoder.WithComments(commentsFlags))
		if err != nil {
			return nil, err
		}
		outputs["workerConfig"] = workerConfig

		talosConfig, err := generate.Talosconfig(input, options.InputOptions.GenOptions...)
		if err != nil {
			return nil, err
		}

		talosConfigYaml, err := yaml.Marshal(talosConfig)
		if err != nil {
			return nil, err
		}
		outputs["talosConfig"] = string(talosConfigYaml)
	case "talos:index:nodeBootstrap":
		id = "nodeBootstrap"

		talosconfig := inputsMap["talosConfig"].(string)
		nodes := []string{inputsMap["node"].(string)}
		endpoints := []string{inputsMap["endpoint"].(string)}
		timeout := int(inputsMap["timeout"].(float64))

		outputs = map[string]interface{}{
			"talosConfig": talosconfig,
			"node":        inputsMap["node"].(string),
			"endpoint":    inputsMap["endpoint"].(string),
			"timeout":     timeout,
		}

		delay := constants.TalosBootstrapResourceDelayBetweenRetries
		maxDelay := constants.TalosBootstrapResourceMaxDelayBetweenRetries

		if _, err := talosClusterOperation(ctx, nodes, endpoints, talosconfig, delay, maxDelay, timeout, "bootstrap"); err != nil {
			return nil, err
		}
	default:
		return nil, fmt.Errorf("unknown resource type '%s'", ty)
	}

	outputProperties, err := plugin.MarshalProperties(
		resource.NewPropertyMapFromMap(outputs),
		plugin.MarshalOptions{KeepUnknowns: true, SkipNulls: true},
	)
	if err != nil {
		return nil, err
	}
	return &pulumirpc.CreateResponse{
		Id:         id,
		Properties: outputProperties,
	}, nil
}

// Read the current live state associated with a resource.
func (k *talosProvider) Read(ctx context.Context, req *pulumirpc.ReadRequest) (*pulumirpc.ReadResponse, error) {
	urn := resource.URN(req.GetUrn())
	ty := urn.Type()

	switch ty {
	case "talos:index:clusterSecrets":
	case "talos:index:clusterConfig":
	case "talos:index:nodeBootstrap":
	default:
		return nil, fmt.Errorf("unknown resource type '%s'", ty)
	}
	return nil, status.Error(codes.Unimplemented, "Read is not yet implemented for talos resources")
}

// Update updates an existing resource with new values.
func (k *talosProvider) Update(ctx context.Context, req *pulumirpc.UpdateRequest) (*pulumirpc.UpdateResponse, error) {
	urn := resource.URN(req.GetUrn())
	ty := urn.Type()

	switch ty {
	case "talos:index:clusterSecrets":
	case "talos:index:clusterConfig":
	case "talos:index:nodeBootstrap":
	default:
		return nil, fmt.Errorf("unknown resource type '%s'", ty)
	}

	// Our Random resource will never be updated - if there is a diff, it will be a replacement.
	return nil, status.Error(codes.Unimplemented, "Update is not yet implemented for talos resources")
}

// Delete tears down an existing resource with the given ID.  If it fails, the resource is assumed
// to still exist.
func (k *talosProvider) Delete(ctx context.Context, req *pulumirpc.DeleteRequest) (*pbempty.Empty, error) {
	urn := resource.URN(req.GetUrn())
	ty := urn.Type()

	switch ty {
	case "talos:index:clusterSecrets":
	case "talos:index:clusterConfig":
	case "talos:index:nodeBootstrap":
	default:
		return nil, fmt.Errorf("unknown resource type '%s'", ty)
	}

	// Note that for Talos resources, we don't have to do anything on Delete.
	return &pbempty.Empty{}, nil
}

// GetPluginInfo returns generic information about this plugin, like its version.
func (k *talosProvider) GetPluginInfo(context.Context, *pbempty.Empty) (*pulumirpc.PluginInfo, error) {
	return &pulumirpc.PluginInfo{
		Version: k.version,
	}, nil
}

// GetSchema returns the JSON-serialized schema for the provider.
func (k *talosProvider) GetSchema(ctx context.Context, req *pulumirpc.GetSchemaRequest) (*pulumirpc.GetSchemaResponse, error) {
	return &pulumirpc.GetSchemaResponse{}, nil
}

// Cancel signals the provider to gracefully shut down and abort any ongoing resource operations.
// Operations aborted in this way will return an error (e.g., `Update` and `Create` will either a
// creation error or an initialization error). Since Cancel is advisory and non-blocking, it is up
// to the host to decide how long to wait after Cancel is called before (e.g.)
// hard-closing any gRPC connection.
func (k *talosProvider) Cancel(context.Context, *pbempty.Empty) (*pbempty.Empty, error) {
	// TODO
	return &pbempty.Empty{}, nil
}

func fixControlPlaneEndpoint(u *url.URL) *url.URL {
	// handle the case when the hostname/IP is given without the port, it parses as URL Path
	if u.Scheme == "" && u.Host == "" && u.Path != "" {
		u.Host = u.Path
		u.Path = ""
	}

	u.Scheme = "https"

	if u.Port() == "" {
		u.Host = fmt.Sprintf("%s:%d", u.Host, talosconstants.DefaultControlPlanePort)
	}

	return u
}

func talosClusterOperation(ctx context.Context,
	nodes, endpoints []string,
	talosconfig string,
	delay, maxDelay time.Duration,
	timeout int,
	operation string,
) (interface{}, error) {
	cfg, err := clientconfig.FromString(talosconfig)
	if err != nil {
		return nil, fmt.Errorf("failed to parse talosconfig %w", err)
	}

	client.WithNodes(ctx, nodes...)
	opts := []client.OptionFunc{
		client.WithConfig(cfg),
		client.WithEndpoints(endpoints...),
	}

	c, err := client.New(ctx, opts...)
	if err != nil {
		return nil, fmt.Errorf("error constructing client: %w", err)
	}

	//nolint:errcheck
	defer c.Close()

	var acceptanceFunc retry.Acceptance

	switch operation {
	case "bootstrap":
		acceptanceFunc = func(try int, nextRetryTime time.Duration) (bool, interface{}, error) {
			if bootstrapError := c.Bootstrap(ctx, &machineapi.BootstrapRequest{}); bootstrapError != nil {
				return false, nil, nil
			}
			return true, nil, nil
		}
	case "kubeconfig":
		acceptanceFunc = func(try int, nextRetryTime time.Duration) (bool, interface{}, error) {
			k, getKubeconfigErr := c.Kubeconfig(ctx)
			if getKubeconfigErr != nil {
				return false, getKubeconfigErr, nil
			}
			return true, string(k), nil
		}
	default:
		return nil, fmt.Errorf("unknown operation '%s'", operation)
	}

	status, value, err := retry.UntilTimeout(ctx, retry.Acceptor{
		Accept:   acceptanceFunc,
		Delay:    &delay,
		MaxDelay: &maxDelay,
	}, time.Duration(timeout)*time.Second)
	if !status {
		return nil, fmt.Errorf("timeout waiting for %s", operation)
	}
	if err != nil {
		return nil, err
	}
	return value, nil
}
