// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.ImageFactory.Outputs
{

    [OutputType]
    public sealed class GetVersionsFiltersResult
    {
        /// <summary>
        /// If set to true, only stable versions will be returned. If set to false, all versions will be returned.
        /// </summary>
        public readonly bool? StableVersionsOnly;

        [OutputConstructor]
        private GetVersionsFiltersResult(bool? stableVersionsOnly)
        {
            StableVersionsOnly = stableVersionsOnly;
        }
    }
}
