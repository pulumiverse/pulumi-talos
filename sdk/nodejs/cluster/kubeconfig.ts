// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Retrieves the kubeconfig for a Talos cluster
 */
export class Kubeconfig extends pulumi.CustomResource {
    /**
     * Get an existing Kubeconfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KubeconfigState, opts?: pulumi.CustomResourceOptions): Kubeconfig {
        return new Kubeconfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'talos:cluster/kubeconfig:Kubeconfig';

    /**
     * Returns true if the given object is an instance of Kubeconfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Kubeconfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Kubeconfig.__pulumiType;
    }

    /**
     * The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
     */
    public readonly certificateRenewalDuration!: pulumi.Output<string>;
    /**
     * The client configuration data
     */
    public readonly clientConfiguration!: pulumi.Output<outputs.cluster.KubeconfigClientConfiguration>;
    /**
     * endpoint to use for the talosclient. If not set, the node value will be used
     */
    public readonly endpoint!: pulumi.Output<string>;
    /**
     * The raw kubeconfig
     */
    public /*out*/ readonly kubeconfigRaw!: pulumi.Output<string>;
    /**
     * The kubernetes client configuration
     */
    public /*out*/ readonly kubernetesClientConfiguration!: pulumi.Output<outputs.cluster.KubeconfigKubernetesClientConfiguration>;
    /**
     * controlplane node to retrieve the kubeconfig from
     */
    public readonly node!: pulumi.Output<string>;
    public readonly timeouts!: pulumi.Output<outputs.cluster.KubeconfigTimeouts | undefined>;

    /**
     * Create a Kubeconfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KubeconfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KubeconfigArgs | KubeconfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KubeconfigState | undefined;
            resourceInputs["certificateRenewalDuration"] = state ? state.certificateRenewalDuration : undefined;
            resourceInputs["clientConfiguration"] = state ? state.clientConfiguration : undefined;
            resourceInputs["endpoint"] = state ? state.endpoint : undefined;
            resourceInputs["kubeconfigRaw"] = state ? state.kubeconfigRaw : undefined;
            resourceInputs["kubernetesClientConfiguration"] = state ? state.kubernetesClientConfiguration : undefined;
            resourceInputs["node"] = state ? state.node : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
        } else {
            const args = argsOrState as KubeconfigArgs | undefined;
            if ((!args || args.clientConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clientConfiguration'");
            }
            if ((!args || args.node === undefined) && !opts.urn) {
                throw new Error("Missing required property 'node'");
            }
            resourceInputs["certificateRenewalDuration"] = args ? args.certificateRenewalDuration : undefined;
            resourceInputs["clientConfiguration"] = args ? args.clientConfiguration : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
            resourceInputs["node"] = args ? args.node : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["kubeconfigRaw"] = undefined /*out*/;
            resourceInputs["kubernetesClientConfiguration"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["kubeconfigRaw"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Kubeconfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Kubeconfig resources.
 */
export interface KubeconfigState {
    /**
     * The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
     */
    certificateRenewalDuration?: pulumi.Input<string>;
    /**
     * The client configuration data
     */
    clientConfiguration?: pulumi.Input<inputs.cluster.KubeconfigClientConfiguration>;
    /**
     * endpoint to use for the talosclient. If not set, the node value will be used
     */
    endpoint?: pulumi.Input<string>;
    /**
     * The raw kubeconfig
     */
    kubeconfigRaw?: pulumi.Input<string>;
    /**
     * The kubernetes client configuration
     */
    kubernetesClientConfiguration?: pulumi.Input<inputs.cluster.KubeconfigKubernetesClientConfiguration>;
    /**
     * controlplane node to retrieve the kubeconfig from
     */
    node?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.cluster.KubeconfigTimeouts>;
}

/**
 * The set of arguments for constructing a Kubeconfig resource.
 */
export interface KubeconfigArgs {
    /**
     * The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
     */
    certificateRenewalDuration?: pulumi.Input<string>;
    /**
     * The client configuration data
     */
    clientConfiguration: pulumi.Input<inputs.cluster.KubeconfigClientConfiguration>;
    /**
     * endpoint to use for the talosclient. If not set, the node value will be used
     */
    endpoint?: pulumi.Input<string>;
    /**
     * controlplane node to retrieve the kubeconfig from
     */
    node: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.cluster.KubeconfigTimeouts>;
}
