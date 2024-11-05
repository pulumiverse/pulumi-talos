# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BootstrapArgs', 'Bootstrap']

@pulumi.input_type
class BootstrapArgs:
    def __init__(__self__, *,
                 client_configuration: pulumi.Input['ClientConfigurationArgs'],
                 node: pulumi.Input[str],
                 endpoint: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['BootstrapTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a Bootstrap resource.
        :param pulumi.Input['ClientConfigurationArgs'] client_configuration: The client configuration data
        :param pulumi.Input[str] node: The name of the node to bootstrap
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        """
        pulumi.set(__self__, "client_configuration", client_configuration)
        pulumi.set(__self__, "node", node)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> pulumi.Input['ClientConfigurationArgs']:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @client_configuration.setter
    def client_configuration(self, value: pulumi.Input['ClientConfigurationArgs']):
        pulumi.set(self, "client_configuration", value)

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
    def timeouts(self) -> Optional[pulumi.Input['BootstrapTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['BootstrapTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _BootstrapState:
    def __init__(__self__, *,
                 client_configuration: Optional[pulumi.Input['ClientConfigurationArgs']] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['BootstrapTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering Bootstrap resources.
        :param pulumi.Input['ClientConfigurationArgs'] client_configuration: The client configuration data
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        :param pulumi.Input[str] node: The name of the node to bootstrap
        """
        if client_configuration is not None:
            pulumi.set(__self__, "client_configuration", client_configuration)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if node is not None:
            pulumi.set(__self__, "node", node)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> Optional[pulumi.Input['ClientConfigurationArgs']]:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @client_configuration.setter
    def client_configuration(self, value: Optional[pulumi.Input['ClientConfigurationArgs']]):
        pulumi.set(self, "client_configuration", value)

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
    def timeouts(self) -> Optional[pulumi.Input['BootstrapTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['BootstrapTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class Bootstrap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_configuration: Optional[pulumi.Input[Union['ClientConfigurationArgs', 'ClientConfigurationArgsDict']]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['BootstrapTimeoutsArgs', 'BootstrapTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        The machine bootstrap resource allows you to bootstrap a Talos node.

        ## Import

        terraform

        machine bootstrap can be imported to let terraform know that the machine is already bootstrapped

        ```sh
        $ pulumi import talos:machine/bootstrap:Bootstrap this <any id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ClientConfigurationArgs', 'ClientConfigurationArgsDict']] client_configuration: The client configuration data
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        :param pulumi.Input[str] node: The name of the node to bootstrap
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BootstrapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The machine bootstrap resource allows you to bootstrap a Talos node.

        ## Import

        terraform

        machine bootstrap can be imported to let terraform know that the machine is already bootstrapped

        ```sh
        $ pulumi import talos:machine/bootstrap:Bootstrap this <any id>
        ```

        :param str resource_name: The name of the resource.
        :param BootstrapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BootstrapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_configuration: Optional[pulumi.Input[Union['ClientConfigurationArgs', 'ClientConfigurationArgsDict']]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['BootstrapTimeoutsArgs', 'BootstrapTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BootstrapArgs.__new__(BootstrapArgs)

            if client_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'client_configuration'")
            __props__.__dict__["client_configuration"] = client_configuration
            __props__.__dict__["endpoint"] = endpoint
            if node is None and not opts.urn:
                raise TypeError("Missing required property 'node'")
            __props__.__dict__["node"] = node
            __props__.__dict__["timeouts"] = timeouts
        super(Bootstrap, __self__).__init__(
            'talos:machine/bootstrap:Bootstrap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_configuration: Optional[pulumi.Input[Union['ClientConfigurationArgs', 'ClientConfigurationArgsDict']]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            node: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['BootstrapTimeoutsArgs', 'BootstrapTimeoutsArgsDict']]] = None) -> 'Bootstrap':
        """
        Get an existing Bootstrap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ClientConfigurationArgs', 'ClientConfigurationArgsDict']] client_configuration: The client configuration data
        :param pulumi.Input[str] endpoint: The endpoint of the machine to bootstrap
        :param pulumi.Input[str] node: The name of the node to bootstrap
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BootstrapState.__new__(_BootstrapState)

        __props__.__dict__["client_configuration"] = client_configuration
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["node"] = node
        __props__.__dict__["timeouts"] = timeouts
        return Bootstrap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> pulumi.Output['outputs.ClientConfiguration']:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint of the machine to bootstrap
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def node(self) -> pulumi.Output[str]:
        """
        The name of the node to bootstrap
        """
        return pulumi.get(self, "node")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.BootstrapTimeouts']]:
        return pulumi.get(self, "timeouts")

