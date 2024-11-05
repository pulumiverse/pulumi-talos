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
    'BootstrapTimeoutsArgs',
    'BootstrapTimeoutsArgsDict',
    'TimeoutArgs',
    'TimeoutArgsDict',
    'CertificateArgs',
    'CertificateArgsDict',
    'CertificatesArgs',
    'CertificatesArgsDict',
    'CertificatesArgs',
    'CertificatesArgsDict',
    'CertificateArgs',
    'CertificateArgsDict',
    'ClientConfigurationArgs',
    'ClientConfigurationArgsDict',
    'ClusterArgs',
    'ClusterArgsDict',
    'ClusterArgs',
    'ClusterArgsDict',
    'KeyArgs',
    'KeyArgsDict',
    'KeyArgs',
    'KeyArgsDict',
    'KubernetesSecretsArgs',
    'KubernetesSecretsArgsDict',
    'KubernetesSecretsArgs',
    'KubernetesSecretsArgsDict',
    'MachineSecretsArgs',
    'MachineSecretsArgsDict',
    'MachineSecretsArgs',
    'MachineSecretsArgsDict',
    'TrustdInfoArgs',
    'TrustdInfoArgsDict',
    'TrustdInfoArgs',
    'TrustdInfoArgsDict',
    'GetDisksClientConfigurationArgs',
    'GetDisksClientConfigurationArgsDict',
    'GetDisksFiltersArgs',
    'GetDisksFiltersArgsDict',
    'GetDisksTimeoutsArgs',
    'GetDisksTimeoutsArgsDict',
]

MYPY = False

if not MYPY:
    class BootstrapTimeoutsArgsDict(TypedDict):
        create: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
elif False:
    BootstrapTimeoutsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class BootstrapTimeoutsArgs:
    def __init__(__self__, *,
                 create: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] create: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        if create is not None:
            pulumi.set(__self__, "create", create)

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


if not MYPY:
    class TimeoutArgsDict(TypedDict):
        create: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        update: NotRequired[pulumi.Input[str]]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
elif False:
    TimeoutArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TimeoutArgs:
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
    class CertificateArgsDict(TypedDict):
        """
        A Machine Secrets Certificate
        """
        cert: str
        """
        Certificate
        """
        key: str
        """
        Private Key
        """
