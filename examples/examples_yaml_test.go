package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getYamlBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions()
	baseYaml := base.With(integration.ProgramTestOptions{})

	return baseYaml
}

func TestYamlHappy(t *testing.T) {
	t.Skip("Yaml currently has issues")
	test := getYamlBaseOptions(t).With(integration.ProgramTestOptions{
		Dir: filepath.Join(getCwd(t), "yaml"),
	})
	integration.ProgramTest(t, &test)
}
