// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// Package talos provides a Pulumi package for creating and managing talos resources.
package talos

import (
	"fmt"
	"path/filepath"
	"unicode"

	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/siderolabs/terraform-provider-talos/shim"

	"github.com/siderolabs/pulumi-provider-talos/provider/pkg/version"
)

// all of the talos token components used below.
const (
	talosPkg = "talos"
	talosMod = "index"
)

// talosMember manufactures a type token for the random package and the given module and type.
func talosMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(talosPkg + ":" + mod + ":" + mem)
}

// talosType manufactures a type token for the random package and the given module and type.
func talosType(mod string, typ string) tokens.Type {
	return tokens.Type(talosMember(mod, typ))
}

// talosResource manufactures a standard resource token given a module and resource name.  It automatically uses the
// talos package and names the file by simply lower casing the resource's first character.
func talosResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]

	return talosType(mod+"/"+fn, res)
}

func talosDataResource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]

	return talosMember(mod+"/"+fn, res)
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() pf.ProviderInfo {
	info := tfbridge.ProviderInfo{
		Name:              talosPkg,
		Description:       "A Pulumi package for creating and managing talos resources.",
		Keywords:          []string{"pulumi", "talos"},
		License:           "MPL-2.0",
		Homepage:          "https://talos.dev",
		GitHubOrg:         "siderolabs",
		Repository:        "https://github.com/siderolabs/pulumi-provider-talos",
		Version:           version.Version,
		Publisher:         "Sidero Labs",
		LogoURL:           "https://www.talos.dev/images/Sidero_stacked_darkbkgd_RGB.svg",
		PluginDownloadURL: "https://github.com/siderolabs/pulumi-provider-talos/releases",
		Resources: map[string]*tfbridge.ResourceInfo{
			"talos_machine_bootstrap":           {Tok: talosResource(talosMod, "TalosMachineBootstrap")},
			"talos_machine_configuration_apply": {Tok: talosResource(talosMod, "TalosMachineConfigurationApply")},
			"talos_machine_secrets":             {Tok: talosResource(talosMod, "TalosMachineSecrets")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"talos_client_configuration":  {Tok: talosDataResource(talosMod, "TalosClientConfiguration")},
			"talos_cluster_kubeconfig":    {Tok: talosDataResource(talosMod, "TalosClusterKubeconfig")},
			"talos_machine_configuration": {Tok: talosDataResource(talosMod, "TalosMachineConfiguration")},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/siderolabs/pulumi-provider-%s/sdk/", talosPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				talosPkg,
			),
			GenerateResourceContainerTypes: true,
		},
	}

	return pf.ProviderInfo{
		ProviderInfo: info,
		NewProvider:  shim.NewProvider,
	}
}
