// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

//go:generate go run ./generate.go

// Package main in the default entrypoint for the Pulumi provider.
package main

import (
	"context"

	// embed is used to embed the schema files in the provider
	_ "embed"

	"github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"

	talos "github.com/pulumiverse/pulumi-talos/provider"
)

//go:embed schema-embed.json
var pulumiSchema []byte

//go:embed bridge-metadata.json
var bridgeMetadata []byte

func main() {
	meta := tfbridge.ProviderMetadata{
		PackageSchema:  pulumiSchema,
		BridgeMetadata: bridgeMetadata,
	}
	tfbridge.Main(context.Background(), "talos", talos.Provider(), meta)
}
