// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// Package talos provides a Pulumi package for creating and managing talos resources.
package talos

import (
	"fmt"
	"path/filepath"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/siderolabs/terraform-provider-talos/talos"

	"github.com/siderolabs/pulumi-provider-talos/provider/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python.
	mainPkg = "talos"
	// modules:
	mainMod    = "index"   // the talos module
	clientMod  = "client"  // the client module
	clusterMod = "cluster" // the talos module
	machineMod = "machine" // the talos module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := shimv2.NewProvider(talos.Provider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:                    p,
		Name:                 "talos",
		DisplayName:          "Talos Linux",
		Publisher:            "Siderolabs",
		LogoURL:              "https://www.talos.dev/images/Sidero_stacked_darkbkgd_RGB.svg",
		PluginDownloadURL:    "github://api.github.com/siderolabs/pulumi-provider-talos",
		Description:          "A Pulumi package for creating and managing talos resources.",
		Keywords:             []string{"pulumi", "talos", "category/os"},
		License:              "MPL-2.0 license ",
		Homepage:             "https://talos.dev",
		Repository:           "https://github.com/siderolabs/pulumi-provider-talos",
		GitHubOrg:            "siderolabs",
		Config:               map[string]*tfbridge.SchemaInfo{},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"talos_client_configuration":               {Tok: tfbridge.MakeResource(mainPkg, clientMod, "Configuration")},
			"talos_cluster_kubeconfig":                 {Tok: tfbridge.MakeResource(mainPkg, clusterMod, "Kubeconfig")},
			"talos_machine_bootstrap":                  {Tok: tfbridge.MakeResource(mainPkg, machineMod, "Bootstrap")},
			"talos_machine_configuration_apply":        {Tok: tfbridge.MakeResource(mainPkg, machineMod, "ConfigurationApply")},
			"talos_machine_configuration_controlplane": {Tok: tfbridge.MakeResource(mainPkg, machineMod, "ConfigurationControlplane")},
			"talos_machine_configuration_worker":       {Tok: tfbridge.MakeResource(mainPkg, machineMod, "ConfigurationWorker")},
			"talos_machine_secrets":                    {Tok: tfbridge.MakeResource(mainPkg, machineMod, "Secrets")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@siderolabs/pulumi-talos",
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
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
