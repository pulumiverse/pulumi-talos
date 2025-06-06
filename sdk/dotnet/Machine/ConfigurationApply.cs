// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Machine
{
    /// <summary>
    /// The machine configuration apply resource allows to apply machine configuration to a node
    /// </summary>
    [TalosResourceType("talos:machine/configurationApply:ConfigurationApply")]
    public partial class ConfigurationApply : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The mode of the apply operation
        /// </summary>
        [Output("applyMode")]
        public Output<string> ApplyMode { get; private set; } = null!;

        /// <summary>
        /// The client configuration data
        /// </summary>
        [Output("clientConfiguration")]
        public Output<Outputs.ClientConfiguration> ClientConfiguration { get; private set; } = null!;

        /// <summary>
        /// The list of config patches to apply
        /// </summary>
        [Output("configPatches")]
        public Output<ImmutableArray<string>> ConfigPatches { get; private set; } = null!;

        /// <summary>
        /// The endpoint of the machine to bootstrap
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// The generated machine configuration after applying patches
        /// </summary>
        [Output("machineConfiguration")]
        public Output<string> MachineConfiguration { get; private set; } = null!;

        /// <summary>
        /// The machine configuration to apply
        /// </summary>
        [Output("machineConfigurationInput")]
        public Output<string> MachineConfigurationInput { get; private set; } = null!;

        /// <summary>
        /// The name of the node to bootstrap
        /// </summary>
        [Output("node")]
        public Output<string> Node { get; private set; } = null!;

        /// <summary>
        /// Actions to be taken on destroy, if *reset* is not set this is a no-op.
        /// </summary>
        [Output("onDestroy")]
        public Output<Outputs.ConfigurationApplyOnDestroy?> OnDestroy { get; private set; } = null!;

        [Output("timeouts")]
        public Output<Outputs.Timeout?> Timeouts { get; private set; } = null!;


        /// <summary>
        /// Create a ConfigurationApply resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConfigurationApply(string name, ConfigurationApplyArgs args, CustomResourceOptions? options = null)
            : base("talos:machine/configurationApply:ConfigurationApply", name, args ?? new ConfigurationApplyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConfigurationApply(string name, Input<string> id, ConfigurationApplyState? state = null, CustomResourceOptions? options = null)
            : base("talos:machine/configurationApply:ConfigurationApply", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "machineConfiguration",
                    "machineConfigurationInput",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ConfigurationApply resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConfigurationApply Get(string name, Input<string> id, ConfigurationApplyState? state = null, CustomResourceOptions? options = null)
        {
            return new ConfigurationApply(name, id, state, options);
        }
    }

    public sealed class ConfigurationApplyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The mode of the apply operation
        /// </summary>
        [Input("applyMode")]
        public Input<string>? ApplyMode { get; set; }

        /// <summary>
        /// The client configuration data
        /// </summary>
        [Input("clientConfiguration", required: true)]
        public Input<Inputs.ClientConfigurationArgs> ClientConfiguration { get; set; } = null!;

        [Input("configPatches")]
        private InputList<string>? _configPatches;

        /// <summary>
        /// The list of config patches to apply
        /// </summary>
        public InputList<string> ConfigPatches
        {
            get => _configPatches ?? (_configPatches = new InputList<string>());
            set => _configPatches = value;
        }

        /// <summary>
        /// The endpoint of the machine to bootstrap
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        [Input("machineConfigurationInput", required: true)]
        private Input<string>? _machineConfigurationInput;

        /// <summary>
        /// The machine configuration to apply
        /// </summary>
        public Input<string>? MachineConfigurationInput
        {
            get => _machineConfigurationInput;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _machineConfigurationInput = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The name of the node to bootstrap
        /// </summary>
        [Input("node", required: true)]
        public Input<string> Node { get; set; } = null!;

        /// <summary>
        /// Actions to be taken on destroy, if *reset* is not set this is a no-op.
        /// </summary>
        [Input("onDestroy")]
        public Input<Inputs.ConfigurationApplyOnDestroyArgs>? OnDestroy { get; set; }

        [Input("timeouts")]
        public Input<Inputs.TimeoutArgs>? Timeouts { get; set; }

        public ConfigurationApplyArgs()
        {
        }
        public static new ConfigurationApplyArgs Empty => new ConfigurationApplyArgs();
    }

    public sealed class ConfigurationApplyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The mode of the apply operation
        /// </summary>
        [Input("applyMode")]
        public Input<string>? ApplyMode { get; set; }

        /// <summary>
        /// The client configuration data
        /// </summary>
        [Input("clientConfiguration")]
        public Input<Inputs.ClientConfigurationGetArgs>? ClientConfiguration { get; set; }

        [Input("configPatches")]
        private InputList<string>? _configPatches;

        /// <summary>
        /// The list of config patches to apply
        /// </summary>
        public InputList<string> ConfigPatches
        {
            get => _configPatches ?? (_configPatches = new InputList<string>());
            set => _configPatches = value;
        }

        /// <summary>
        /// The endpoint of the machine to bootstrap
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        [Input("machineConfiguration")]
        private Input<string>? _machineConfiguration;

        /// <summary>
        /// The generated machine configuration after applying patches
        /// </summary>
        public Input<string>? MachineConfiguration
        {
            get => _machineConfiguration;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _machineConfiguration = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("machineConfigurationInput")]
        private Input<string>? _machineConfigurationInput;

        /// <summary>
        /// The machine configuration to apply
        /// </summary>
        public Input<string>? MachineConfigurationInput
        {
            get => _machineConfigurationInput;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _machineConfigurationInput = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The name of the node to bootstrap
        /// </summary>
        [Input("node")]
        public Input<string>? Node { get; set; }

        /// <summary>
        /// Actions to be taken on destroy, if *reset* is not set this is a no-op.
        /// </summary>
        [Input("onDestroy")]
        public Input<Inputs.ConfigurationApplyOnDestroyGetArgs>? OnDestroy { get; set; }

        [Input("timeouts")]
        public Input<Inputs.TimeoutGetArgs>? Timeouts { get; set; }

        public ConfigurationApplyState()
        {
        }
        public static new ConfigurationApplyState Empty => new ConfigurationApplyState();
    }
}
