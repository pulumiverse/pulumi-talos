# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ConfigurationApplyArgs', 'ConfigurationApply']

@pulumi.input_type
class ConfigurationApplyArgs:
    def __init__(__self__, *,
                 client_configuration: pulumi.Input['ConfigurationApplyClientConfigurationArgs'],
                 machine_configuration_input: pulumi.Input[str],
                 node: pulumi.Input[str],
                 apply_mode: Optional[pulumi.Input[str]] = None,
                 config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['TimeoutArgs']] = None):
        """
        The set of arguments for constructing a ConfigurationApply resource.
        :param pulumi.Input['ConfigurationApplyClientConfigurationArgs'] client_configuration: The client configuration data
        :param pulumi.Input[str] machine_configuration_input: The machine configuration to apply
        :param pulumi.Input[str] node: The name of the node to bootstrap
        :param pulumi.Input[str] apply_mode: The mode of the apply operation
        :param pulumi.Input[Sequence[pulumi.Input[str]]] config_patches: The list of config patches to apply
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        """
        ConfigurationApplyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            client_configuration=client_configuration,
            machine_configuration_input=machine_configuration_input,
            node=node,
            apply_mode=apply_mode,
            config_patches=config_patches,
            endpoint=endpoint,
            timeouts=timeouts,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             client_configuration: pulumi.Input['ConfigurationApplyClientConfigurationArgs'],
             machine_configuration_input: pulumi.Input[str],
             node: pulumi.Input[str],
             apply_mode: Optional[pulumi.Input[str]] = None,
             config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             endpoint: Optional[pulumi.Input[str]] = None,
             timeouts: Optional[pulumi.Input['TimeoutArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("client_configuration", client_configuration)
        _setter("machine_configuration_input", machine_configuration_input)
        _setter("node", node)
        if apply_mode is not None:
            _setter("apply_mode", apply_mode)
        if config_patches is not None:
            _setter("config_patches", config_patches)
        if endpoint is not None:
            _setter("endpoint", endpoint)
        if timeouts is not None:
            _setter("timeouts", timeouts)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> pulumi.Input['ConfigurationApplyClientConfigurationArgs']:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @client_configuration.setter
    def client_configuration(self, value: pulumi.Input['ConfigurationApplyClientConfigurationArgs']):
        pulumi.set(self, "client_configuration", value)

    @property
    @pulumi.getter(name="machineConfigurationInput")
    def machine_configuration_input(self) -> pulumi.Input[str]:
        """
        The machine configuration to apply
        """
        return pulumi.get(self, "machine_configuration_input")

    @machine_configuration_input.setter
    def machine_configuration_input(self, value: pulumi.Input[str]):
        pulumi.set(self, "machine_configuration_input", value)

    @property
    @pulumi.getter
    def node(self) -> pulumi.Input[str]:
        """
        The name of the node to bootstrap
        """
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: pulumi.Input[str]):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter(name="applyMode")
    def apply_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the apply operation
        """
        return pulumi.get(self, "apply_mode")

    @apply_mode.setter
    def apply_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "apply_mode", value)

    @property
    @pulumi.getter(name="configPatches")
    def config_patches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of config patches to apply
        """
        return pulumi.get(self, "config_patches")

    @config_patches.setter
    def config_patches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "config_patches", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint of the machine to bootstrap
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['TimeoutArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['TimeoutArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _ConfigurationApplyState:
    def __init__(__self__, *,
                 apply_mode: Optional[pulumi.Input[str]] = None,
                 client_configuration: Optional[pulumi.Input['ConfigurationApplyClientConfigurationArgs']] = None,
                 config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 machine_configuration: Optional[pulumi.Input[str]] = None,
                 machine_configuration_input: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['TimeoutArgs']] = None):
        """
        Input properties used for looking up and filtering ConfigurationApply resources.
        :param pulumi.Input[str] apply_mode: The mode of the apply operation
        :param pulumi.Input['ConfigurationApplyClientConfigurationArgs'] client_configuration: The client configuration data
        :param pulumi.Input[Sequence[pulumi.Input[str]]] config_patches: The list of config patches to apply
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        :param pulumi.Input[str] machine_configuration: The generated machine configuration after applying patches
        :param pulumi.Input[str] machine_configuration_input: The machine configuration to apply
        :param pulumi.Input[str] node: The name of the node to bootstrap
        """
        _ConfigurationApplyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            apply_mode=apply_mode,
            client_configuration=client_configuration,
            config_patches=config_patches,
            endpoint=endpoint,
            machine_configuration=machine_configuration,
            machine_configuration_input=machine_configuration_input,
            node=node,
            timeouts=timeouts,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             apply_mode: Optional[pulumi.Input[str]] = None,
             client_configuration: Optional[pulumi.Input['ConfigurationApplyClientConfigurationArgs']] = None,
             config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             endpoint: Optional[pulumi.Input[str]] = None,
             machine_configuration: Optional[pulumi.Input[str]] = None,
             machine_configuration_input: Optional[pulumi.Input[str]] = None,
             node: Optional[pulumi.Input[str]] = None,
             timeouts: Optional[pulumi.Input['TimeoutArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if apply_mode is not None:
            _setter("apply_mode", apply_mode)
        if client_configuration is not None:
            _setter("client_configuration", client_configuration)
        if config_patches is not None:
            _setter("config_patches", config_patches)
        if endpoint is not None:
            _setter("endpoint", endpoint)
        if machine_configuration is not None:
            _setter("machine_configuration", machine_configuration)
        if machine_configuration_input is not None:
            _setter("machine_configuration_input", machine_configuration_input)
        if node is not None:
            _setter("node", node)
        if timeouts is not None:
            _setter("timeouts", timeouts)

    @property
    @pulumi.getter(name="applyMode")
    def apply_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The mode of the apply operation
        """
        return pulumi.get(self, "apply_mode")

    @apply_mode.setter
    def apply_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "apply_mode", value)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> Optional[pulumi.Input['ConfigurationApplyClientConfigurationArgs']]:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @client_configuration.setter
    def client_configuration(self, value: Optional[pulumi.Input['ConfigurationApplyClientConfigurationArgs']]):
        pulumi.set(self, "client_configuration", value)

    @property
    @pulumi.getter(name="configPatches")
    def config_patches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of config patches to apply
        """
        return pulumi.get(self, "config_patches")

    @config_patches.setter
    def config_patches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "config_patches", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint of the machine to bootstrap
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="machineConfiguration")
    def machine_configuration(self) -> Optional[pulumi.Input[str]]:
        """
        The generated machine configuration after applying patches
        """
        return pulumi.get(self, "machine_configuration")

    @machine_configuration.setter
    def machine_configuration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "machine_configuration", value)

    @property
    @pulumi.getter(name="machineConfigurationInput")
    def machine_configuration_input(self) -> Optional[pulumi.Input[str]]:
        """
        The machine configuration to apply
        """
        return pulumi.get(self, "machine_configuration_input")

    @machine_configuration_input.setter
    def machine_configuration_input(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "machine_configuration_input", value)

    @property
    @pulumi.getter
    def node(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the node to bootstrap
        """
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['TimeoutArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['TimeoutArgs']]):
        pulumi.set(self, "timeouts", value)


class ConfigurationApply(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_mode: Optional[pulumi.Input[str]] = None,
                 client_configuration: Optional[pulumi.Input[pulumi.InputType['ConfigurationApplyClientConfigurationArgs']]] = None,
                 config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 machine_configuration_input: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[pulumi.InputType['TimeoutArgs']]] = None,
                 __props__=None):
        """
        The machine configuration apply resource allows to apply machine configuration to a node

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] apply_mode: The mode of the apply operation
        :param pulumi.Input[pulumi.InputType['ConfigurationApplyClientConfigurationArgs']] client_configuration: The client configuration data
        :param pulumi.Input[Sequence[pulumi.Input[str]]] config_patches: The list of config patches to apply
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        :param pulumi.Input[str] machine_configuration_input: The machine configuration to apply
        :param pulumi.Input[str] node: The name of the node to bootstrap
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationApplyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The machine configuration apply resource allows to apply machine configuration to a node

        :param str resource_name: The name of the resource.
        :param ConfigurationApplyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationApplyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ConfigurationApplyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apply_mode: Optional[pulumi.Input[str]] = None,
                 client_configuration: Optional[pulumi.Input[pulumi.InputType['ConfigurationApplyClientConfigurationArgs']]] = None,
                 config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 machine_configuration_input: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[pulumi.InputType['TimeoutArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationApplyArgs.__new__(ConfigurationApplyArgs)

            __props__.__dict__["apply_mode"] = apply_mode
            if client_configuration is not None and not isinstance(client_configuration, ConfigurationApplyClientConfigurationArgs):
                client_configuration = client_configuration or {}
                def _setter(key, value):
                    client_configuration[key] = value
                ConfigurationApplyClientConfigurationArgs._configure(_setter, **client_configuration)
            if client_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'client_configuration'")
            __props__.__dict__["client_configuration"] = client_configuration
            __props__.__dict__["config_patches"] = config_patches
            __props__.__dict__["endpoint"] = endpoint
            if machine_configuration_input is None and not opts.urn:
                raise TypeError("Missing required property 'machine_configuration_input'")
            __props__.__dict__["machine_configuration_input"] = None if machine_configuration_input is None else pulumi.Output.secret(machine_configuration_input)
            if node is None and not opts.urn:
                raise TypeError("Missing required property 'node'")
            __props__.__dict__["node"] = node
            if timeouts is not None and not isinstance(timeouts, TimeoutArgs):
                timeouts = timeouts or {}
                def _setter(key, value):
                    timeouts[key] = value
                TimeoutArgs._configure(_setter, **timeouts)
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["machine_configuration"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["machineConfiguration", "machineConfigurationInput"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ConfigurationApply, __self__).__init__(
            'talos:machine/configurationApply:ConfigurationApply',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            apply_mode: Optional[pulumi.Input[str]] = None,
            client_configuration: Optional[pulumi.Input[pulumi.InputType['ConfigurationApplyClientConfigurationArgs']]] = None,
            config_patches: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            machine_configuration: Optional[pulumi.Input[str]] = None,
            machine_configuration_input: Optional[pulumi.Input[str]] = None,
            node: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[pulumi.InputType['TimeoutArgs']]] = None) -> 'ConfigurationApply':
        """
        Get an existing ConfigurationApply resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] apply_mode: The mode of the apply operation
        :param pulumi.Input[pulumi.InputType['ConfigurationApplyClientConfigurationArgs']] client_configuration: The client configuration data
        :param pulumi.Input[Sequence[pulumi.Input[str]]] config_patches: The list of config patches to apply
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        :param pulumi.Input[str] machine_configuration: The generated machine configuration after applying patches
        :param pulumi.Input[str] machine_configuration_input: The machine configuration to apply
        :param pulumi.Input[str] node: The name of the node to bootstrap
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConfigurationApplyState.__new__(_ConfigurationApplyState)

        __props__.__dict__["apply_mode"] = apply_mode
        __props__.__dict__["client_configuration"] = client_configuration
        __props__.__dict__["config_patches"] = config_patches
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["machine_configuration"] = machine_configuration
        __props__.__dict__["machine_configuration_input"] = machine_configuration_input
        __props__.__dict__["node"] = node
        __props__.__dict__["timeouts"] = timeouts
        return ConfigurationApply(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applyMode")
    def apply_mode(self) -> pulumi.Output[str]:
        """
        The mode of the apply operation
        """
        return pulumi.get(self, "apply_mode")

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> pulumi.Output['outputs.ConfigurationApplyClientConfiguration']:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @property
    @pulumi.getter(name="configPatches")
    def config_patches(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of config patches to apply
        """
        return pulumi.get(self, "config_patches")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint of the machine to bootstrap
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="machineConfiguration")
    def machine_configuration(self) -> pulumi.Output[str]:
        """
        The generated machine configuration after applying patches
        """
        return pulumi.get(self, "machine_configuration")

    @property
    @pulumi.getter(name="machineConfigurationInput")
    def machine_configuration_input(self) -> pulumi.Output[str]:
        """
        The machine configuration to apply
        """
        return pulumi.get(self, "machine_configuration_input")

    @property
    @pulumi.getter
    def node(self) -> pulumi.Output[str]:
        """
        The name of the node to bootstrap
        """
        return pulumi.get(self, "node")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.Timeout']]:
        return pulumi.get(self, "timeouts")