elif False:
    CertificateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 cert: str,
                 key: str):
        """
        A Machine Secrets Certificate
        :param str cert: Certificate
        :param str key: Private Key
        """
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> str:
        """
        Certificate
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: str):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Private Key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


if not MYPY:
    class CertificatesArgsDict(TypedDict):
        """
        A complete Machine Secrets Certificates configuration
        """
        etcd: 'CertificateArgsDict'
        k8s: 'CertificateArgsDict'
        k8s_aggregator: 'CertificateArgsDict'
        k8s_serviceaccount: 'KeyArgsDict'
        os: 'CertificateArgsDict'
elif False:
    CertificatesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CertificatesArgs:
    def __init__(__self__, *,
                 etcd: 'CertificateArgs',
                 k8s: 'CertificateArgs',
                 k8s_aggregator: 'CertificateArgs',
                 k8s_serviceaccount: 'KeyArgs',
                 os: 'CertificateArgs'):
        """
        A complete Machine Secrets Certificates configuration
        """
        pulumi.set(__self__, "etcd", etcd)
        pulumi.set(__self__, "k8s", k8s)
        pulumi.set(__self__, "k8s_aggregator", k8s_aggregator)
        pulumi.set(__self__, "k8s_serviceaccount", k8s_serviceaccount)
        pulumi.set(__self__, "os", os)

    @property
    @pulumi.getter
    def etcd(self) -> 'CertificateArgs':
        return pulumi.get(self, "etcd")

    @etcd.setter
    def etcd(self, value: 'CertificateArgs'):
        pulumi.set(self, "etcd", value)

    @property
    @pulumi.getter
    def k8s(self) -> 'CertificateArgs':
        return pulumi.get(self, "k8s")

    @k8s.setter
    def k8s(self, value: 'CertificateArgs'):
        pulumi.set(self, "k8s", value)

    @property
    @pulumi.getter(name="k8sAggregator")
    def k8s_aggregator(self) -> 'CertificateArgs':
        return pulumi.get(self, "k8s_aggregator")

    @k8s_aggregator.setter
    def k8s_aggregator(self, value: 'CertificateArgs'):
        pulumi.set(self, "k8s_aggregator", value)

    @property
    @pulumi.getter(name="k8sServiceaccount")
    def k8s_serviceaccount(self) -> 'KeyArgs':
        return pulumi.get(self, "k8s_serviceaccount")

    @k8s_serviceaccount.setter
    def k8s_serviceaccount(self, value: 'KeyArgs'):
        pulumi.set(self, "k8s_serviceaccount", value)

    @property
    @pulumi.getter
    def os(self) -> 'CertificateArgs':
        return pulumi.get(self, "os")

    @os.setter
    def os(self, value: 'CertificateArgs'):
        pulumi.set(self, "os", value)


if not MYPY:
    class CertificatesArgsDict(TypedDict):
        """
        A complete Machine Secrets Certificates configuration
        """
        etcd: pulumi.Input['CertificateArgsDict']
        k8s: pulumi.Input['CertificateArgsDict']
        k8s_aggregator: pulumi.Input['CertificateArgsDict']
        k8s_serviceaccount: pulumi.Input['KeyArgsDict']
        os: pulumi.Input['CertificateArgsDict']
elif False:
    CertificatesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CertificatesArgs:
    def __init__(__self__, *,
                 etcd: pulumi.Input['CertificateArgs'],
                 k8s: pulumi.Input['CertificateArgs'],
                 k8s_aggregator: pulumi.Input['CertificateArgs'],
                 k8s_serviceaccount: pulumi.Input['KeyArgs'],
                 os: pulumi.Input['CertificateArgs']):
        """
        A complete Machine Secrets Certificates configuration
        """
        pulumi.set(__self__, "etcd", etcd)
        pulumi.set(__self__, "k8s", k8s)
        pulumi.set(__self__, "k8s_aggregator", k8s_aggregator)
        pulumi.set(__self__, "k8s_serviceaccount", k8s_serviceaccount)
        pulumi.set(__self__, "os", os)

    @property
    @pulumi.getter
    def etcd(self) -> pulumi.Input['CertificateArgs']:
        return pulumi.get(self, "etcd")

    @etcd.setter
    def etcd(self, value: pulumi.Input['CertificateArgs']):
        pulumi.set(self, "etcd", value)

    @property
    @pulumi.getter
    def k8s(self) -> pulumi.Input['CertificateArgs']:
        return pulumi.get(self, "k8s")

    @k8s.setter
    def k8s(self, value: pulumi.Input['CertificateArgs']):
        pulumi.set(self, "k8s", value)

    @property
    @pulumi.getter(name="k8sAggregator")
    def k8s_aggregator(self) -> pulumi.Input['CertificateArgs']:
        return pulumi.get(self, "k8s_aggregator")

    @k8s_aggregator.setter
    def k8s_aggregator(self, value: pulumi.Input['CertificateArgs']):
        pulumi.set(self, "k8s_aggregator", value)

    @property
    @pulumi.getter(name="k8sServiceaccount")
    def k8s_serviceaccount(self) -> pulumi.Input['KeyArgs']:
        return pulumi.get(self, "k8s_serviceaccount")

    @k8s_serviceaccount.setter
    def k8s_serviceaccount(self, value: pulumi.Input['KeyArgs']):
        pulumi.set(self, "k8s_serviceaccount", value)

    @property
    @pulumi.getter
    def os(self) -> pulumi.Input['CertificateArgs']:
        return pulumi.get(self, "os")

    @os.setter
    def os(self, value: pulumi.Input['CertificateArgs']):
        pulumi.set(self, "os", value)


if not MYPY:
    class CertificateArgsDict(TypedDict):
        """
        A Machine Secrets Certificate
        """
        cert: pulumi.Input[str]
        """
        Certificate
        """
        key: pulumi.Input[str]
        """
        Private Key
        """
elif False:
    CertificateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 cert: pulumi.Input[str],
                 key: pulumi.Input[str]):
        """
        A Machine Secrets Certificate
        :param pulumi.Input[str] cert: Certificate
        :param pulumi.Input[str] key: Private Key
        """
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Input[str]:
        """
        Certificate
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: pulumi.Input[str]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Private Key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)


