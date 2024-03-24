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
    /// A Machine Secrets Bootstrap data
    /// </summary>
    public sealed class KubernetesSecretsArgs : global::Pulumi.InvokeArgs
    {
        [Input("aescbc_encryption_secret")]
        private string? _aescbc_encryption_secret;

        /// <summary>
        /// The aescbc encryption secret for the talos kubernetes cluster
        /// </summary>
        public string? Aescbc_encryption_secret
        {
            get => _aescbc_encryption_secret;
            set => _aescbc_encryption_secret = value;
        }

        [Input("bootstrap_token", required: true)]
        private string? _bootstrap_token;

        /// <summary>
        /// The bootstrap token for the talos kubernetes cluster
        /// </summary>
        public string? Bootstrap_token
        {
            get => _bootstrap_token;
            set => _bootstrap_token = value;
        }

        [Input("secretbox_encryption_secret", required: true)]
        private string? _secretbox_encryption_secret;

        /// <summary>
        /// The secretbox encryption secret for the talos kubernetes cluster
        /// </summary>
        public string? Secretbox_encryption_secret
        {
            get => _secretbox_encryption_secret;
            set => _secretbox_encryption_secret = value;
        }

        public KubernetesSecretsArgs()
        {
        }
        public static new KubernetesSecretsArgs Empty => new KubernetesSecretsArgs();
    }
}
