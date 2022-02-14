package main

import (
	"github.com/frezbo/pulumi-provider-talos/sdk/go/talos"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		b, err := talos.NewClusterSecrets(ctx, "secret", &talos.ClusterSecretsArgs{})
		if err != nil {
			return err
		}

		tc, err := talos.NewClusterConfig(ctx, "config", &talos.ClusterConfigArgs{
			ClusterEndpoint: pulumi.String("https://talos.example.com:6443"),
			ClusterName:     pulumi.String("talos"),
			Secrets:         b.Secrets,
			ConfigPatches: pulumi.Array{
				pulumi.Map{
					"op":    pulumi.String("add"),
					"path":  pulumi.String("/cluster/allowSchedulingOnMasters"),
					"value": pulumi.BoolPtr(true),
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("controlPlaneConfig", tc.ControlplaneConfig)
		ctx.Export("workerConfig", tc.WorkerConfig)
		ctx.Export("talosConfig", tc.TalosConfig)
		return nil
	})
}