if not MYPY:
    class ClientConfigurationArgsDict(TypedDict):
        """
        A Client Configuration
        """
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
        The client private key
        """
elif False:
    ClientConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ClientConfigurationArgs:
    def __init__(__self__, *,
                 ca_certificate: pulumi.Input[str],
                 client_certificate: pulumi.Input[str],
                 client_key: pulumi.Input[str]):
        """
        A Client Configuration
        :param pulumi.Input[str] ca_certificate: The client CA certificate
        :param pulumi.Input[str] client_certificate: The client certificate
        :param pulumi.Input[str] client_key: The client private key
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
        The client private key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_key", value)


if not MYPY:
    class ClusterArgsDict(TypedDict):
        """
        A Machine Secrets Cluster Info
        """
        id: str
        """
        Certificate
        """
        secret: str
        """
        Private Key
        """
elif False:
    ClusterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 id: str,
                 secret: str):
        """
        A Machine Secrets Cluster Info
        :param str id: Certificate
        :param str secret: Private Key
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Certificate
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: str):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def secret(self) -> str:
        """
        Private Key
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: str):
        pulumi.set(self, "secret", value)


if not MYPY:
    class ClusterArgsDict(TypedDict):
        """
        A Machine Secrets Cluster Info
        """
        id: pulumi.Input[str]
        """
        Certificate
        """
        secret: pulumi.Input[str]
        """
        Private Key
        """
elif False:
    ClusterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        """
        A Machine Secrets Cluster Info
        :param pulumi.Input[str] id: Certificate
        :param pulumi.Input[str] secret: Private Key
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Certificate
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        """
        Private Key
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)


if not MYPY:
    class KeyArgsDict(TypedDict):
        """
        A Machine Secrets Private Key
        """
        key: str
        """
        Private Key
        """
elif False:
    KeyArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyArgs:
    def __init__(__self__, *,
                 key: str):
        """
        A Machine Secrets Private Key
        :param str key: Private Key
        """
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Private Key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


if not MYPY:
    class KeyArgsDict(TypedDict):
        """
        A Machine Secrets Private Key
        """
        key: pulumi.Input[str]
        """
        Private Key
        """
elif False:
    KeyArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str]):
        """
        A Machine Secrets Private Key
        :param pulumi.Input[str] key: Private Key
        """
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Private Key
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)


if not MYPY:
    class KubernetesSecretsArgsDict(TypedDict):
        """
        A Machine Secrets Bootstrap data
        """
        bootstrap_token: str
        """
        The bootstrap token for the talos kubernetes cluster
        """
        secretbox_encryption_secret: str
        """
        The secretbox encryption secret for the talos kubernetes cluster
        """
        aescbc_encryption_secret: NotRequired[str]
        """
        The aescbc encryption secret for the talos kubernetes cluster
        """
