// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// Package talos provides a Pulumi package for creating and managing talos resources.
package talos

import (
	"fmt"
	"path/filepath"

	// embed is used to embed the schema files in the provider
	_ "embed"

	"github.com/siderolabs/terraform-provider-talos/pkg/talos"

	pf "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	tks "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"

	"github.com/pulumiverse/pulumi-talos/provider/pkg/version"
)

// all the talos token components used below.
const (
	talosPkg        = "talos"
	talosMod        = "index"
	clientMod       = "client"        // the client module
	clusterMod      = "cluster"       // the cluster module
	machineMod      = "machine"       // the machine module
	imageFactoryMod = "image_factory" // the image factory module
)

//go:embed cmd/pulumi-resource-talos/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	prov := tfbridge.ProviderInfo{
		P:                 pf.ShimProvider(talos.New()),
		Name:              talosPkg,
		DisplayName:       "Talos",
		Description:       "A Pulumi package for creating and managing Talos Linux machines and clusters.",
		Keywords:          []string{"pulumi", "talos", "category/infrastructure"},
		License:           "MPL-2.0",
		Homepage:          "https://www.talos.dev",
		GitHubOrg:         "siderolabs",
		Repository:        "https://github.com/pulumiverse/pulumi-talos",
		Version:           version.Version,
		Publisher:         "Pulumiverse",
		LogoURL:           "https://raw.githubusercontent.com/pulumiverse/pulumi-talos/refs/heads/main/assets/talos-logo.png",
		PluginDownloadURL: "github://api.github.com/pulumiverse",
		MetadataInfo:      tfbridge.NewProviderMetadata(metadata),
		//MuxWith: []tfbridge.MuxProvider{
		//	native.NewProvider(),
		//},
		ExtraTypes: map[string]schema.ComplexTypeSpec{
			"talos:machine/generated:Key": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A Machine Secrets Private Key",
					Properties: map[string]schema.PropertySpec{
						"key": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "Private Key",
							Secret:      true,
						},
					},
					Required: []string{
						"key",
					},
				},
			},
			"talos:machine/generated:Certificate": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A Machine Secrets Certificate",
					Properties: map[string]schema.PropertySpec{
						"cert": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "Certificate",
						},
						"key": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "Private Key",
							Secret:      true,
						},
					},
					Required: []string{
						"cert",
						"key",
					},
				},
			},
			"talos:machine/generated:Cluster": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A Machine Secrets Cluster Info",
					Properties: map[string]schema.PropertySpec{
						"id": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "Certificate",
						},
						"secret": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "Private Key",
							Secret:      true,
						},
					},
					Required: []string{
						"id",
						"secret",
					},
				},
			},
			"talos:machine/generated:KubernetesSecrets": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A Machine Secrets Bootstrap data",
					Properties: map[string]schema.PropertySpec{
						"bootstrapToken": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The bootstrap token for the talos kubernetes cluster",
							Secret:      true,
						},
						"secretboxEncryptionSecret": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The secretbox encryption secret for the talos kubernetes cluster",
							Secret:      true,
						},
						"aescbcEncryptionSecret": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The aescbc encryption secret for the talos kubernetes cluster",
							Secret:      true,
						},
					},
					Required: []string{
						"bootstrapToken",
						"secretboxEncryptionSecret",
					},
				},
			},
			"talos:machine/generated:TrustdInfo": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A Machine Secrets Trust daemon info",
					Properties: map[string]schema.PropertySpec{
						"token": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The trustd token for the talos kubernetes cluster",
							Secret:      true,
						},
					},
					Required: []string{
						"token",
					},
				},
			},
			"talos:machine/generated:Certificates": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A complete Machine Secrets Certificates configuration",
					Properties: map[string]schema.PropertySpec{
						"etcd": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Certificate",
							},
						},
						"k8s": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Certificate",
							},
						},
						"k8sAggregator": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Certificate",
							},
						},
						"k8sServiceaccount": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Key",
							},
						},
						"os": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Certificate",
							},
						},
					},
					Required: []string{
						"etcd",
						"k8s",
						"k8sAggregator",
						"k8sServiceaccount",
						"os",
					},
				},
			},
			"talos:machine/generated:ClientConfiguration": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A Client Configuration",
					Properties: map[string]schema.PropertySpec{
						"caCertificate": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The client CA certificate",
						},
						"clientCertificate": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The client certificate",
						},
						"clientKey": {
							TypeSpec:    schema.TypeSpec{Type: "string"},
							Description: "The client private key",
							Secret:      true,
						},
					},
					Required: []string{
						"caCertificate",
						"clientCertificate",
						"clientKey",
					},
				},
			},
			"talos:machine/generated:MachineSecrets": {
				ObjectTypeSpec: schema.ObjectTypeSpec{
					Type:        "object",
					Description: "A complete Machine Secrets configuration",
					Properties: map[string]schema.PropertySpec{
						"certs": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Certificates",
							},
						},
						"cluster": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:Cluster",
							},
						},
						"secrets": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:KubernetesSecrets",
							},
						},
						"trustdinfo": {
							TypeSpec: schema.TypeSpec{
								Ref: "#types/talos:machine/generated:TrustdInfo",
							},
						},
					},
					Required: []string{
						"certs",
						"cluster",
						"secrets",
						"trustdinfo",
					},
				},
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			"talos_image_factory_schematic": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"schematic": {
						CSharpName: "SchematicData",
					},
				},
			},
			"talos_machine_bootstrap": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"client_configuration": {
						Elem: &tfbridge.SchemaInfo{
							Type: "talos:machine/generated:ClientConfiguration",
						},
					},
				},
			},
			"talos_machine_configuration_apply": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"timeouts": {
						Elem: &tfbridge.SchemaInfo{
							NestedType: "Timeout",
						},
					},
					"client_configuration": {
						Elem: &tfbridge.SchemaInfo{
							Type: "talos:machine/generated:ClientConfiguration",
						},
					},
				},
			},
			"talos_machine_secrets": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"client_configuration": {
						Elem: &tfbridge.SchemaInfo{
							Type: "talos:machine/generated:ClientConfiguration",
						},
					},
					"machine_secrets": {
						Elem: &tfbridge.SchemaInfo{
							Type: "talos:machine/generated:MachineSecrets",
						},
					},
				},
			},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"talos_machine_configuration": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"machine_secrets": {
						Elem: &tfbridge.SchemaInfo{
							Type: "talos:machine/generated:MachineSecrets",
						},
					},
				},
			},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@pulumiverse/talos",
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			RespectSchemaVersion: true,
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "pulumiverse_talos",
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
			PyProject:            struct{ Enabled bool }{true},
			RespectSchemaVersion: true,
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumiverse/pulumi-%s/sdk/", talosPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				talosPkg,
			),
			GenerateResourceContainerTypes: true,
			RespectSchemaVersion:           true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "Pulumiverse",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			RespectSchemaVersion: true,
		},
	}

	prov.MustComputeTokens(
		tks.KnownModules(
			"talos_",
			"index",
			[]string{
				clientMod,
				clusterMod,
				machineMod,
				imageFactoryMod,
			},
			tks.MakeStandard(talosPkg),
		),
	)
	prov.SetAutonaming(255, "-")
	prov.MustApplyAutoAliases()

	return prov
}
