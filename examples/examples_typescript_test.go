package examples

import (
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getTsBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions()
	baseTs := base.With(integration.ProgramTestOptions{
		Dependencies: []string{"@pulumiverse/talos"},
	})

	return baseTs
}

func TestTsHappy(t *testing.T) {
	test := getTsBaseOptions(t).With(integration.ProgramTestOptions{
		Dir: filepath.Join(getCwd(t), "typescript"),
	})
	integration.ProgramTest(t, &test)
}