elif False:
    KubernetesSecretsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KubernetesSecretsArgs:
    def __init__(__self__, *,
                 bootstrap_token: str,
                 secretbox_encryption_secret: str,
                 aescbc_encryption_secret: Optional[str] = None):
        """
        A Machine Secrets Bootstrap data
        :param str bootstrap_token: The bootstrap token for the talos kubernetes cluster
        :param str secretbox_encryption_secret: The secretbox encryption secret for the talos kubernetes cluster
        :param str aescbc_encryption_secret: The aescbc encryption secret for the talos kubernetes cluster
        """
        pulumi.set(__self__, "bootstrap_token", bootstrap_token)
        pulumi.set(__self__, "secretbox_encryption_secret", secretbox_encryption_secret)
        if aescbc_encryption_secret is not None:
            pulumi.set(__self__, "aescbc_encryption_secret", aescbc_encryption_secret)

    @property
    @pulumi.getter(name="bootstrapToken")
    def bootstrap_token(self) -> str:
        """
        The bootstrap token for the talos kubernetes cluster
        """
        return pulumi.get(self, "bootstrap_token")

    @bootstrap_token.setter
    def bootstrap_token(self, value: str):
        pulumi.set(self, "bootstrap_token", value)

    @property
    @pulumi.getter(name="secretboxEncryptionSecret")
    def secretbox_encryption_secret(self) -> str:
        """
        The secretbox encryption secret for the talos kubernetes cluster
        """
        return pulumi.get(self, "secretbox_encryption_secret")

    @secretbox_encryption_secret.setter
    def secretbox_encryption_secret(self, value: str):
        pulumi.set(self, "secretbox_encryption_secret", value)

    @property
    @pulumi.getter(name="aescbcEncryptionSecret")
    def aescbc_encryption_secret(self) -> Optional[str]:
        """
        The aescbc encryption secret for the talos kubernetes cluster
        """
        return pulumi.get(self, "aescbc_encryption_secret")

    @aescbc_encryption_secret.setter
    def aescbc_encryption_secret(self, value: Optional[str]):
        pulumi.set(self, "aescbc_encryption_secret", value)


if not MYPY:
    class KubernetesSecretsArgsDict(TypedDict):
        """
        A Machine Secrets Bootstrap data
        """
        bootstrap_token: pulumi.Input[str]
        """
        The bootstrap token for the talos kubernetes cluster
        """
        secretbox_encryption_secret: pulumi.Input[str]
        """
        The secretbox encryption secret for the talos kubernetes cluster
        """
        aescbc_encryption_secret: NotRequired[pulumi.Input[str]]
        """
        The aescbc encryption secret for the talos kubernetes cluster
        """
