package main

import (
	"github.com/frezbo/pulumi-provider-talos/sdk/v3/go/talos/bundle"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		b, err := bundle.NewSecretsBundle(ctx, "secret", &bundle.SecretsBundleArgs{
			// ConfigVersion: bundle.TalosMachineConfigVersionV1alpha1,
		}, []pulumi.ResourceOption{
			pulumi.AdditionalSecretOutputs([]string{
				"secretsBundle",
			}),
		}...)
		if err != nil {
			return err
		}
		ctx.Export("bundle", b.SecretsBundle.Cluster().Id())

		return nil
	})
}
