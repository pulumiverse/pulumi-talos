package main

import (
	"github.com/frezbo/pulumi-provider-talos/sdk/v3/go/talos/bundle"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// create a simple two node kind cluster
		// with one control-plane and one worer node
		bundle, err := bundle.NewSecretsBundle(ctx, "secret", &bundle.SecretsBundleArgs{
			ConfigVersion: bundle.TalosMachineConfigVersionV1alpha1,
		})
		if err != nil {
			return err
		}
		ctx.Export("bundle", bundle.SecretsBundle.Cluster().ID())
		return nil
	})
}
