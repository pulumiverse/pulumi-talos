import * as talos from "@pulumi/talos";

const b = new talos.ClusterSecrets("secrets", {});

const tc = new talos.ClusterConfig("config", {
    clusterName: "talos-cluster",
    secrets: b.secrets,
    clusterEndpoint: "https://talos.example.com:6443",
    configPatches: {
        patchFiles: [
            "patches/common.json"
        ],
    },
    configPatchesControlPlane: {
        patches: [
            {
                "op": "add",
                "path": "/machine/network/interfaces",
                "value": [
                    {
                        "interface": "bond0",
                        "vip": {
                            "ip": "192.168.1.50",
                        },
                    },
                ],
            },
        ],
        patchFiles: [
            "patches/controlplane.yaml",
        ]
    },
    configPatchesWorker: {
        patchFiles: [
            "patches/network.yaml",
        ],
    },
}, {
    additionalSecretOutputs: [
				"controlplaneConfig",
				"workerConfig",
				"talosConfig",
    ]
});

new talos.NodeBootstrap("bootstrap", {
    endpoint: "192.168.1.50",
    node: "192.168.1.50",
    talosConfig: tc.talosConfig,
});

const kubeconfig = tc.talosConfig.apply(talosconfig => {
    talos.getKubeConfig({
        endpoint: "192.168.1.50",
        node: "192.168.1.50",
        talosConfig: talosconfig,
    })
}
);


export const talosconfig = tc.talosConfig;
export const talosControlPlaneConfig = tc.controlplaneConfig;
export const talosWorkerConfig = tc.workerConfig;
export const kubeConfig = kubeconfig;
