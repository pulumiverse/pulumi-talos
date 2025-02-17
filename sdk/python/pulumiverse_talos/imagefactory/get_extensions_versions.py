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

__all__ = [
    'GetExtensionsVersionsResult',
    'AwaitableGetExtensionsVersionsResult',
    'get_extensions_versions',
    'get_extensions_versions_output',
]

@pulumi.output_type
class GetExtensionsVersionsResult:
    """
    A collection of values returned by getExtensionsVersions.
    """
    def __init__(__self__, extensions_infos=None, filters=None, id=None, talos_version=None):
        if extensions_infos and not isinstance(extensions_infos, list):
            raise TypeError("Expected argument 'extensions_infos' to be a list")
        pulumi.set(__self__, "extensions_infos", extensions_infos)
        if filters and not isinstance(filters, dict):
            raise TypeError("Expected argument 'filters' to be a dict")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if talos_version and not isinstance(talos_version, str):
            raise TypeError("Expected argument 'talos_version' to be a str")
        pulumi.set(__self__, "talos_version", talos_version)

    @property
    @pulumi.getter(name="extensionsInfos")
    def extensions_infos(self) -> Sequence['outputs.GetExtensionsVersionsExtensionsInfoResult']:
        """
        The list of available extensions for the specified talos version.
        """
        return pulumi.get(self, "extensions_infos")

    @property
    @pulumi.getter
    def filters(self) -> Optional['outputs.GetExtensionsVersionsFiltersResult']:
        """
        The filter to apply to the extensions list.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="talosVersion")
    def talos_version(self) -> str:
        """
        The talos version to get extensions for.
        """
        return pulumi.get(self, "talos_version")


class AwaitableGetExtensionsVersionsResult(GetExtensionsVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtensionsVersionsResult(
            extensions_infos=self.extensions_infos,
            filters=self.filters,
            id=self.id,
            talos_version=self.talos_version)


def get_extensions_versions(filters: Optional[Union['GetExtensionsVersionsFiltersArgs', 'GetExtensionsVersionsFiltersArgsDict']] = None,
                            talos_version: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtensionsVersionsResult:
    """
    The image factory extensions versions data source provides a list of available extensions for a specific talos version from the image factory.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_talos as talos

    this = talos.imageFactory.get_extensions_versions(talos_version="v1.7.5",
        filters={
            "names": [
                "amdgpu",
                "tailscale",
            ],
        })
    ```


    :param Union['GetExtensionsVersionsFiltersArgs', 'GetExtensionsVersionsFiltersArgsDict'] filters: The filter to apply to the extensions list.
    :param str talos_version: The talos version to get extensions for.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['talosVersion'] = talos_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('talos:imageFactory/getExtensionsVersions:getExtensionsVersions', __args__, opts=opts, typ=GetExtensionsVersionsResult).value

    return AwaitableGetExtensionsVersionsResult(
        extensions_infos=pulumi.get(__ret__, 'extensions_infos'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        talos_version=pulumi.get(__ret__, 'talos_version'))
def get_extensions_versions_output(filters: Optional[pulumi.Input[Optional[Union['GetExtensionsVersionsFiltersArgs', 'GetExtensionsVersionsFiltersArgsDict']]]] = None,
                                   talos_version: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetExtensionsVersionsResult]:
    """
    The image factory extensions versions data source provides a list of available extensions for a specific talos version from the image factory.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_talos as talos

    this = talos.imageFactory.get_extensions_versions(talos_version="v1.7.5",
        filters={
            "names": [
                "amdgpu",
                "tailscale",
            ],
        })
    ```


    :param Union['GetExtensionsVersionsFiltersArgs', 'GetExtensionsVersionsFiltersArgsDict'] filters: The filter to apply to the extensions list.
    :param str talos_version: The talos version to get extensions for.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['talosVersion'] = talos_version
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('talos:imageFactory/getExtensionsVersions:getExtensionsVersions', __args__, opts=opts, typ=GetExtensionsVersionsResult)
    return __ret__.apply(lambda __response__: GetExtensionsVersionsResult(
        extensions_infos=pulumi.get(__response__, 'extensions_infos'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id'),
        talos_version=pulumi.get(__response__, 'talos_version')))
