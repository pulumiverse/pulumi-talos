// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Cluster
{
    public static class GetHealth
    {
        /// <summary>
        /// Checks the health of a Talos cluster
        /// </summary>
        public static Task<GetHealthResult> InvokeAsync(GetHealthArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetHealthResult>("talos:cluster/getHealth:getHealth", args ?? new GetHealthArgs(), options.WithDefaults());

        /// <summary>
        /// Checks the health of a Talos cluster
        /// </summary>
        public static Output<GetHealthResult> Invoke(GetHealthInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetHealthResult>("talos:cluster/getHealth:getHealth", args ?? new GetHealthInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetHealthArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The client configuration data
        /// </summary>
        [Input("clientConfiguration", required: true)]
        public Inputs.GetHealthClientConfigurationArgs ClientConfiguration { get; set; } = null!;

        [Input("controlPlaneNodes", required: true)]
        private List<string>? _controlPlaneNodes;

        /// <summary>
        /// List of control plane nodes to check for health.
        /// </summary>
        public List<string> ControlPlaneNodes
        {
            get => _controlPlaneNodes ?? (_controlPlaneNodes = new List<string>());
            set => _controlPlaneNodes = value;
        }

        [Input("endpoints", required: true)]
        private List<string>? _endpoints;

        /// <summary>
        /// endpoints to use for the health check client. Use at least one control plane endpoint.
        /// </summary>
        public List<string> Endpoints
        {
            get => _endpoints ?? (_endpoints = new List<string>());
            set => _endpoints = value;
        }

        [Input("timeouts")]
        public Inputs.GetHealthTimeoutsArgs? Timeouts { get; set; }

        [Input("workerNodes")]
        private List<string>? _workerNodes;

        /// <summary>
        /// List of worker nodes to check for health.
        /// </summary>
        public List<string> WorkerNodes
        {
            get => _workerNodes ?? (_workerNodes = new List<string>());
            set => _workerNodes = value;
        }

        public GetHealthArgs()
        {
        }
        public static new GetHealthArgs Empty => new GetHealthArgs();
    }

    public sealed class GetHealthInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The client configuration data
        /// </summary>
        [Input("clientConfiguration", required: true)]
        public Input<Inputs.GetHealthClientConfigurationInputArgs> ClientConfiguration { get; set; } = null!;

        [Input("controlPlaneNodes", required: true)]
        private InputList<string>? _controlPlaneNodes;

        /// <summary>
        /// List of control plane nodes to check for health.
        /// </summary>
        public InputList<string> ControlPlaneNodes
        {
            get => _controlPlaneNodes ?? (_controlPlaneNodes = new InputList<string>());
            set => _controlPlaneNodes = value;
        }

        [Input("endpoints", required: true)]
        private InputList<string>? _endpoints;

        /// <summary>
        /// endpoints to use for the health check client. Use at least one control plane endpoint.
        /// </summary>
        public InputList<string> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<string>());
            set => _endpoints = value;
        }

        [Input("timeouts")]
        public Input<Inputs.GetHealthTimeoutsInputArgs>? Timeouts { get; set; }

        [Input("workerNodes")]
        private InputList<string>? _workerNodes;

        /// <summary>
        /// List of worker nodes to check for health.
        /// </summary>
        public InputList<string> WorkerNodes
        {
            get => _workerNodes ?? (_workerNodes = new InputList<string>());
            set => _workerNodes = value;
        }

        public GetHealthInvokeArgs()
        {
        }
        public static new GetHealthInvokeArgs Empty => new GetHealthInvokeArgs();
    }


    [OutputType]
    public sealed class GetHealthResult
    {
        /// <summary>
        /// The client configuration data
        /// </summary>
        public readonly Outputs.GetHealthClientConfigurationResult ClientConfiguration;
        /// <summary>
        /// List of control plane nodes to check for health.
        /// </summary>
        public readonly ImmutableArray<string> ControlPlaneNodes;
        /// <summary>
        /// endpoints to use for the health check client. Use at least one control plane endpoint.
        /// </summary>
        public readonly ImmutableArray<string> Endpoints;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly string Id;
        public readonly Outputs.GetHealthTimeoutsResult? Timeouts;
        /// <summary>
        /// List of worker nodes to check for health.
        /// </summary>
        public readonly ImmutableArray<string> WorkerNodes;

        [OutputConstructor]
        private GetHealthResult(
            Outputs.GetHealthClientConfigurationResult clientConfiguration,

            ImmutableArray<string> controlPlaneNodes,

            ImmutableArray<string> endpoints,

            string id,

            Outputs.GetHealthTimeoutsResult? timeouts,

            ImmutableArray<string> workerNodes)
        {
            ClientConfiguration = clientConfiguration;
            ControlPlaneNodes = controlPlaneNodes;
            Endpoints = endpoints;
            Id = id;
            Timeouts = timeouts;
            WorkerNodes = workerNodes;
        }
    }
}