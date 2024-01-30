package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
	"github.com/stretchr/testify/require"
)

func TestSimpleTs(t *testing.T) {
	require.NoError(t, startNodes(t), "failed to start docker nodes")

	test := getJSBaseOptions(t).With(integration.ProgramTestOptions{
		Dir: filepath.Join(getCwd(t), "typescript"),
		Config: map[string]string{
			"name":     "exampleCluster",
			"endpoint": "https://cluster.local:6443",
			"node0":    "10.6.0.2",
		},
	})
	integration.ProgramTest(t, &test)
}

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions(t)
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@pulumiverse/talos",
		},
	})

	return baseJS
}
