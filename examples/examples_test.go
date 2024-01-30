// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

package examples

import (
	"context"
	"os"
	"path/filepath"
	"testing"

	"github.com/stretchr/testify/require"
	tc "github.com/testcontainers/testcontainers-go"
	tcc "github.com/testcontainers/testcontainers-go/modules/compose"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

func getBaseOptions(t *testing.T) integration.ProgramTestOptions {
	return integration.ProgramTestOptions{
		LocalProviders: []integration.LocalDependency{{
			Package: "talos",
			Path:    filepath.Join(getCwd(t), "..", "bin"),
		}},
	}
}

func startNodes(t *testing.T) error {
	composePath := filepath.Join(getCwd(t), "testdata", "docker-compose.yaml")
	compose, err := tcc.NewDockerComposeWith(
		tcc.WithStackFiles(composePath),
		tcc.WithLogger(tc.TestLogger(t)),
	)
	require.NoError(t, err)

	t.Cleanup(func() {
		err := compose.Down(context.Background(),
			tcc.RemoveOrphans(true),
			tcc.RemoveImagesLocal,
			tcc.RemoveVolumes(true),
		)
		require.NoError(t, err)
	})

	ctx, cancel := context.WithCancel(context.Background())
	t.Cleanup(cancel)

	return compose.Up(ctx, tcc.Wait(true))
}
