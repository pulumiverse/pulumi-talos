// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Machine.Inputs
{

    public sealed class GetDisksFiltersArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter disks by bus path
        /// </summary>
        [Input("busPath")]
        public string? BusPath { get; set; }

        /// <summary>
        /// Filter disks by modalias
        /// </summary>
        [Input("modalias")]
        public string? Modalias { get; set; }

        /// <summary>
        /// Filter disks by model
        /// </summary>
        [Input("model")]
        public string? Model { get; set; }

        /// <summary>
        /// Filter disks by name
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Filter disks by serial number
        /// </summary>
        [Input("serial")]
        public string? Serial { get; set; }

        /// <summary>
        /// Filter disks by size
        /// </summary>
        [Input("size")]
        public string? Size { get; set; }

        /// <summary>
        /// Filter disks by type
        /// </summary>
        [Input("type")]
        public string? Type { get; set; }

        /// <summary>
        /// Filter disks by uuid
        /// </summary>
        [Input("uuid")]
        public string? Uuid { get; set; }

        /// <summary>
        /// Filter disks by wwid
        /// </summary>
        [Input("wwid")]
        public string? Wwid { get; set; }

        public GetDisksFiltersArgs()
        {
        }
        public static new GetDisksFiltersArgs Empty => new GetDisksFiltersArgs();
    }
}