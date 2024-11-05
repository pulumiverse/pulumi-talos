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

__all__ = [
    'GetHealthClientConfigurationResult',
    'GetHealthTimeoutsResult',
    'GetKubeconfigClientConfigurationResult',
    'GetKubeconfigKubernetesClientConfigurationResult',
    'GetKubeconfigTimeoutsResult',
]

@pulumi.output_type
class GetHealthClientConfigurationResult(dict):
    def __init__(__self__, *,
                 ca_certificate: str,
                 client_certificate: str,
                 client_key: str):
        """
        :param str ca_certificate: The client CA certificate
        :param str client_certificate: The client certificate
        :param str client_key: The client key
        """
        pulumi.set(__self__, "ca_certificate", ca_certificate)
        pulumi.set(__self__, "client_certificate", client_certificate)
        pulumi.set(__self__, "client_key", client_key)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> str:
        """
        The client CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> str:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> str:
        """
        The client key
        """
        return pulumi.get(self, "client_key")


@pulumi.output_type
class GetHealthTimeoutsResult(dict):
    def __init__(__self__, *,
                 read: Optional[str] = None):
        """
        :param str read: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        if read is not None:
            pulumi.set(__self__, "read", read)

    @property
    @pulumi.getter
    def read(self) -> Optional[str]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        return pulumi.get(self, "read")


@pulumi.output_type
class GetKubeconfigClientConfigurationResult(dict):
    def __init__(__self__, *,
                 ca_certificate: str,
                 client_certificate: str,
                 client_key: str):
        """
        :param str ca_certificate: The client CA certificate
        :param str client_certificate: The client certificate
        :param str client_key: The client key
        """
        pulumi.set(__self__, "ca_certificate", ca_certificate)
        pulumi.set(__self__, "client_certificate", client_certificate)
        pulumi.set(__self__, "client_key", client_key)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> str:
        """
        The client CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> str:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> str:
        """
        The client key
        """
        return pulumi.get(self, "client_key")


@pulumi.output_type
class GetKubeconfigKubernetesClientConfigurationResult(dict):
    def __init__(__self__, *,
                 ca_certificate: str,
                 client_certificate: str,
                 client_key: str,
                 host: str):
        """
        :param str ca_certificate: The kubernetes CA certificate
        :param str client_certificate: The kubernetes client certificate
        :param str client_key: The kubernetes client key
        :param str host: The kubernetes host
        """
        pulumi.set(__self__, "ca_certificate", ca_certificate)
        pulumi.set(__self__, "client_certificate", client_certificate)
        pulumi.set(__self__, "client_key", client_key)
        pulumi.set(__self__, "host", host)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> str:
        """
        The kubernetes CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> str:
        """
        The kubernetes client certificate
        """
        return pulumi.get(self, "client_certificate")

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> str:
        """
        The kubernetes client key
        """
        return pulumi.get(self, "client_key")

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The kubernetes host
        """
        return pulumi.get(self, "host")


@pulumi.output_type
class GetKubeconfigTimeoutsResult(dict):
    def __init__(__self__, *,
                 read: Optional[str] = None):
        """
        :param str read: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        if read is not None:
            pulumi.set(__self__, "read", read)

    @property
    @pulumi.getter
    def read(self) -> Optional[str]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        return pulumi.get(self, "read")


