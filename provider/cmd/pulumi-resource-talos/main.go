// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

//go:generate go run ./generate.go

// Package main in the default entrypoint for the Pulumi provider.
package main

import (
	_ "embed"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"

	talos "github.com/siderolabs/pulumi-provider-talos/provider"
	"github.com/siderolabs/pulumi-provider-talos/provider/pkg/version"
)

//go:embed schema-embed.json
var pulumiSchema []byte

func main() {
	// Modify the path to point to the new provider
	tfbridge.Main("talos", version.Version, talos.Provider(), pulumiSchema)
}
