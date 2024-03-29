// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Machine.Outputs
{

    /// <summary>
    /// A Machine Secrets Bootstrap data
    /// </summary>
    [OutputType]
    public sealed class KubernetesSecretsResult
    {
        /// <summary>
        /// The aescbc encryption secret for the talos kubernetes cluster
        /// </summary>
        public readonly string? AescbcEncryptionSecret;
        /// <summary>
        /// The bootstrap token for the talos kubernetes cluster
        /// </summary>
        public readonly string BootstrapToken;
        /// <summary>
        /// The secretbox encryption secret for the talos kubernetes cluster
        /// </summary>
        public readonly string SecretboxEncryptionSecret;

        [OutputConstructor]
        private KubernetesSecretsResult(
            string? aescbcEncryptionSecret,

            string bootstrapToken,

            string secretboxEncryptionSecret)
        {
            AescbcEncryptionSecret = aescbcEncryptionSecret;
            BootstrapToken = bootstrapToken;
            SecretboxEncryptionSecret = secretboxEncryptionSecret;
        }
    }
}
