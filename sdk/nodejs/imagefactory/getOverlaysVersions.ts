// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The image factory overlays versions data source provides a list of available overlays for a specific talos version from the image factory.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as talos from "@pulumi/talos";
 *
 * const this = talos.imageFactory.getOverlaysVersions({
 *     talosVersion: "v1.7.5",
 *     filters: {
 *         name: "rock4cplus",
 *     },
 * });
 * ```
 */
export function getOverlaysVersions(args: GetOverlaysVersionsArgs, opts?: pulumi.InvokeOptions): Promise<GetOverlaysVersionsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("talos:imageFactory/getOverlaysVersions:getOverlaysVersions", {
        "filters": args.filters,
        "talosVersion": args.talosVersion,
    }, opts);
}

/**
 * A collection of arguments for invoking getOverlaysVersions.
 */
export interface GetOverlaysVersionsArgs {
    /**
     * The filter to apply to the overlays list.
     */
    filters?: inputs.imageFactory.GetOverlaysVersionsFilters;
    /**
     * The talos version to get overlays for.
     */
    talosVersion: string;
}

/**
 * A collection of values returned by getOverlaysVersions.
 */
export interface GetOverlaysVersionsResult {
    /**
     * The filter to apply to the overlays list.
     */
    readonly filters?: outputs.imageFactory.GetOverlaysVersionsFilters;
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * The list of available extensions for the specified talos version.
     */
    readonly overlaysInfos: outputs.imageFactory.GetOverlaysVersionsOverlaysInfo[];
    /**
     * The talos version to get overlays for.
     */
    readonly talosVersion: string;
}
/**
 * The image factory overlays versions data source provides a list of available overlays for a specific talos version from the image factory.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as talos from "@pulumi/talos";
 *
 * const this = talos.imageFactory.getOverlaysVersions({
 *     talosVersion: "v1.7.5",
 *     filters: {
 *         name: "rock4cplus",
 *     },
 * });
 * ```
 */
export function getOverlaysVersionsOutput(args: GetOverlaysVersionsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetOverlaysVersionsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("talos:imageFactory/getOverlaysVersions:getOverlaysVersions", {
        "filters": args.filters,
        "talosVersion": args.talosVersion,
    }, opts);
}

/**
 * A collection of arguments for invoking getOverlaysVersions.
 */
export interface GetOverlaysVersionsOutputArgs {
    /**
     * The filter to apply to the overlays list.
     */
    filters?: pulumi.Input<inputs.imageFactory.GetOverlaysVersionsFiltersArgs>;
    /**
     * The talos version to get overlays for.
     */
    talosVersion: pulumi.Input<string>;
}
