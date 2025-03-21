// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Waits for the Talos cluster to be healthy. Can be used as a dependency before running other operations on the cluster.
 */
export function getHealth(args: GetHealthArgs, opts?: pulumi.InvokeOptions): Promise<GetHealthResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("talos:cluster/getHealth:getHealth", {
        "clientConfiguration": args.clientConfiguration,
        "controlPlaneNodes": args.controlPlaneNodes,
        "endpoints": args.endpoints,
        "skipKubernetesChecks": args.skipKubernetesChecks,
        "timeouts": args.timeouts,
        "workerNodes": args.workerNodes,
    }, opts);
}

/**
 * A collection of arguments for invoking getHealth.
 */
export interface GetHealthArgs {
    /**
     * The client configuration data
     */
    clientConfiguration: inputs.cluster.GetHealthClientConfiguration;
    /**
     * List of control plane nodes to check for health.
     */
    controlPlaneNodes: string[];
    /**
     * endpoints to use for the health check client. Use at least one control plane endpoint.
     */
    endpoints: string[];
    /**
     * Skip Kubernetes component checks, this is useful to check if the nodes has finished booting up and kubelet is running. Default is false.
     */
    skipKubernetesChecks?: boolean;
    timeouts?: inputs.cluster.GetHealthTimeouts;
    /**
     * List of worker nodes to check for health.
     */
    workerNodes?: string[];
}

/**
 * A collection of values returned by getHealth.
 */
export interface GetHealthResult {
    /**
     * The client configuration data
     */
    readonly clientConfiguration: outputs.cluster.GetHealthClientConfiguration;
    /**
     * List of control plane nodes to check for health.
     */
    readonly controlPlaneNodes: string[];
    /**
     * endpoints to use for the health check client. Use at least one control plane endpoint.
     */
    readonly endpoints: string[];
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * Skip Kubernetes component checks, this is useful to check if the nodes has finished booting up and kubelet is running. Default is false.
     */
    readonly skipKubernetesChecks?: boolean;
    readonly timeouts?: outputs.cluster.GetHealthTimeouts;
    /**
     * List of worker nodes to check for health.
     */
    readonly workerNodes?: string[];
}
/**
 * Waits for the Talos cluster to be healthy. Can be used as a dependency before running other operations on the cluster.
 */
export function getHealthOutput(args: GetHealthOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetHealthResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("talos:cluster/getHealth:getHealth", {
        "clientConfiguration": args.clientConfiguration,
        "controlPlaneNodes": args.controlPlaneNodes,
        "endpoints": args.endpoints,
        "skipKubernetesChecks": args.skipKubernetesChecks,
        "timeouts": args.timeouts,
        "workerNodes": args.workerNodes,
    }, opts);
}

/**
 * A collection of arguments for invoking getHealth.
 */
export interface GetHealthOutputArgs {
    /**
     * The client configuration data
     */
    clientConfiguration: pulumi.Input<inputs.cluster.GetHealthClientConfigurationArgs>;
    /**
     * List of control plane nodes to check for health.
     */
    controlPlaneNodes: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * endpoints to use for the health check client. Use at least one control plane endpoint.
     */
    endpoints: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Skip Kubernetes component checks, this is useful to check if the nodes has finished booting up and kubelet is running. Default is false.
     */
    skipKubernetesChecks?: pulumi.Input<boolean>;
    timeouts?: pulumi.Input<inputs.cluster.GetHealthTimeoutsArgs>;
    /**
     * List of worker nodes to check for health.
     */
    workerNodes?: pulumi.Input<pulumi.Input<string>[]>;
}
