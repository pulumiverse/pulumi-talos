---
title: Talos Linux
meta_desc: Provides an overview of the Talos Linux Provider for Pulumi.
layout: package
---

The Talos Linux provider for Pulumi can be used to provision Talos Linux machines and activate Kubernetes clusters running on top of them.

## Example

{{< chooser language "typescript,python,go,csharp,yaml" >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as talos from "@pulumiverse/talos";

const secrets = new talos.machine.Secrets("secrets", {});

const configuration = talos.machine.ConfigurationOutput({
    clusterName: "exampleCluster",
    machineType: "controlplane",
    clusterEndpoint: "https://cluster.local:6443",
    machineSecrets: secrets.machineSecrets,
});

const configurationApply = new talos.machine.ConfigurationApply("configurationApply", {
    clientConfiguration: secrets.clientConfiguration,
    machineConfigurationInput: configuration.machineConfiguration,
    node: "10.5.0.2",
    configPatches: [JSON.stringify({
        machine: {
            install: {
                disk: "/dev/sdd",
            },
        },
    })],
});

const bootstrap = new talos.machine.Bootstrap("bootstrap", {
    node: "10.5.0.2",
    clientConfiguration: secrets.clientConfiguration,
}, {
    dependsOn: [configurationApply],
});
```
 
{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import json
import pulumiverse_talos as talos

secrets = talos.machine.Secrets("secrets")

configuration = talos.machine.configuration_output(cluster_name="exampleCluster",
    machine_type="controlplane",
    cluster_endpoint="https://cluster.local:6443",
    machine_secrets=secrets.machine_secrets)

configuration_apply = talos.machine.ConfigurationApply("configurationApply",
    client_configuration=secrets.client_configuration,
    machine_configuration_input=configuration.machine_configuration,
    node="10.5.0.2",
    config_patches=[json.dumps({
        "machine": {
            "install": {
                "disk": "/dev/sdd",
            },
        },
    })])

bootstrap = talos.machine.Bootstrap("bootstrap",
    node="10.5.0.2",
    client_configuration=secrets.client_configuration,
    opts=pulumi.ResourceOptions(depends_on=[configuration_apply]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
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

		configuration := machine.ConfigurationOutput(ctx, machine.ConfigurationOutputArgs{
			ClusterName:     pulumi.String("exampleCluster"),
			MachineType:     pulumi.String("controlplane"),
			ClusterEndpoint: pulumi.String("https://cluster.local:6443"),
			MachineSecrets:  secrets.MachineSecrets,
		}, nil).ApplyT(func(invoke machine.ConfigurationResult) (*string, error) {
			return invoke.MachineConfiguration, nil
		}).(pulumi.StringPtrOutput)
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
			MachineConfigurationInput: *pulumi.String(configuration),
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
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Pulumi;
using Talos = Pulumiverse.Talos;

return await Deployment.RunAsync(() => 
{
    var secrets = new Talos.Machine.Secrets("secrets");

    var configuration = Talos.Machine.Configuration.Invoke(new()
    {
        ClusterName = "exampleCluster",
        MachineType = "controlplane",
        ClusterEndpoint = "https://cluster.local:6443",
        MachineSecrets = secrets.MachineSecrets,
    });

    var configurationApply = new Talos.Machine.ConfigurationApply("configurationApply", new()
    {
        ClientConfiguration = secrets.ClientConfiguration,
        MachineConfigurationInput = configuration.MachineConfiguration,
        Node = "10.5.0.2",
        ConfigPatches = new[]
        {
            JsonSerializer.Serialize(new Dictionary<string, object?>
            {
                ["machine"] = new Dictionary<string, object?>
                {
                    ["install"] = new Dictionary<string, object?>
                    {
                        ["disk"] = "/dev/sdd",
                    },
                },
            }),
        },
    });

    var bootstrap = new Talos.Machine.Bootstrap("bootstrap", new()
    {
        Node = "10.5.0.2",
        ClientConfiguration = secrets.ClientConfiguration,
    }, new CustomResourceOptions
    {
        DependsOn = new[]
        {
            configurationApply,
        },
    });

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: talos
runtime: yaml
description: A minimal Talos program in Pulumi YAML
variables:
  configuration:
    fn::invoke:
      function: talos:machine/configuration:Configuration
      arguments:
        clusterName: "exampleCluster"
        machineType: "controlplane"
        clusterEndpoint: "https://cluster.local:6443"
        machineSecrets: ${secrets.machineSecrets}
      return: machineConfiguration

resources:
  secrets:
    type: talos:machine/secrets:Secrets
  configurationApply:
    type: talos:machine/configurationApply:ConfigurationApply
    properties:
      clientConfiguration: ${secrets.clientConfiguration}
      machineConfigurationInput: ${configuration}
      node: "10.5.0.2"
      configPatches:
        - fn::toJSON:
            machine:
              install:
                disk: "/dev/sdd"
  bootstrap:
    type: talos:machine:Bootstrap
    properties:
      node: "10.5.0.2"
      clientConfiguration: ${secrets.clientConfiguration}
    options:
      dependsOn:
        - ${configurationApply}

outputs: {}
```

{{% /choosable %}}

{{< /chooser >}}
