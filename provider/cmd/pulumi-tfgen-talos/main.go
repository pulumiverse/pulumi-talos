// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

// Package main is th tfgen entrypoint for the Pulumi provider.
package main

import (
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen"

	talos "github.com/siderolabs/pulumi-provider-talos/provider"
	"github.com/siderolabs/pulumi-provider-talos/provider/pkg/version"
)

func main() {
	// Modify the path to point to the new provider
	tfgen.Main("talos", version.Version, talos.Provider())
}
