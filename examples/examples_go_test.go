// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.
//go:build go || all
// +build go all

package examples

import (
	//"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

// func TestAccWebserverGo(t *testing.T) {
// 	test := getGoBaseOptions(t).
// 		With(integration.ProgramTestOptions{
// 			Dir: filepath.Join(getCwd(t), "go/server"),
// 		})

// 	integration.ProgramTest(t, &test)
// }

func getGoBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)

	baseGo := base.With(integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
		Dependencies: []string{
			"github.com/pulumiverse/pulumi-scaleway/sdk",
		},
	})

	return baseGo
}
