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

    /// <summary>
    /// A Machine Secrets Trust daemon info
    /// </summary>
    public sealed class TrustdInfoGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("token", required: true)]
        private Input<string>? _token;

        /// <summary>
        /// The trustd token for the talos kubernetes cluster
        /// </summary>
        public Input<string>? Token
        {
            get => _token;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _token = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public TrustdInfoGetArgs()
        {
        }
        public static new TrustdInfoGetArgs Empty => new TrustdInfoGetArgs();
    }
}