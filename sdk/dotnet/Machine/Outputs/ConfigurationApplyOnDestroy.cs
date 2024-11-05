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
    public sealed class ConfigurationApplyOnDestroy
    {
        /// <summary>
        /// Graceful indicates whether node should leave etcd before the upgrade, it also enforces etcd checks before leaving. Default true
        /// </summary>
        public readonly bool? Graceful;
        /// <summary>
        /// Reboot indicates whether node should reboot or halt after resetting. Default false
        /// </summary>
        public readonly bool? Reboot;
        /// <summary>
        /// Reset the machine to the initial state (STATE and EPHEMERAL will be wiped). Default false
        /// </summary>
        public readonly bool? Reset;

        [OutputConstructor]
        private ConfigurationApplyOnDestroy(
            bool? graceful,

            bool? reboot,

            bool? reset)
        {
            Graceful = graceful;
            Reboot = reboot;
            Reset = reset;
        }
    }
}
