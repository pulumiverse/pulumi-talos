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

    [OutputType]
    public sealed class ConfigurationMachineSecretsCertsResult
    {
        /// <summary>
        /// The certificate and key pair
        /// </summary>
        public readonly Outputs.ConfigurationMachineSecretsCertsEtcdResult Etcd;
        /// <summary>
        /// The certificate and key pair
        /// </summary>
        public readonly Outputs.ConfigurationMachineSecretsCertsK8sResult K8s;
        /// <summary>
        /// The certificate and key pair
        /// </summary>
        public readonly Outputs.ConfigurationMachineSecretsCertsK8sAggregatorResult K8sAggregator;
        public readonly Outputs.ConfigurationMachineSecretsCertsK8sServiceaccountResult K8sServiceaccount;
        /// <summary>
        /// The certificate and key pair
        /// </summary>
        public readonly Outputs.ConfigurationMachineSecretsCertsOsResult Os;

        [OutputConstructor]
        private ConfigurationMachineSecretsCertsResult(
            Outputs.ConfigurationMachineSecretsCertsEtcdResult etcd,

            Outputs.ConfigurationMachineSecretsCertsK8sResult k8s,

            Outputs.ConfigurationMachineSecretsCertsK8sAggregatorResult k8sAggregator,

            Outputs.ConfigurationMachineSecretsCertsK8sServiceaccountResult k8sServiceaccount,

            Outputs.ConfigurationMachineSecretsCertsOsResult os)
        {
            Etcd = etcd;
            K8s = k8s;
            K8sAggregator = k8sAggregator;
            K8sServiceaccount = k8sServiceaccount;
            Os = os;
        }
    }
}
