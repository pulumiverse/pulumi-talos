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
    /// A complete Machine Secrets Certificates configuration
    /// </summary>
    public sealed class CertificatesInputArgs : global::Pulumi.ResourceArgs
    {
        [Input("etcd", required: true)]
        public Input<Inputs.CertificateInputArgs> Etcd { get; set; } = null!;

        [Input("k8s", required: true)]
        public Input<Inputs.CertificateInputArgs> K8s { get; set; } = null!;

        [Input("k8s_aggregator", required: true)]
        public Input<Inputs.CertificateInputArgs> K8s_aggregator { get; set; } = null!;

        [Input("k8s_serviceaccount", required: true)]
        public Input<Inputs.KeyInputArgs> K8s_serviceaccount { get; set; } = null!;

        [Input("os", required: true)]
        public Input<Inputs.CertificateInputArgs> Os { get; set; } = null!;

        public CertificatesInputArgs()
        {
        }
        public static new CertificatesInputArgs Empty => new CertificatesInputArgs();
    }
}