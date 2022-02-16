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
			ConfigPatches: talos.ConfigPatchesArgs{
				PatchFiles: pulumi.AssetOrArchiveArray{
					pulumi.NewFileAsset("patches/common.json"),
				},
			},
			ConfigPatchesControlPlane: talos.ConfigPatchesArgs{
				Patches: pulumi.Array{
					pulumi.Map{
						"op":   pulumi.String("add"),
						"path": pulumi.String("/machine/network/interfaces"),
						"value": pulumi.MapArray{
							pulumi.Map{
								"interface": pulumi.String("bond0"),
								"vip": pulumi.Map{
									"ip": pulumi.String("192.168.1.50"),
								},
							},
						},
					},
				},
				PatchFiles: pulumi.AssetOrArchiveArray{
					pulumi.NewFileAsset("patches/controlplane.yaml"),
				},
			},
			ConfigPatchesWorker: talos.ConfigPatchesArgs{
				PatchFiles: pulumi.AssetOrArchiveArray{
					pulumi.NewFileAsset("patches/network.yaml"),
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("controlPlaneConfig", tc.ControlplaneConfig)
		ctx.Export("workerConfig", tc.WorkerConfig)
		ctx.Export("talosConfig", tc.TalosConfig)

		_, err = talos.NewNodeBootstrap(ctx, "bootstrap", &talos.NodeBootstrapArgs{
			Endpoint:    pulumi.String("192.168.15.40"),
			Node:        pulumi.String("192.168.15.40"),
			TalosConfig: tc.TalosConfig,
		})
		if err != nil {
			return err
		}
		return nil
	})
}
