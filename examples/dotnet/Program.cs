using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using Pulumi;
using Talos = Pulumiverse.Talos;

return await Deployment.RunAsync(() => 
{
    var secrets = new Talos.Machine.Secrets("secrets");

    var configuration = Talos.Machine.GetConfiguration.Invoke(new()
    {
        ClusterName = "exampleCluster",
        MachineType = "controlplane",
        ClusterEndpoint = "https://cluster.local:6443",
        MachineSecrets = secrets.MachineSecrets,
    });

    var configurationApply = new Talos.Machine.ConfigurationApply("configurationApply", new()
    {
        ClientConfiguration = secrets.ClientConfiguration,
        MachineConfigurationInput = configuration,
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

