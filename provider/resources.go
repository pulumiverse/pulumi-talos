// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// Package talos provides a Pulumi package for creating and managing talos resources.
package talos

import (
	"fmt"
	"path/filepath"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumiverse/pulumi-talos/provider/pkg/version"
	"github.com/siderolabs/terraform-provider-talos/shim"
)

// all of the talos token components used below.
const (
	talosPkg   = "talos"
	talosMod   = "index"
	clientMod  = "client"  // the client module
	clusterMod = "cluster" // the talos module
	machineMod = "machine" // the talos module
)

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	info := tfbridge.ProviderInfo{
		P:                 shim.ShimmedProvider(),
		Name:              talosPkg,
		Description:       "A Pulumi package for creating and managing Talos Linux machines and clusters.",
		Keywords:          []string{"pulumi", "talos", "category/infrastructure"},
		License:           "MPL-2.0",
		Homepage:          "https://talos.dev",
		GitHubOrg:         "siderolabs",
		Repository:        "https://github.com/pulumiverse/pulumi-talos",
		Version:           version.Version,
		Publisher:         "Pulumiverse",
		LogoURL:           "https://www.talos.dev/images/Sidero_stacked_darkbkgd_RGB.svg",
		PluginDownloadURL: "https://github.com/pulumiverse/pulumi-talos/releases",
		Resources: map[string]*tfbridge.ResourceInfo{
			"talos_machine_bootstrap": {Tok: tfbridge.MakeResource(talosPkg, machineMod, "Bootstrap")},
			"talos_machine_configuration_apply": {
				Tok: tfbridge.MakeResource(talosPkg, machineMod, "ConfigurationApply"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"timeouts": {Elem: &tfbridge.SchemaInfo{
						NestedType: "Timeout",
					}},
				},
			},
			"talos_machine_secrets": {Tok: tfbridge.MakeResource(talosPkg, machineMod, "Secrets")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"talos_client_configuration":  {Tok: tfbridge.MakeDataSource(talosPkg, clientMod, "Configuration")},
			"talos_cluster_kubeconfig":    {Tok: tfbridge.MakeDataSource(talosPkg, clusterMod, "Kubeconfig")},
			"talos_machine_configuration": {Tok: tfbridge.MakeDataSource(talosPkg, machineMod, "Configuration")},
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
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "pulumiverse_talos",
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumiverse/pulumi-%s/sdk/", talosPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				talosPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "Pulumiverse",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	info.SetAutonaming(255, "-")

	return info
}
