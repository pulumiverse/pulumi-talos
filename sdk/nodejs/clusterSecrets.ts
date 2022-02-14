// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "./types";
import * as utilities from "./utilities";

/**
 * Talos secrets resource
 */
export class ClusterSecrets extends pulumi.CustomResource {
    /**
     * Get an existing ClusterSecrets resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ClusterSecrets {
        return new ClusterSecrets(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'talos:index:clusterSecrets';

    /**
     * Returns true if the given object is an instance of ClusterSecrets.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterSecrets {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterSecrets.__pulumiType;
    }

    public readonly configVersion!: pulumi.Output<outputs.TalosMachineConfigVersionOutput>;
    /**
     * Talos Secrets Bundle
     */
    public /*out*/ readonly secrets!: pulumi.Output<outputs.SecretsBundle>;
    /**
     * Talos version the config generated for
     */
    public readonly talosVersion!: pulumi.Output<outputs.TalosVersionOutput>;

    /**
     * Create a ClusterSecrets resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ClusterSecretsArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["configVersion"] = (args ? args.configVersion : undefined) ?? "v1alpha1";
            resourceInputs["talosVersion"] = args ? args.talosVersion : undefined;
            resourceInputs["secrets"] = undefined /*out*/;
        } else {
            resourceInputs["configVersion"] = undefined /*out*/;
            resourceInputs["secrets"] = undefined /*out*/;
            resourceInputs["talosVersion"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ClusterSecrets.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ClusterSecrets resource.
 */
export interface ClusterSecretsArgs {
    /**
     * the desired machine config version to generate (default "v1alpha1")
     */
    configVersion?: pulumi.Input<string | enums.TalosMachineConfigVersion>;
    /**
     * the desired Talos version to generate config for (backwards compatibility, e.g. v0.8)
     */
    talosVersion?: pulumi.Input<string>;
}
