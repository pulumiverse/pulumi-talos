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

__all__ = ['KubeconfigArgs', 'Kubeconfig']

@pulumi.input_type
class KubeconfigArgs:
    def __init__(__self__, *,
                 client_configuration: pulumi.Input['KubeconfigClientConfigurationArgs'],
                 node: pulumi.Input[str],
                 certificate_renewal_duration: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['KubeconfigTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a Kubeconfig resource.
        :param pulumi.Input['KubeconfigClientConfigurationArgs'] client_configuration: The client configuration data
        :param pulumi.Input[str] node: controlplane node to retrieve the kubeconfig from
        :param pulumi.Input[str] certificate_renewal_duration: The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        :param pulumi.Input[str] endpoint: endpoint to use for the talosclient. If not set, the node value will be used
        """
        pulumi.set(__self__, "client_configuration", client_configuration)
        pulumi.set(__self__, "node", node)
        if certificate_renewal_duration is not None:
            pulumi.set(__self__, "certificate_renewal_duration", certificate_renewal_duration)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> pulumi.Input['KubeconfigClientConfigurationArgs']:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @client_configuration.setter
    def client_configuration(self, value: pulumi.Input['KubeconfigClientConfigurationArgs']):
        pulumi.set(self, "client_configuration", value)

    @property
    @pulumi.getter
    def node(self) -> pulumi.Input[str]:
        """
        controlplane node to retrieve the kubeconfig from
        """
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: pulumi.Input[str]):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter(name="certificateRenewalDuration")
    def certificate_renewal_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        """
        return pulumi.get(self, "certificate_renewal_duration")

    @certificate_renewal_duration.setter
    def certificate_renewal_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_renewal_duration", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        endpoint to use for the talosclient. If not set, the node value will be used
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['KubeconfigTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['KubeconfigTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _KubeconfigState:
    def __init__(__self__, *,
                 certificate_renewal_duration: Optional[pulumi.Input[str]] = None,
                 client_configuration: Optional[pulumi.Input['KubeconfigClientConfigurationArgs']] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 kubeconfig_raw: Optional[pulumi.Input[str]] = None,
                 kubernetes_client_configuration: Optional[pulumi.Input['KubeconfigKubernetesClientConfigurationArgs']] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['KubeconfigTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering Kubeconfig resources.
        :param pulumi.Input[str] certificate_renewal_duration: The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        :param pulumi.Input['KubeconfigClientConfigurationArgs'] client_configuration: The client configuration data
        :param pulumi.Input[str] endpoint: endpoint to use for the talosclient. If not set, the node value will be used
        :param pulumi.Input[str] kubeconfig_raw: The raw kubeconfig
        :param pulumi.Input['KubeconfigKubernetesClientConfigurationArgs'] kubernetes_client_configuration: The kubernetes client configuration
        :param pulumi.Input[str] node: controlplane node to retrieve the kubeconfig from
        """
        if certificate_renewal_duration is not None:
            pulumi.set(__self__, "certificate_renewal_duration", certificate_renewal_duration)
        if client_configuration is not None:
            pulumi.set(__self__, "client_configuration", client_configuration)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if kubeconfig_raw is not None:
            pulumi.set(__self__, "kubeconfig_raw", kubeconfig_raw)
        if kubernetes_client_configuration is not None:
            pulumi.set(__self__, "kubernetes_client_configuration", kubernetes_client_configuration)
        if node is not None:
            pulumi.set(__self__, "node", node)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="certificateRenewalDuration")
    def certificate_renewal_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        """
        return pulumi.get(self, "certificate_renewal_duration")

    @certificate_renewal_duration.setter
    def certificate_renewal_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_renewal_duration", value)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> Optional[pulumi.Input['KubeconfigClientConfigurationArgs']]:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @client_configuration.setter
    def client_configuration(self, value: Optional[pulumi.Input['KubeconfigClientConfigurationArgs']]):
        pulumi.set(self, "client_configuration", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        endpoint to use for the talosclient. If not set, the node value will be used
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="kubeconfigRaw")
    def kubeconfig_raw(self) -> Optional[pulumi.Input[str]]:
        """
        The raw kubeconfig
        """
        return pulumi.get(self, "kubeconfig_raw")

    @kubeconfig_raw.setter
    def kubeconfig_raw(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig_raw", value)

    @property
    @pulumi.getter(name="kubernetesClientConfiguration")
    def kubernetes_client_configuration(self) -> Optional[pulumi.Input['KubeconfigKubernetesClientConfigurationArgs']]:
        """
        The kubernetes client configuration
        """
        return pulumi.get(self, "kubernetes_client_configuration")

    @kubernetes_client_configuration.setter
    def kubernetes_client_configuration(self, value: Optional[pulumi.Input['KubeconfigKubernetesClientConfigurationArgs']]):
        pulumi.set(self, "kubernetes_client_configuration", value)

    @property
    @pulumi.getter
    def node(self) -> Optional[pulumi.Input[str]]:
        """
        controlplane node to retrieve the kubeconfig from
        """
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['KubeconfigTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['KubeconfigTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class Kubeconfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_renewal_duration: Optional[pulumi.Input[str]] = None,
                 client_configuration: Optional[pulumi.Input[Union['KubeconfigClientConfigurationArgs', 'KubeconfigClientConfigurationArgsDict']]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['KubeconfigTimeoutsArgs', 'KubeconfigTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Retrieves the kubeconfig for a Talos cluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_renewal_duration: The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        :param pulumi.Input[Union['KubeconfigClientConfigurationArgs', 'KubeconfigClientConfigurationArgsDict']] client_configuration: The client configuration data
        :param pulumi.Input[str] endpoint: endpoint to use for the talosclient. If not set, the node value will be used
        :param pulumi.Input[str] node: controlplane node to retrieve the kubeconfig from
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KubeconfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Retrieves the kubeconfig for a Talos cluster

        :param str resource_name: The name of the resource.
        :param KubeconfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KubeconfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_renewal_duration: Optional[pulumi.Input[str]] = None,
                 client_configuration: Optional[pulumi.Input[Union['KubeconfigClientConfigurationArgs', 'KubeconfigClientConfigurationArgsDict']]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 node: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['KubeconfigTimeoutsArgs', 'KubeconfigTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KubeconfigArgs.__new__(KubeconfigArgs)

            __props__.__dict__["certificate_renewal_duration"] = certificate_renewal_duration
            if client_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'client_configuration'")
            __props__.__dict__["client_configuration"] = client_configuration
            __props__.__dict__["endpoint"] = endpoint
            if node is None and not opts.urn:
                raise TypeError("Missing required property 'node'")
            __props__.__dict__["node"] = node
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["kubeconfig_raw"] = None
            __props__.__dict__["kubernetes_client_configuration"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["kubeconfigRaw"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Kubeconfig, __self__).__init__(
            'talos:cluster/kubeconfig:Kubeconfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate_renewal_duration: Optional[pulumi.Input[str]] = None,
            client_configuration: Optional[pulumi.Input[Union['KubeconfigClientConfigurationArgs', 'KubeconfigClientConfigurationArgsDict']]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            kubeconfig_raw: Optional[pulumi.Input[str]] = None,
            kubernetes_client_configuration: Optional[pulumi.Input[Union['KubeconfigKubernetesClientConfigurationArgs', 'KubeconfigKubernetesClientConfigurationArgsDict']]] = None,
            node: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['KubeconfigTimeoutsArgs', 'KubeconfigTimeoutsArgsDict']]] = None) -> 'Kubeconfig':
        """
        Get an existing Kubeconfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_renewal_duration: The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        :param pulumi.Input[Union['KubeconfigClientConfigurationArgs', 'KubeconfigClientConfigurationArgsDict']] client_configuration: The client configuration data
        :param pulumi.Input[str] endpoint: endpoint to use for the talosclient. If not set, the node value will be used
        :param pulumi.Input[str] kubeconfig_raw: The raw kubeconfig
        :param pulumi.Input[Union['KubeconfigKubernetesClientConfigurationArgs', 'KubeconfigKubernetesClientConfigurationArgsDict']] kubernetes_client_configuration: The kubernetes client configuration
        :param pulumi.Input[str] node: controlplane node to retrieve the kubeconfig from
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KubeconfigState.__new__(_KubeconfigState)

        __props__.__dict__["certificate_renewal_duration"] = certificate_renewal_duration
        __props__.__dict__["client_configuration"] = client_configuration
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["kubeconfig_raw"] = kubeconfig_raw
        __props__.__dict__["kubernetes_client_configuration"] = kubernetes_client_configuration
        __props__.__dict__["node"] = node
        __props__.__dict__["timeouts"] = timeouts
        return Kubeconfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateRenewalDuration")
    def certificate_renewal_duration(self) -> pulumi.Output[str]:
        """
        The duration in hours before the certificate is renewed, defaults to 720h. Must be a valid duration string
        """
        return pulumi.get(self, "certificate_renewal_duration")

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> pulumi.Output['outputs.KubeconfigClientConfiguration']:
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        endpoint to use for the talosclient. If not set, the node value will be used
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="kubeconfigRaw")
    def kubeconfig_raw(self) -> pulumi.Output[str]:
        """
        The raw kubeconfig
        """
        return pulumi.get(self, "kubeconfig_raw")

    @property
    @pulumi.getter(name="kubernetesClientConfiguration")
    def kubernetes_client_configuration(self) -> pulumi.Output['outputs.KubeconfigKubernetesClientConfiguration']:
        """
        The kubernetes client configuration
        """
        return pulumi.get(self, "kubernetes_client_configuration")

    @property
    @pulumi.getter
    def node(self) -> pulumi.Output[str]:
        """
        controlplane node to retrieve the kubeconfig from
        """
        return pulumi.get(self, "node")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.KubeconfigTimeouts']]:
        return pulumi.get(self, "timeouts")

