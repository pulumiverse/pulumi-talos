// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Generate machine secrets for Talos cluster.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as talos from "@pulumiverse/talos";
 *
 * const machineSecrets = new talos.machine.Secrets("machine_secrets", {});
 * ```
 *
 * ## Import
 *
 * terraform
 *
 * machine secrets can be imported from an existing secrets file
 *
 * ```sh
 * $ pulumi import talos:machine/secrets:Secrets this <path-to-secrets.yaml>
 * ```
 */
export class Secrets extends pulumi.CustomResource {
    /**
     * Get an existing Secrets resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretsState, opts?: pulumi.CustomResourceOptions): Secrets {
        return new Secrets(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'talos:machine/secrets:Secrets';

    /**
     * Returns true if the given object is an instance of Secrets.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Secrets {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Secrets.__pulumiType;
    }

    /**
     * The generated client configuration data
     */
    public /*out*/ readonly clientConfiguration!: pulumi.Output<outputs.machine.ClientConfiguration>;
    /**
     * The secrets for the talos cluster
     */
    public /*out*/ readonly machineSecrets!: pulumi.Output<outputs.machine.MachineSecrets>;
    /**
     * The version of talos features to use in generated machine configuration
     */
    public readonly talosVersion!: pulumi.Output<string>;

    /**
     * Create a Secrets resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SecretsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecretsArgs | SecretsState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SecretsState | undefined;
            resourceInputs["clientConfiguration"] = state ? state.clientConfiguration : undefined;
            resourceInputs["machineSecrets"] = state ? state.machineSecrets : undefined;
            resourceInputs["talosVersion"] = state ? state.talosVersion : undefined;
        } else {
            const args = argsOrState as SecretsArgs | undefined;
            resourceInputs["talosVersion"] = args ? args.talosVersion : undefined;
            resourceInputs["clientConfiguration"] = undefined /*out*/;
            resourceInputs["machineSecrets"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Secrets.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Secrets resources.
 */
export interface SecretsState {
    /**
     * The generated client configuration data
     */
    clientConfiguration?: pulumi.Input<inputs.machine.ClientConfiguration>;
    /**
     * The secrets for the talos cluster
     */
    machineSecrets?: pulumi.Input<inputs.machine.MachineSecretsArgs>;
    /**
     * The version of talos features to use in generated machine configuration
     */
    talosVersion?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Secrets resource.
 */
export interface SecretsArgs {
    /**
     * The version of talos features to use in generated machine configuration
     */
    talosVersion?: pulumi.Input<string>;
}
