package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-talos/sdk/go/talos/machine"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		secrets, err := machine.NewSecrets(ctx, "secrets", nil)
		if err != nil {
			return err
		}

		configuration := machine.GetConfigurationOutput(ctx, machine.GetConfigurationOutputArgs{
			ClusterName:     pulumi.String("exampleCluster"),
			MachineType:     pulumi.String("controlplane"),
			ClusterEndpoint: pulumi.String("https://cluster.local:6443"),
			MachineSecrets:  secrets.MachineSecrets,
		}, nil)

		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"machine": map[string]interface{}{
				"install": map[string]interface{}{
					"disk": "/dev/sdd",
				},
			},
		})
		if err != nil {
			return err
		}
		json0 := string(tmpJSON0)
		configurationApply, err := machine.NewConfigurationApply(ctx, "configurationApply", &machine.ConfigurationApplyArgs{
			ClientConfiguration:       secrets.ClientConfiguration,
			MachineConfigurationInput: configuration.MachineConfiguration(),
			Node:                      pulumi.String("10.5.0.2"),
			ConfigPatches: pulumi.StringArray{
				pulumi.String(json0),
			},
		})
		if err != nil {
			return err
		}
		_, err = machine.NewBootstrap(ctx, "bootstrap", &machine.BootstrapArgs{
			Node:                pulumi.String("10.5.0.2"),
			ClientConfiguration: secrets.ClientConfiguration,
		}, pulumi.DependsOn([]pulumi.Resource{
			configurationApply,
		}))
		if err != nil {
			return err
		}
		return nil
	})
}
