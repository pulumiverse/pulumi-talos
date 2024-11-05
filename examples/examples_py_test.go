// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.
//go:build python || all
// +build python all

package examples

import (
	//"path"
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

// func TestAccWebserverPython(t *testing.T) {
// 	test := getPythonBaseOptions(t).
// 		With(integration.ProgramTestOptions{
// 			Dir: path.Join(getCwd(t), "python/server"),
// 		})

// 	integration.ProgramTest(t, &test)
// }

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	basePython := base.With(integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return basePython
}
