// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.ImageFactory
{
    public static class GetExtensionsVersions
    {
        /// <summary>
        /// The image factory extensions versions data source provides a list of available extensions for a specific talos version from the image factory.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Talos = Pulumi.Talos;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var @this = Talos.ImageFactory.GetExtensionsVersions.Invoke(new()
        ///     {
        ///         TalosVersion = "v1.7.5",
        ///         Filters = new Talos.ImageFactory.Inputs.GetExtensionsVersionsFiltersInputArgs
        ///         {
        ///             Names = new[]
        ///             {
        ///                 "amdgpu",
        ///                 "tailscale",
        ///             },
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetExtensionsVersionsResult> InvokeAsync(GetExtensionsVersionsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetExtensionsVersionsResult>("talos:imageFactory/getExtensionsVersions:getExtensionsVersions", args ?? new GetExtensionsVersionsArgs(), options.WithDefaults());

        /// <summary>
        /// The image factory extensions versions data source provides a list of available extensions for a specific talos version from the image factory.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Talos = Pulumi.Talos;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var @this = Talos.ImageFactory.GetExtensionsVersions.Invoke(new()
        ///     {
        ///         TalosVersion = "v1.7.5",
        ///         Filters = new Talos.ImageFactory.Inputs.GetExtensionsVersionsFiltersInputArgs
        ///         {
        ///             Names = new[]
        ///             {
        ///                 "amdgpu",
        ///                 "tailscale",
        ///             },
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetExtensionsVersionsResult> Invoke(GetExtensionsVersionsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetExtensionsVersionsResult>("talos:imageFactory/getExtensionsVersions:getExtensionsVersions", args ?? new GetExtensionsVersionsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The image factory extensions versions data source provides a list of available extensions for a specific talos version from the image factory.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Talos = Pulumi.Talos;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var @this = Talos.ImageFactory.GetExtensionsVersions.Invoke(new()
        ///     {
        ///         TalosVersion = "v1.7.5",
        ///         Filters = new Talos.ImageFactory.Inputs.GetExtensionsVersionsFiltersInputArgs
        ///         {
        ///             Names = new[]
        ///             {
        ///                 "amdgpu",
        ///                 "tailscale",
        ///             },
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetExtensionsVersionsResult> Invoke(GetExtensionsVersionsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetExtensionsVersionsResult>("talos:imageFactory/getExtensionsVersions:getExtensionsVersions", args ?? new GetExtensionsVersionsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetExtensionsVersionsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The filter to apply to the extensions list.
        /// </summary>
        [Input("filters")]
        public Inputs.GetExtensionsVersionsFiltersArgs? Filters { get; set; }

        /// <summary>
        /// The talos version to get extensions for.
        /// </summary>
        [Input("talosVersion", required: true)]
        public string TalosVersion { get; set; } = null!;

        public GetExtensionsVersionsArgs()
        {
        }
        public static new GetExtensionsVersionsArgs Empty => new GetExtensionsVersionsArgs();
    }

    public sealed class GetExtensionsVersionsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The filter to apply to the extensions list.
        /// </summary>
        [Input("filters")]
        public Input<Inputs.GetExtensionsVersionsFiltersInputArgs>? Filters { get; set; }

        /// <summary>
        /// The talos version to get extensions for.
        /// </summary>
        [Input("talosVersion", required: true)]
        public Input<string> TalosVersion { get; set; } = null!;

        public GetExtensionsVersionsInvokeArgs()
        {
        }
        public static new GetExtensionsVersionsInvokeArgs Empty => new GetExtensionsVersionsInvokeArgs();
    }


    [OutputType]
    public sealed class GetExtensionsVersionsResult
    {
        /// <summary>
        /// The list of available extensions for the specified talos version.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetExtensionsVersionsExtensionsInfoResult> ExtensionsInfos;
        /// <summary>
        /// The filter to apply to the extensions list.
        /// </summary>
        public readonly Outputs.GetExtensionsVersionsFiltersResult? Filters;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The talos version to get extensions for.
        /// </summary>
        public readonly string TalosVersion;

        [OutputConstructor]
        private GetExtensionsVersionsResult(
            ImmutableArray<Outputs.GetExtensionsVersionsExtensionsInfoResult> extensionsInfos,

            Outputs.GetExtensionsVersionsFiltersResult? filters,

            string id,

            string talosVersion)
        {
            ExtensionsInfos = extensionsInfos;
            Filters = filters;
            Id = id;
            TalosVersion = talosVersion;
        }
    }
}