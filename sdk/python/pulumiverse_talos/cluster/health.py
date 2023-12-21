# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'HealthResult',
    'AwaitableHealthResult',
    'health',
    'health_output',
]

@pulumi.output_type
class HealthResult:
    """
    A collection of values returned by Health.
    """
    def __init__(__self__, client_configuration=None, control_plane_nodes=None, endpoints=None, id=None, timeouts=None, worker_nodes=None):
        if client_configuration and not isinstance(client_configuration, dict):
            raise TypeError("Expected argument 'client_configuration' to be a dict")
        pulumi.set(__self__, "client_configuration", client_configuration)
        if control_plane_nodes and not isinstance(control_plane_nodes, list):
            raise TypeError("Expected argument 'control_plane_nodes' to be a list")
        pulumi.set(__self__, "control_plane_nodes", control_plane_nodes)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if timeouts and not isinstance(timeouts, dict):
            raise TypeError("Expected argument 'timeouts' to be a dict")
        pulumi.set(__self__, "timeouts", timeouts)
        if worker_nodes and not isinstance(worker_nodes, list):
            raise TypeError("Expected argument 'worker_nodes' to be a list")
        pulumi.set(__self__, "worker_nodes", worker_nodes)

    @property
    @pulumi.getter(name="clientConfiguration")
    def client_configuration(self) -> 'outputs.HealthClientConfigurationResult':
        """
        The client configuration data
        """
        return pulumi.get(self, "client_configuration")

    @property
    @pulumi.getter(name="controlPlaneNodes")
    def control_plane_nodes(self) -> Sequence[str]:
        """
        List of control plane nodes to check for health.
        """
        return pulumi.get(self, "control_plane_nodes")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence[str]:
        """
        endpoints to use for the health check client. Use at least one control plane endpoint.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def timeouts(self) -> Optional['outputs.HealthTimeoutsResult']:
        return pulumi.get(self, "timeouts")

    @property
    @pulumi.getter(name="workerNodes")
    def worker_nodes(self) -> Optional[Sequence[str]]:
        """
        List of worker nodes to check for health.
        """
        return pulumi.get(self, "worker_nodes")


class AwaitableHealthResult(HealthResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return HealthResult(
            client_configuration=self.client_configuration,
            control_plane_nodes=self.control_plane_nodes,
            endpoints=self.endpoints,
            id=self.id,
            timeouts=self.timeouts,
            worker_nodes=self.worker_nodes)


def health(client_configuration: Optional[pulumi.InputType['HealthClientConfigurationArgs']] = None,
           control_plane_nodes: Optional[Sequence[str]] = None,
           endpoints: Optional[Sequence[str]] = None,
           timeouts: Optional[pulumi.InputType['HealthTimeoutsArgs']] = None,
           worker_nodes: Optional[Sequence[str]] = None,
           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableHealthResult:
    """
    Checks the health of a Talos cluster


    :param pulumi.InputType['HealthClientConfigurationArgs'] client_configuration: The client configuration data
    :param Sequence[str] control_plane_nodes: List of control plane nodes to check for health.
    :param Sequence[str] endpoints: endpoints to use for the health check client. Use at least one control plane endpoint.
    :param Sequence[str] worker_nodes: List of worker nodes to check for health.
    """
    __args__ = dict()
    __args__['clientConfiguration'] = client_configuration
    __args__['controlPlaneNodes'] = control_plane_nodes
    __args__['endpoints'] = endpoints
    __args__['timeouts'] = timeouts
    __args__['workerNodes'] = worker_nodes
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('talos:cluster/health:Health', __args__, opts=opts, typ=HealthResult).value

    return AwaitableHealthResult(
        client_configuration=pulumi.get(__ret__, 'client_configuration'),
        control_plane_nodes=pulumi.get(__ret__, 'control_plane_nodes'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        id=pulumi.get(__ret__, 'id'),
        timeouts=pulumi.get(__ret__, 'timeouts'),
        worker_nodes=pulumi.get(__ret__, 'worker_nodes'))


@_utilities.lift_output_func(health)
def health_output(client_configuration: Optional[pulumi.Input[pulumi.InputType['HealthClientConfigurationArgs']]] = None,
                  control_plane_nodes: Optional[pulumi.Input[Sequence[str]]] = None,
                  endpoints: Optional[pulumi.Input[Sequence[str]]] = None,
                  timeouts: Optional[pulumi.Input[Optional[pulumi.InputType['HealthTimeoutsArgs']]]] = None,
                  worker_nodes: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[HealthResult]:
    """
    Checks the health of a Talos cluster


    :param pulumi.InputType['HealthClientConfigurationArgs'] client_configuration: The client configuration data
    :param Sequence[str] control_plane_nodes: List of control plane nodes to check for health.
    :param Sequence[str] endpoints: endpoints to use for the health check client. Use at least one control plane endpoint.
    :param Sequence[str] worker_nodes: List of worker nodes to check for health.
    """
    ...
