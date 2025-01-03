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
    'KubeconfigClientConfigurationArgs',
    'KubeconfigClientConfigurationArgsDict',
    'KubeconfigKubernetesClientConfigurationArgs',
    'KubeconfigKubernetesClientConfigurationArgsDict',
    'KubeconfigTimeoutsArgs',
    'KubeconfigTimeoutsArgsDict',
    'GetHealthClientConfigurationArgs',
    'GetHealthClientConfigurationArgsDict',
    'GetHealthTimeoutsArgs',
    'GetHealthTimeoutsArgsDict',
    'GetKubeconfigClientConfigurationArgs',
    'GetKubeconfigClientConfigurationArgsDict',
    'GetKubeconfigTimeoutsArgs',
    'GetKubeconfigTimeoutsArgsDict',
]

MYPY = False

if not MYPY:
    class KubeconfigClientConfigurationArgsDict(TypedDict):
        ca_certificate: pulumi.Input[str]
        """
        The client CA certificate
        """
        client_certificate: pulumi.Input[str]
        """
        The client certificate
        """
        client_key: pulumi.Input[str]
        """
        The client key
        """
elif False:
    KubeconfigClientConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KubeconfigClientConfigurationArgs:
    def __init__(__self__, *,
                 ca_certificate: pulumi.Input[str],
                 client_certificate: pulumi.Input[str],
                 client_key: pulumi.Input[str]):
        """
        :param pulumi.Input[str] ca_certificate: The client CA certificate
        :param pulumi.Input[str] client_certificate: The client certificate
        :param pulumi.Input[str] client_key: The client key
        """
        pulumi.set(__self__, "ca_certificate", ca_certificate)
        pulumi.set(__self__, "client_certificate", client_certificate)
        pulumi.set(__self__, "client_key", client_key)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> pulumi.Input[str]:
        """
        The client CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @ca_certificate.setter
    def ca_certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> pulumi.Input[str]:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Input[str]:
        """
        The client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_key", value)


if not MYPY:
    class KubeconfigKubernetesClientConfigurationArgsDict(TypedDict):
        ca_certificate: NotRequired[pulumi.Input[str]]
        """
        The kubernetes CA certificate
        """
        client_certificate: NotRequired[pulumi.Input[str]]
        """
        The kubernetes client certificate
        """
        client_key: NotRequired[pulumi.Input[str]]
        """
        The kubernetes client key
        """
        host: NotRequired[pulumi.Input[str]]
        """
        The kubernetes host
        """
elif False:
    KubeconfigKubernetesClientConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KubeconfigKubernetesClientConfigurationArgs:
    def __init__(__self__, *,
                 ca_certificate: Optional[pulumi.Input[str]] = None,
                 client_certificate: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ca_certificate: The kubernetes CA certificate
        :param pulumi.Input[str] client_certificate: The kubernetes client certificate
        :param pulumi.Input[str] client_key: The kubernetes client key
        :param pulumi.Input[str] host: The kubernetes host
        """
        if ca_certificate is not None:
            pulumi.set(__self__, "ca_certificate", ca_certificate)
        if client_certificate is not None:
            pulumi.set(__self__, "client_certificate", client_certificate)
        if client_key is not None:
            pulumi.set(__self__, "client_key", client_key)
        if host is not None:
            pulumi.set(__self__, "host", host)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The kubernetes CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The kubernetes client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[str]]:
        """
        The kubernetes client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_key", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The kubernetes host
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)


if not MYPY:
    class KubeconfigTimeoutsArgsDict(TypedDict):
        create: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        update: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
elif False:
    KubeconfigTimeoutsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KubeconfigTimeoutsArgs:
    def __init__(__self__, *,
                 create: Optional[pulumi.Input[str]] = None,
                 update: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] create: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        :param pulumi.Input[str] update: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        if create is not None:
            pulumi.set(__self__, "create", create)
        if update is not None:
            pulumi.set(__self__, "update", update)

    @property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "create")

    @create.setter
    def create(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create", value)

    @property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[str]]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "update")

    @update.setter
    def update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update", value)


if not MYPY:
    class GetHealthClientConfigurationArgsDict(TypedDict):
        ca_certificate: str
        """
        The client CA certificate
        """
        client_certificate: str
        """
        The client certificate
        """
        client_key: str
        """
        The client key
        """
elif False:
    GetHealthClientConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetHealthClientConfigurationArgs:
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

    @ca_certificate.setter
    def ca_certificate(self, value: str):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> str:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: str):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> str:
        """
        The client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: str):
        pulumi.set(self, "client_key", value)


if not MYPY:
    class GetHealthTimeoutsArgsDict(TypedDict):
        read: NotRequired[str]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
elif False:
    GetHealthTimeoutsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetHealthTimeoutsArgs:
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

    @read.setter
    def read(self, value: Optional[str]):
        pulumi.set(self, "read", value)


if not MYPY:
    class GetKubeconfigClientConfigurationArgsDict(TypedDict):
        ca_certificate: str
        """
        The client CA certificate
        """
        client_certificate: str
        """
        The client certificate
        """
        client_key: str
        """
        The client key
        """
elif False:
    GetKubeconfigClientConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetKubeconfigClientConfigurationArgs:
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

    @ca_certificate.setter
    def ca_certificate(self, value: str):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> str:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: str):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> str:
        """
        The client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: str):
        pulumi.set(self, "client_key", value)


if not MYPY:
    class GetKubeconfigTimeoutsArgsDict(TypedDict):
        read: NotRequired[str]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
elif False:
    GetKubeconfigTimeoutsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetKubeconfigTimeoutsArgs:
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

    @read.setter
    def read(self, value: Optional[str]):
        pulumi.set(self, "read", value)


