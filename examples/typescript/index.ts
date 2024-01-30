import * as pulumi from "@pulumi/pulumi";
import * as talos from "@pulumiverse/talos";

const config = new pulumi.Config();
const name = config.require("name");
const endpoint = config.require("endpoint");
const node0 = config.require("node0");

const secrets = new talos.machine.Secrets("secrets", {});

const configuration = talos.machine.getConfigurationOutput({
    clusterName: name,
    machineType: "controlplane",
    clusterEndpoint: endpoint,
    machineSecrets: secrets.machineSecrets,
});

const configurationApply = new talos.machine.ConfigurationApply("configurationApply", {
    clientConfiguration: secrets.clientConfiguration,
    machineConfigurationInput: configuration.machineConfiguration,
    node: node0,
    configPatches: [JSON.stringify({
        machine: {
            install: {
                disk: "/dev/sdd",
            },

            // For integration tests
            features: {
              hostDNS: {
                enabled: true,
                forwardKubeDNSToHost: true,
              },
            },
        },
    })],
});

const bootstrap = new talos.machine.Bootstrap("bootstrap", {
    node: node0,
    clientConfiguration: secrets.clientConfiguration,
}, {
    dependsOn: [configurationApply],
});

const health = talos.cluster.getHealthOutput({
    controlPlaneNodes: [bootstrap.node],
    endpoints: [bootstrap.endpoint],
    clientConfiguration: secrets.clientConfiguration,
    timeouts: { read: "4m" },
});
