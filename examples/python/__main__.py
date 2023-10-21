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
