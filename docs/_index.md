---
title: Talos Linux
meta_desc: Provides an overview of the Talos Linux Provider for Pulumi.
layout: overview
---

The Talos Linux provider for Pulumi can be used to provision Talos Linux machines and activate Kubernetes clusters running on top of them.

## Example

{{< chooser language "typescript,python,go,csharp,yaml" >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as talos from "@pulumiverse/talos";

const bootstrapConfig = new talos.machine.Bootstrap("mynodes", {
    description: "My Site Nodes",
});
```
 
{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumiverse_talos as talos

db = talos.machine.Bootstrap("mynodes",
    description="mysite"
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"fmt"
	talos "github.com/pulumiverse/pulumi-talos/sdk/go/talos"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		site, err := talos.NewSite(ctx, "mysite", &talos.SiteArgs{
            Description: pulumi.String("mysite"),
		})
		if err != nil {
			return fmt.Errorf("error creating site: %v", err)
		}

		ctx.Export("dbId", site.Id)

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumiverse.Talos;

class TalosHosts : Stack
{
    public TalosHosts()
    {
        var db = new Machine("mynode", new MachineArgs{
            Description: "mysite"
        });
    }
}
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
  #     configPatches:
  #       - fn::toJSON:
  #           machine:
  #             install:
  #               disk: "/dev/sdd"
  # bootstrap:
  #   type: talos:machine:Bootstrap
  #   properties:
  #     node: "10.5.0.2"
  #     clientConfiguration: ${secrets.clientConfiguration}
  #   options:
  #     dependsOn:
  #       - configurationApply

outputs: {}
```

{{% /choosable %}}

{{< /chooser >}}
