// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The image factory schematic resource allows you to create a schematic for a Talos image.
 */
export class ImageFactorySchematic extends pulumi.CustomResource {
    /**
     * Get an existing ImageFactorySchematic resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageFactorySchematicState, opts?: pulumi.CustomResourceOptions): ImageFactorySchematic {
        return new ImageFactorySchematic(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'talos:index/imageFactorySchematic:ImageFactorySchematic';

    /**
     * Returns true if the given object is an instance of ImageFactorySchematic.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ImageFactorySchematic {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ImageFactorySchematic.__pulumiType;
    }

    /**
     * The schematic yaml respresentation to generate the image.
     */
    public readonly schematic!: pulumi.Output<string | undefined>;

    /**
     * Create a ImageFactorySchematic resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ImageFactorySchematicArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ImageFactorySchematicArgs | ImageFactorySchematicState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ImageFactorySchematicState | undefined;
            resourceInputs["schematic"] = state ? state.schematic : undefined;
        } else {
            const args = argsOrState as ImageFactorySchematicArgs | undefined;
            resourceInputs["schematic"] = args ? args.schematic : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ImageFactorySchematic.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ImageFactorySchematic resources.
 */
export interface ImageFactorySchematicState {
    /**
     * The schematic yaml respresentation to generate the image.
     */
    schematic?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ImageFactorySchematic resource.
 */
export interface ImageFactorySchematicArgs {
    /**
     * The schematic yaml respresentation to generate the image.
     */
    schematic?: pulumi.Input<string>;
}