elif False:
    KubernetesSecretsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KubernetesSecretsArgs:
    def __init__(__self__, *,
                 bootstrap_token: pulumi.Input[str],
                 secretbox_encryption_secret: pulumi.Input[str],
                 aescbc_encryption_secret: Optional[pulumi.Input[str]] = None):
        """
        A Machine Secrets Bootstrap data
        :param pulumi.Input[str] bootstrap_token: The bootstrap token for the talos kubernetes cluster
        :param pulumi.Input[str] secretbox_encryption_secret: The secretbox encryption secret for the talos kubernetes cluster
        :param pulumi.Input[str] aescbc_encryption_secret: The aescbc encryption secret for the talos kubernetes cluster
        """
        pulumi.set(__self__, "bootstrap_token", bootstrap_token)
        pulumi.set(__self__, "secretbox_encryption_secret", secretbox_encryption_secret)
        if aescbc_encryption_secret is not None:
            pulumi.set(__self__, "aescbc_encryption_secret", aescbc_encryption_secret)

    @property
    @pulumi.getter(name="bootstrapToken")
    def bootstrap_token(self) -> pulumi.Input[str]:
        """
        The bootstrap token for the talos kubernetes cluster
        """
        return pulumi.get(self, "bootstrap_token")

    @bootstrap_token.setter
    def bootstrap_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "bootstrap_token", value)

    @property
    @pulumi.getter(name="secretboxEncryptionSecret")
    def secretbox_encryption_secret(self) -> pulumi.Input[str]:
        """
        The secretbox encryption secret for the talos kubernetes cluster
        """
        return pulumi.get(self, "secretbox_encryption_secret")

    @secretbox_encryption_secret.setter
    def secretbox_encryption_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secretbox_encryption_secret", value)

    @property
    @pulumi.getter(name="aescbcEncryptionSecret")
    def aescbc_encryption_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The aescbc encryption secret for the talos kubernetes cluster
        """
        return pulumi.get(self, "aescbc_encryption_secret")

    @aescbc_encryption_secret.setter
    def aescbc_encryption_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aescbc_encryption_secret", value)


if not MYPY:
    class MachineSecretsArgsDict(TypedDict):
        """
        A complete Machine Secrets configuration
        """
        certs: 'CertificatesArgsDict'
        cluster: 'ClusterArgsDict'
        secrets: 'KubernetesSecretsArgsDict'
        trustdinfo: 'TrustdInfoArgsDict'
elif False:
    MachineSecretsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MachineSecretsArgs:
    def __init__(__self__, *,
                 certs: 'CertificatesArgs',
                 cluster: 'ClusterArgs',
                 secrets: 'KubernetesSecretsArgs',
                 trustdinfo: 'TrustdInfoArgs'):
        """
        A complete Machine Secrets configuration
        """
        pulumi.set(__self__, "certs", certs)
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "secrets", secrets)
        pulumi.set(__self__, "trustdinfo", trustdinfo)

    @property
    @pulumi.getter
    def certs(self) -> 'CertificatesArgs':
        return pulumi.get(self, "certs")

    @certs.setter
    def certs(self, value: 'CertificatesArgs'):
        pulumi.set(self, "certs", value)

    @property
    @pulumi.getter
    def cluster(self) -> 'ClusterArgs':
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: 'ClusterArgs'):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def secrets(self) -> 'KubernetesSecretsArgs':
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: 'KubernetesSecretsArgs'):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter
    def trustdinfo(self) -> 'TrustdInfoArgs':
        return pulumi.get(self, "trustdinfo")

    @trustdinfo.setter
    def trustdinfo(self, value: 'TrustdInfoArgs'):
        pulumi.set(self, "trustdinfo", value)


if not MYPY:
    class MachineSecretsArgsDict(TypedDict):
        """
        A complete Machine Secrets configuration
        """
        certs: pulumi.Input['CertificatesArgsDict']
        cluster: pulumi.Input['ClusterArgsDict']
        secrets: pulumi.Input['KubernetesSecretsArgsDict']
        trustdinfo: pulumi.Input['TrustdInfoArgsDict']
elif False:
    MachineSecretsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MachineSecretsArgs:
    def __init__(__self__, *,
                 certs: pulumi.Input['CertificatesArgs'],
                 cluster: pulumi.Input['ClusterArgs'],
                 secrets: pulumi.Input['KubernetesSecretsArgs'],
                 trustdinfo: pulumi.Input['TrustdInfoArgs']):
        """
        A complete Machine Secrets configuration
        """
        pulumi.set(__self__, "certs", certs)
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "secrets", secrets)
        pulumi.set(__self__, "trustdinfo", trustdinfo)

    @property
    @pulumi.getter
    def certs(self) -> pulumi.Input['CertificatesArgs']:
        return pulumi.get(self, "certs")

    @certs.setter
    def certs(self, value: pulumi.Input['CertificatesArgs']):
        pulumi.set(self, "certs", value)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Input['ClusterArgs']:
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: pulumi.Input['ClusterArgs']):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def secrets(self) -> pulumi.Input['KubernetesSecretsArgs']:
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: pulumi.Input['KubernetesSecretsArgs']):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter
    def trustdinfo(self) -> pulumi.Input['TrustdInfoArgs']:
        return pulumi.get(self, "trustdinfo")

    @trustdinfo.setter
    def trustdinfo(self, value: pulumi.Input['TrustdInfoArgs']):
        pulumi.set(self, "trustdinfo", value)


if not MYPY:
    class TrustdInfoArgsDict(TypedDict):
        """
        A Machine Secrets Trust daemon info
        """
        token: str
        """
        The trustd token for the talos kubernetes cluster
        """
elif False:
    TrustdInfoArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TrustdInfoArgs:
    def __init__(__self__, *,
                 token: str):
        """
        A Machine Secrets Trust daemon info
        :param str token: The trustd token for the talos kubernetes cluster
        """
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        The trustd token for the talos kubernetes cluster
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: str):
        pulumi.set(self, "token", value)


if not MYPY:
    class TrustdInfoArgsDict(TypedDict):
        """
        A Machine Secrets Trust daemon info
        """
        token: pulumi.Input[str]
        """
        The trustd token for the talos kubernetes cluster
        """
elif False:
    TrustdInfoArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TrustdInfoArgs:
    def __init__(__self__, *,
                 token: pulumi.Input[str]):
        """
        A Machine Secrets Trust daemon info
        :param pulumi.Input[str] token: The trustd token for the talos kubernetes cluster
        """
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        The trustd token for the talos kubernetes cluster
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)


if not MYPY:
    class GetDisksClientConfigurationArgsDict(TypedDict):
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
    GetDisksClientConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetDisksClientConfigurationArgs:
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
    class GetDisksFiltersArgsDict(TypedDict):
        bus_path: NotRequired[str]
        """
        Filter disks by bus path
        """
        modalias: NotRequired[str]
        """
        Filter disks by modalias
        """
        model: NotRequired[str]
        """
        Filter disks by model
        """
        name: NotRequired[str]
        """
        Filter disks by name
        """
        serial: NotRequired[str]
        """
        Filter disks by serial number
        """
        size: NotRequired[str]
        """
        Filter disks by size
        """
        type: NotRequired[str]
        """
        Filter disks by type
        """
        uuid: NotRequired[str]
        """
        Filter disks by uuid
        """
        wwid: NotRequired[str]
        """
        Filter disks by wwid
        """
elif False:
    GetDisksFiltersArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetDisksFiltersArgs:
    def __init__(__self__, *,
                 bus_path: Optional[str] = None,
                 modalias: Optional[str] = None,
                 model: Optional[str] = None,
                 name: Optional[str] = None,
                 serial: Optional[str] = None,
                 size: Optional[str] = None,
                 type: Optional[str] = None,
                 uuid: Optional[str] = None,
                 wwid: Optional[str] = None):
        """
        :param str bus_path: Filter disks by bus path
        :param str modalias: Filter disks by modalias
        :param str model: Filter disks by model
        :param str name: Filter disks by name
        :param str serial: Filter disks by serial number
        :param str size: Filter disks by size
        :param str type: Filter disks by type
        :param str uuid: Filter disks by uuid
        :param str wwid: Filter disks by wwid
        """
        if bus_path is not None:
            pulumi.set(__self__, "bus_path", bus_path)
        if modalias is not None:
            pulumi.set(__self__, "modalias", modalias)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if serial is not None:
            pulumi.set(__self__, "serial", serial)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if wwid is not None:
            pulumi.set(__self__, "wwid", wwid)

    @property
    @pulumi.getter(name="busPath")
    def bus_path(self) -> Optional[str]:
        """
        Filter disks by bus path
        """
        return pulumi.get(self, "bus_path")

    @bus_path.setter
    def bus_path(self, value: Optional[str]):
        pulumi.set(self, "bus_path", value)

    @property
    @pulumi.getter
    def modalias(self) -> Optional[str]:
        """
        Filter disks by modalias
        """
        return pulumi.get(self, "modalias")

    @modalias.setter
    def modalias(self, value: Optional[str]):
        pulumi.set(self, "modalias", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[str]:
        """
        Filter disks by model
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[str]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Filter disks by name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def serial(self) -> Optional[str]:
        """
        Filter disks by serial number
        """
        return pulumi.get(self, "serial")

    @serial.setter
    def serial(self, value: Optional[str]):
        pulumi.set(self, "serial", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        Filter disks by size
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[str]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Filter disks by type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[str]:
        """
        Filter disks by uuid
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[str]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter
    def wwid(self) -> Optional[str]:
        """
        Filter disks by wwid
        """
        return pulumi.get(self, "wwid")

    @wwid.setter
    def wwid(self, value: Optional[str]):
        pulumi.set(self, "wwid", value)


if not MYPY:
    class GetDisksTimeoutsArgsDict(TypedDict):
        read: NotRequired[str]
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
elif False:
    GetDisksTimeoutsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetDisksTimeoutsArgs:
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


