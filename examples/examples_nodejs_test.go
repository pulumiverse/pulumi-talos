// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.
//go:build nodejs || all
// +build nodejs all

package examples

import (
	//"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

// func TestAccWebserverNode(t *testing.T) {
// 	test := getJSBaseOptions(t).
// 		With(integration.ProgramTestOptions{
// 			Dir: path.Join(getCwd(t), "ts/server"),
// 		})

// 	integration.ProgramTest(t, &test)
// }

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseJS := base.With(integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
		Dependencies: []string{
			"@pulumiverse/scaleway",
		},
	})

	return baseJS
}
