//go:build dotnet || all
// +build dotnet all

package examples

import (
	//"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

// func TestAccWebserverDotnet(t *testing.T) {
// 	test := getCsharpBaseOptions(t).
// 		With(integration.ProgramTestOptions{
// 			Dir: path.Join(getCwd(t), "dotnet/server"),
// 		})

// 	integration.ProgramTest(t, &test)
// }

func getCsharpBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseCsharp := base.With(integration.ProgramTestOptions{
		ExpectRefreshChanges: true,
		Dependencies: []string{
			"Pulumiverse.Scaleway",
		},
	})

	return baseCsharp
}
