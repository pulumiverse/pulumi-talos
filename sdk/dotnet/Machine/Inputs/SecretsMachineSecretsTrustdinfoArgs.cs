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

    public sealed class SecretsMachineSecretsTrustdinfoArgs : global::Pulumi.ResourceArgs
    {
        [Input("token")]
        private Input<string>? _token;
        public Input<string>? Token
        {
            get => _token;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _token = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public SecretsMachineSecretsTrustdinfoArgs()
        {
        }
        public static new SecretsMachineSecretsTrustdinfoArgs Empty => new SecretsMachineSecretsTrustdinfoArgs();
    }
}