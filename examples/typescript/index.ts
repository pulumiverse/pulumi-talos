import * as pulumi from "@pulumi/pulumi";
import * as talos from "@pulumiverse/talos";

const secrets = new talos.machine.Secrets("secrets", {});

const configuration = talos.machine.getConfigurationOutput({
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
