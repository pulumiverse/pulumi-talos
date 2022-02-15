package gen

import (
	"encoding/json"
	"fmt"
	"strings"

	"github.com/alecthomas/jsonschema"
	"github.com/frezbo/pulumi-provider-talos/provider/pkg/constants"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/go/common/util/contract"
	talosconstants "github.com/talos-systems/talos/pkg/machinery/constants"
)

func PulumiSchema(swagger *jsonschema.Schema) schema.PackageSpec {
	pkg := schema.PackageSpec{
		Name:        "talos",
		Description: "A Pulumi package for creating and managing talos config",
		License:     "Apache-2.0",
		Keywords:    []string{"talos", "kubernetes", "pulumi"},
		Homepage:    "https://talos.dev",
		Repository:  "https://github.com/frezbo/pulumi-provider-talos",

		Config: schema.ConfigSpec{},

		Provider: schema.ResourceSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Description: "The provider type for the Talos package",
				Type:        "object",
			},
		},

		Types:     map[string]schema.ComplexTypeSpec{},
		Resources: map[string]schema.ResourceSpec{},
		Functions: map[string]schema.FunctionSpec{},
		Language:  map[string]schema.RawMessage{},
	}

	for defintion, definitionProperties := range swagger.Definitions {

		tok := fmt.Sprintf("talos:%s:%s", "index", defintion)

		objectSpec := schema.ObjectTypeSpec{
			Description: fmt.Sprintf("Talos %s", defintion),
			Type:        "object",
			Properties:  map[string]schema.PropertySpec{},
			Language:    map[string]schema.RawMessage{},
		}

		resourceSpec := schema.ResourceSpec{
			ObjectTypeSpec:  objectSpec,
			InputProperties: map[string]schema.PropertySpec{},
			RequiredInputs:  definitionProperties.Required,
		}

		for _, definitionPropertyKey := range definitionProperties.Properties.Keys() {
			if val, ok := definitionProperties.Properties.Get(definitionPropertyKey); ok {
				// the returned value is an interface
				// we need to cast it to jsonSchema.Type to access the fields
				definitionPropertyValue := val.(*jsonschema.Type)

				resourceOutputProperty := schema.PropertySpec{
					TypeSpec: schema.TypeSpec{
						Type: definitionPropertyValue.Type,
						Ref:  openAPISpecRefToPulumiRef(definitionPropertyValue.Ref),
					},
				}
				if definitionPropertyValue.Items != nil {
					resourceOutputProperty.TypeSpec.Items = &schema.TypeSpec{
						Type: definitionPropertyValue.Items.Type,
						Ref:  openAPISpecRefToPulumiRef(definitionPropertyValue.Items.Ref),
					}
				}

				// talos defines the type as `[]byte` for `PEMEncodedCertificateAndKey` and `PEMEncodedKey`,
				// since Pulumi schema doesn't have a type for it, we'll use the anytype instead
				if defintion == "PEMEncodedCertificateAndKey" || defintion == "PEMEncodedKey" {
					resourceOutputProperty.Type = ""
					resourceOutputProperty.Ref = "pulumi.json#/Any"
				}

				resourceSpec.Properties[definitionPropertyKey] = resourceOutputProperty

				typeSpec := schema.ComplexTypeSpec{
					ObjectTypeSpec: schema.ObjectTypeSpec{
						Description: fmt.Sprintf("Talos %s type", defintion),
						Type:        "object",
						Properties:  resourceSpec.Properties,
						Language:    map[string]schema.RawMessage{},
					},
				}

				pkg.Types[tok] = typeSpec
			}
		}

		// let's add the clusterSecrets resource
		pkg.Resources["talos:index:clusterSecrets"] = schema.ResourceSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Description: "Talos secrets resource",
				Type:        "object",
				Properties: map[string]schema.PropertySpec{
					"secrets": {
						Description: "Talos Secrets Bundle",
						TypeSpec: schema.TypeSpec{
							Type: "object",
							Ref:  "#/types/talos:index:SecretsBundle",
						},
						// Secret: true,
					},
					"talosVersion": {
						Description: "Talos version the config generated for",
						TypeSpec: schema.TypeSpec{
							Type: "string",
							Ref:  "#/types/talos:index:TalosVersionOutput",
						},
					},
					"configVersion": {
						TypeSpec: schema.TypeSpec{
							Type: "string",
							Ref:  "#/types/talos:index:TalosMachineConfigVersionOutput",
						},
					},
				},
				Required: []string{
					"secrets",
					"talosVersion",
					"configVersion",
				},
			},
			InputProperties: map[string]schema.PropertySpec{
				"talosVersion": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: "the desired Talos version to generate config for (backwards compatibility, e.g. v0.8)",
				},
				"configVersion": {
					TypeSpec: schema.TypeSpec{
						OneOf: []schema.TypeSpec{
							{
								Type: "string",
							},
							{
								Type: "string",
								Ref:  "#/types/talos:index:TalosMachineConfigVersion",
							},
						},
					},
					Description: fmt.Sprintf("the desired machine config version to generate (default \"%s\")", constants.TalosMachineConfigVersion),
					Default:     constants.TalosMachineConfigVersion,
				},
			},
		}

		pkg.Types["talos:index:TalosMachineConfigVersion"] = schema.ComplexTypeSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Type: "string",
			},
			Enum: []schema.EnumValueSpec{
				{
					Value:       constants.TalosMachineConfigVersion,
					Description: "Talos Machine Configuration Version",
				},
			},
		}

		pkg.Types["talos:index:TalosMachineConfigVersionOutput"] = schema.ComplexTypeSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Type:        "object",
				Description: "Talos Machine Configuration Version Output",
			},
		}

		pkg.Types["talos:index:TalosVersionOutput"] = schema.ComplexTypeSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Type:        "object",
				Description: "Talos Version Output",
			},
		}

		pkg.Resources["talos:index:clusterConfig"] = schema.ResourceSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Description: "Talos cluster config resource",
				Type:        "object",
				Properties: map[string]schema.PropertySpec{
					"clusterName": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "cluster name",
					},
					"clusterEndpoint": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "The cluster endpoint",
					},
					"additionalSans": {
						TypeSpec: schema.TypeSpec{
							Type:  "array",
							Items: &schema.TypeSpec{Type: "string"},
						},
						Description: "additional Subject-Alt-Names for the APIServer certificate",
					},
					"configPatches": {
						TypeSpec: schema.TypeSpec{
							Type: "array",
							Items: &schema.TypeSpec{
								Type: "object",
								Ref:  "pulumi.json#/Any",
							},
						},
						Description: "generated machineconfigs (applied to all node types)",
					},
					"configPatchesControlPlane": {
						TypeSpec: schema.TypeSpec{
							Type: "array",
							Items: &schema.TypeSpec{
								Type: "object",
								Ref:  "pulumi.json#/Any",
							},
						},
						Description: "generated machineconfigs (applied to 'controlplane' types)",
					},
					"configPatchesWorker": {
						TypeSpec: schema.TypeSpec{
							Type: "array",
							Items: &schema.TypeSpec{
								Type: "object",
								Ref:  "pulumi.json#/Any",
							},
						},
						Description: "generated machineconfigs (applied to 'worker' type)",
					},
					"dnsDomain": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "the dns domain to use for cluster",
					},
					"installDisk": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "the disk to install to ",
					},
					"installImage": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "the image used to perform an installation",
					},
					"kubernetesVersion": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "desired kubernetes version to run",
					},
					"persist": {
						TypeSpec:    schema.TypeSpec{Type: "boolean"},
						Description: "persist value for configs",
					},
					"registryMirrors": {
						TypeSpec: schema.TypeSpec{
							Type:  "array",
							Items: &schema.TypeSpec{Type: "string"},
						},
						Description: "list of registry mirrors",
					},
					"talosVersion": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "the desired Talos version",
					},
					"configVersion": {
						TypeSpec:    schema.TypeSpec{Type: "string"},
						Description: "the desired machine config version to refer to",
					},
					"clusterDiscovery": {
						TypeSpec:    schema.TypeSpec{Type: "boolean"},
						Description: "cluster discovery feature",
					},
					"docs": {
						TypeSpec:    schema.TypeSpec{Type: "boolean"},
						Description: "machine config documentation enabled",
					},
					"examples": {
						TypeSpec:    schema.TypeSpec{Type: "boolean"},
						Description: "machine config examples enabled",
					},
					"kubespan": {
						TypeSpec:    schema.TypeSpec{Type: "boolean"},
						Description: "kubespan enabled",
					},
					"controlplaneConfig": {
						Description: "Talos Controlplane Config",
						TypeSpec: schema.TypeSpec{
							Type: "string",
						},
					},
					"workerConfig": {
						Description: "Talos Worker Config",
						TypeSpec: schema.TypeSpec{
							Type: "string",
						},
					},
					"talosConfig": {
						Description: "Talos Config",
						TypeSpec: schema.TypeSpec{
							Type: "string",
						},
					},
					"secrets": {
						Description: "Talos Secrets Bundle",
						TypeSpec: schema.TypeSpec{
							Type: "object",
							Ref:  "#/types/talos:index:SecretsBundle",
						},
						// Secret: true,
					},
				},
				Required: []string{
					"clusterName",
					"clusterEndpoint",
					"additionalSans",
					"configPatches",
					"configPatchesControlPlane",
					"configPatchesWorker",
					"dnsDomain",
					"installDisk",
					"installImage",
					"kubernetesVersion",
					"persist",
					"registryMirrors",
					"talosVersion",
					"configVersion",
					"clusterDiscovery",
					"docs",
					"examples",
					"kubespan",
					"controlplaneConfig",
					"workerConfig",
					"talosConfig",
					"secrets",
				},
			},
			InputProperties: map[string]schema.PropertySpec{
				"clusterName": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: "cluster name",
				},
				"clusterEndpoint": {
					TypeSpec: schema.TypeSpec{Type: "string"},
					Description: `The cluster endpoint is the URL for the Kubernetes API. If you decide to use
a control plane node, common in a single node control plane setup, use port 6443 as
this is the port that the API server binds to on every control plane node. For an HA
setup, usually involving a load balancer, use the IP and port of the load balancer.`,
				},
				"secrets": {
					Description: "Talos Secrets Bundle",
					TypeSpec: schema.TypeSpec{
						Type: "object",
						Ref:  "#/types/talos:index:SecretsBundle",
					},
					// Secret: true,
				},
				"additionalSans": {
					TypeSpec: schema.TypeSpec{
						Type:  "array",
						Items: &schema.TypeSpec{Type: "string"},
					},
					Description: "additional Subject-Alt-Names for the APIServer certificate",
				},
				"configPatches": {
					TypeSpec: schema.TypeSpec{
						Type: "array",
						Items: &schema.TypeSpec{
							Type: "object",
							Ref:  "pulumi.json#/Any",
						},
					},
					Description: "patch generated machineconfigs (applied to all node types)",
				},
				"configPatchesControlPlane": {
					TypeSpec: schema.TypeSpec{
						Type: "array",
						Items: &schema.TypeSpec{
							Type: "object",
							Ref:  "pulumi.json#/Any",
						},
					},
					Description: "patch generated machineconfigs (applied to 'controlplane' types)",
				},
				"configPatchesWorker": {
					TypeSpec: schema.TypeSpec{
						Type: "array",
						Items: &schema.TypeSpec{
							Type: "object",
							Ref:  "pulumi.json#/Any",
						},
					},
					Description: "patch generated machineconfigs (applied to 'worker' type)",
				},
				"dnsDomain": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: fmt.Sprintf("the dns domain to use for cluster (default \"%s\")", talosconstants.DefaultDNSDomain),
					Default:     talosconstants.DefaultDNSDomain,
				},
				"installDisk": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: fmt.Sprintf("the disk to install to (default \"%s\")", constants.TalosInstallDisk),
					Default:     constants.TalosInstallDisk,
				},
				"installImage": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: fmt.Sprintf("the image used to perform an installation (default \"ghcr.io/talos-systems/installer:%s\")", constants.TalosInstallImageVersion),
					Default:     fmt.Sprintf("ghcr.io/talos-systems/installer:%s", constants.TalosInstallImageVersion),
				},
				"kubernetesVersion": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: fmt.Sprintf("desired kubernetes version to run (default \"%s\")", talosconstants.DefaultKubernetesVersion),
					Default:     talosconstants.DefaultKubernetesVersion,
				},
				"persist": {
					TypeSpec:    schema.TypeSpec{Type: "boolean"},
					Description: fmt.Sprintf("the desired persist value for configs (default %t)", constants.TalosPersistConfig),
					Default:     constants.TalosPersistConfig,
				},
				"registryMirrors": {
					TypeSpec: schema.TypeSpec{
						Type:  "array",
						Items: &schema.TypeSpec{Type: "string"},
					},
					Description: "list of registry mirrors to use in format: <registry host>=<mirror URL>",
				},
				"talosVersion": {
					TypeSpec: schema.TypeSpec{
						Ref: "#/types/talos:index:TalosVersionOutput",
					},
					Description: "the desired Talos version to refer to",
				},
				"configVersion": {
					TypeSpec: schema.TypeSpec{
						Ref: "#/types/talos:index:TalosMachineConfigVersionOutput",
					},
					Description: "the desired machine config version to refer to",
				},
				"clusterDiscovery": {
					TypeSpec:    schema.TypeSpec{Type: "boolean"},
					Description: fmt.Sprintf("enable cluster discovery feature (default %t)", constants.TalosClusterDiscovery),
					Default:     constants.TalosClusterDiscovery,
				},
				"docs": {
					TypeSpec:    schema.TypeSpec{Type: "boolean"},
					Description: fmt.Sprintf("renders all machine configs adding the documentation for each field (default %t)", constants.TalosConfigDocs),
					Default:     constants.TalosConfigDocs,
				},
				"examples": {
					TypeSpec:    schema.TypeSpec{Type: "boolean"},
					Description: fmt.Sprintf("renders all machine configs with the commented examples (default %t)", constants.TalosConfigExamples),
					Default:     constants.TalosConfigExamples,
				},
				"kubespan": {
					TypeSpec:    schema.TypeSpec{Type: "boolean"},
					Description: "enable kubespan feature",
				},
			},
			RequiredInputs: []string{
				"clusterName",
				"clusterEndpoint",
				"secrets",
			},
		}
	}

	pkg.Resources["talos:index:nodeBootstrap"] = schema.ResourceSpec{
		ObjectTypeSpec: schema.ObjectTypeSpec{
			Description: "A node bootstrap resource",
			Type:        "object",
			Properties: map[string]schema.PropertySpec{
				"endpoint": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: "node endpoint address",
				},
				"node": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: "node address",
				},
				"talosConfig": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: "talosconfig",
				},
				"timeout": {
					TypeSpec:    schema.TypeSpec{Type: "integer"},
					Description: "wait timeout in seconds",
				},
			},
			Required: []string{
				"endpoint",
				"node",
				"talosConfig",
				"timeout",
			},
		},
		InputProperties: map[string]schema.PropertySpec{
			"endpoint": {
				TypeSpec:    schema.TypeSpec{Type: "string"},
				Description: "node endpoint address",
			},
			"node": {
				TypeSpec:    schema.TypeSpec{Type: "string"},
				Description: "node address",
			},
			"talosConfig": {
				TypeSpec:    schema.TypeSpec{Type: "string"},
				Description: "talosconfig",
			},
			"timeout": {
				TypeSpec:    schema.TypeSpec{Type: "integer"},
				Description: fmt.Sprintf("timeout in seconds (default %d)", constants.TalosBootstrapResourceTimeout),
				Default:     constants.TalosBootstrapResourceTimeout,
			},
		},
		RequiredInputs: []string{
			"endpoint",
			"node",
			"talosConfig",
		},
	}

	goImportPath := "github.com/frezbo/pulumi-provider-talos/sdk/go/talos"

	pkg.Language["go"] = rawMessage(map[string]interface{}{
		"importBasePath":                 goImportPath,
		"generateResourceContainerTypes": true,
	})

	pkg.Language["csharp"] = rawMessage(map[string]interface{}{
		"packageReferences": map[string]string{
			"Pulumi": "3.*",
		},
		"namespaces": map[string]string{
			"bundle": "bundle",
		},
	})

	pkg.Language["python"] = rawMessage(map[string]interface{}{
		"requires": map[string]string{
			"pulumi": ">=3.0.0,<4.0.0",
		},
	})

	pkg.Language["nodejs"] = rawMessage(map[string]interface{}{
		"dependencies": map[string]string{
			"@pulumi/pulumi": "^3.0.0",
		},
		"devDependencies": map[string]string{
			"typescript":  "^3.7.0",
			"@types/node": "^17.0.0",
		},
	})

	return pkg
}

func rawMessage(v interface{}) schema.RawMessage {
	bytes, err := json.Marshal(v)
	contract.Assert(err == nil)
	return bytes
}

func openAPISpecRefToPulumiRef(ref string) string {
	if ref != "" {
		// convert openAPI schema references to Pulumi schema reference
		// remove `definitions` and replace by `types`
		// ref: https://www.pulumi.com/docs/guides/pulumi-packages/schema/#
		ref = strings.ReplaceAll(ref, "#/definitions/", "")
		ref = fmt.Sprintf("%s/talos:%s:%s", "#/types", "index", ref)
		return ref
	}
	return ref
}
