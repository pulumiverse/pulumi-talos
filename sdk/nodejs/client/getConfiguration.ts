// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Generate client configuration for a Talos cluster
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as talos from "@pulumi/talos";
 * import * as talos from "@pulumiverse/talos";
 *
 * const thisSecrets = new talos.machine.Secrets("thisSecrets", {});
 * const thisConfiguration = talos.client.getConfigurationOutput({
 *     clusterName: "example-cluster",
 *     clientConfiguration: thisSecrets.clientConfiguration,
 *     nodes: ["10.5.0.2"],
 * });
 * ```
 */
export function getConfiguration(args: GetConfigurationArgs, opts?: pulumi.InvokeOptions): Promise<GetConfigurationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("talos:client/getConfiguration:getConfiguration", {
        "clientConfiguration": args.clientConfiguration,
        "clusterName": args.clusterName,
        "endpoints": args.endpoints,
        "nodes": args.nodes,
    }, opts);
}

/**
 * A collection of arguments for invoking getConfiguration.
 */
export interface GetConfigurationArgs {
    /**
     * The client configuration data
     */
    clientConfiguration: inputs.client.GetConfigurationClientConfiguration;
    /**
     * The name of the cluster in the generated config
     */
    clusterName: string;
    /**
     * endpoints to set in the generated config
     */
    endpoints?: string[];
    /**
     * nodes to set in the generated config
     */
    nodes?: string[];
}

/**
 * A collection of values returned by getConfiguration.
 */
export interface GetConfigurationResult {
    /**
     * The client configuration data
     */
    readonly clientConfiguration: outputs.client.GetConfigurationClientConfiguration;
    /**
     * The name of the cluster in the generated config
     */
    readonly clusterName: string;
    /**
     * endpoints to set in the generated config
     */
    readonly endpoints?: string[];
    /**
     * The ID of this resource
     */
    readonly id: string;
    /**
     * nodes to set in the generated config
     */
    readonly nodes?: string[];
    /**
     * The generated client configuration
     */
    readonly talosConfig: string;
}
/**
 * Generate client configuration for a Talos cluster
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as talos from "@pulumi/talos";
 * import * as talos from "@pulumiverse/talos";
 *
 * const thisSecrets = new talos.machine.Secrets("thisSecrets", {});
 * const thisConfiguration = talos.client.getConfigurationOutput({
 *     clusterName: "example-cluster",
 *     clientConfiguration: thisSecrets.clientConfiguration,
 *     nodes: ["10.5.0.2"],
 * });
 * ```
 */
export function getConfigurationOutput(args: GetConfigurationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetConfigurationResult> {
    return pulumi.output(args).apply((a: any) => getConfiguration(a, opts))
}

/**
 * A collection of arguments for invoking getConfiguration.
 */
export interface GetConfigurationOutputArgs {
    /**
     * The client configuration data
     */
    clientConfiguration: pulumi.Input<inputs.client.GetConfigurationClientConfigurationArgs>;
    /**
     * The name of the cluster in the generated config
     */
    clusterName: pulumi.Input<string>;
    /**
     * endpoints to set in the generated config
     */
    endpoints?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * nodes to set in the generated config
     */
    nodes?: pulumi.Input<pulumi.Input<string>[]>;
}