// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Inputs
{

    public sealed class GetImageFactoryExtensionsVersionsFiltersArgs : global::Pulumi.InvokeArgs
    {
        [Input("names")]
        private List<string>? _names;

        /// <summary>
        /// The name of the extension to filter by.
        /// </summary>
        public List<string> Names
        {
            get => _names ?? (_names = new List<string>());
            set => _names = value;
        }

        public GetImageFactoryExtensionsVersionsFiltersArgs()
        {
        }
        public static new GetImageFactoryExtensionsVersionsFiltersArgs Empty => new GetImageFactoryExtensionsVersionsFiltersArgs();
    }
}
