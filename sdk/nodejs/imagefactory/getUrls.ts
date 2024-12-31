// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Generates URLs for different assets supported by the Talos image factory.
 */
export function getUrls(args: GetUrlsArgs, opts?: pulumi.InvokeOptions): Promise<GetUrlsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("talos:imageFactory/getUrls:getUrls", {
        "architecture": args.architecture,
        "platform": args.platform,
        "sbc": args.sbc,
        "schematicId": args.schematicId,
        "talosVersion": args.talosVersion,
    }, opts);
}

/**
 * A collection of arguments for invoking getUrls.
 */
export interface GetUrlsArgs {
    architecture?: string;
    platform?: string;
    sbc?: string;
    schematicId: string;
    talosVersion: string;
}

/**
 * A collection of values returned by getUrls.
 */
export interface GetUrlsResult {
    readonly architecture: string;
    readonly id: string;
    readonly platform?: string;
    readonly sbc?: string;
    readonly schematicId: string;
    readonly talosVersion: string;
    readonly urls: outputs.imageFactory.GetUrlsUrls;
}
/**
 * Generates URLs for different assets supported by the Talos image factory.
 */
export function getUrlsOutput(args: GetUrlsOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetUrlsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("talos:imageFactory/getUrls:getUrls", {
        "architecture": args.architecture,
        "platform": args.platform,
        "sbc": args.sbc,
        "schematicId": args.schematicId,
        "talosVersion": args.talosVersion,
    }, opts);
}

/**
 * A collection of arguments for invoking getUrls.
 */
export interface GetUrlsOutputArgs {
    architecture?: pulumi.Input<string>;
    platform?: pulumi.Input<string>;
    sbc?: pulumi.Input<string>;
    schematicId: pulumi.Input<string>;
    talosVersion: pulumi.Input<string>;
}