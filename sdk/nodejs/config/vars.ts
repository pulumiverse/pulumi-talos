// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("talos");

/**
 * The URL of Image Factory to generate schematics. If not set defaults to https://factory.talos.dev.
 */
export declare const imageFactoryUrl: string | undefined;
Object.defineProperty(exports, "imageFactoryUrl", {
    get() {
        return __config.get("imageFactoryUrl");
    },
    enumerable: true,
});
