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

    public sealed class DisksTimeoutsInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        /// </summary>
        [Input("read")]
        public Input<string>? Read { get; set; }

        public DisksTimeoutsInputArgs()
        {
        }
        public static new DisksTimeoutsInputArgs Empty => new DisksTimeoutsInputArgs();
    }
}
