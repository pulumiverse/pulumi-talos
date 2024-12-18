// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export namespace client {
    export interface GetConfigurationClientConfiguration {
        /**
         * The client CA certificate
         */
        caCertificate: string;
        /**
         * The client certificate
         */
        clientCertificate: string;
        /**
         * The client key
         */
        clientKey: string;
    }

    export interface GetConfigurationClientConfigurationArgs {
        /**
         * The client CA certificate
         */
        caCertificate: pulumi.Input<string>;
        /**
         * The client certificate
         */
        clientCertificate: pulumi.Input<string>;
        /**
         * The client key
         */
        clientKey: pulumi.Input<string>;
    }
}

export namespace cluster {
    export interface GetHealthClientConfiguration {
        /**
         * The client CA certificate
         */
        caCertificate: string;
        /**
         * The client certificate
         */
        clientCertificate: string;
        /**
         * The client key
         */
        clientKey: string;
    }

    export interface GetHealthClientConfigurationArgs {
        /**
         * The client CA certificate
         */
        caCertificate: pulumi.Input<string>;
        /**
         * The client certificate
         */
        clientCertificate: pulumi.Input<string>;
        /**
         * The client key
         */
        clientKey: pulumi.Input<string>;
    }

    export interface GetHealthTimeouts {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
         */
        read?: string;
    }

    export interface GetHealthTimeoutsArgs {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
         */
        read?: pulumi.Input<string>;
    }

    export interface GetKubeconfigClientConfiguration {
        /**
         * The client CA certificate
         */
        caCertificate: string;
        /**
         * The client certificate
         */
        clientCertificate: string;
        /**
         * The client key
         */
        clientKey: string;
    }

    export interface GetKubeconfigClientConfigurationArgs {
        /**
         * The client CA certificate
         */
        caCertificate: pulumi.Input<string>;
        /**
         * The client certificate
         */
        clientCertificate: pulumi.Input<string>;
        /**
         * The client key
         */
        clientKey: pulumi.Input<string>;
    }

    export interface GetKubeconfigTimeouts {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
         */
        read?: string;
    }

    export interface GetKubeconfigTimeoutsArgs {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
         */
        read?: pulumi.Input<string>;
    }

    export interface KubeconfigClientConfiguration {
        /**
         * The client CA certificate
         */
        caCertificate: pulumi.Input<string>;
        /**
         * The client certificate
         */
        clientCertificate: pulumi.Input<string>;
        /**
         * The client key
         */
        clientKey: pulumi.Input<string>;
    }

    export interface KubeconfigKubernetesClientConfiguration {
        /**
         * The kubernetes CA certificate
         */
        caCertificate?: pulumi.Input<string>;
        /**
         * The kubernetes client certificate
         */
        clientCertificate?: pulumi.Input<string>;
        /**
         * The kubernetes client key
         */
        clientKey?: pulumi.Input<string>;
        /**
         * The kubernetes host
         */
        host?: pulumi.Input<string>;
    }

    export interface KubeconfigTimeouts {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
         */
        create?: pulumi.Input<string>;
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
         */
        update?: pulumi.Input<string>;
    }
}

export namespace imageFactory {
    export interface GetExtensionsVersionsFilters {
        /**
         * The name of the extension to filter by.
         */
        names?: string[];
    }

    export interface GetExtensionsVersionsFiltersArgs {
        /**
         * The name of the extension to filter by.
         */
        names?: pulumi.Input<pulumi.Input<string>[]>;
    }

    export interface GetOverlaysVersionsFilters {
        /**
         * The name of the overlay to filter by.
         */
        name?: string;
    }

    export interface GetOverlaysVersionsFiltersArgs {
        /**
         * The name of the overlay to filter by.
         */
        name?: pulumi.Input<string>;
    }

    export interface GetVersionsFilters {
        /**
         * If set to true, only stable versions will be returned. If set to false, all versions will be returned.
         */
        stableVersionsOnly?: boolean;
    }

    export interface GetVersionsFiltersArgs {
        /**
         * If set to true, only stable versions will be returned. If set to false, all versions will be returned.
         */
        stableVersionsOnly?: pulumi.Input<boolean>;
    }
}

export namespace machine {
    export interface BootstrapTimeouts {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
         */
        create?: pulumi.Input<string>;
    }

    /**
     * A Machine Secrets Certificate
     */
    export interface Certificate {
        /**
         * Certificate
         */
        cert: string;
        /**
         * Private Key
         */
        key: string;
    }

    /**
     * A Machine Secrets Certificate
     */
    export interface CertificateArgs {
        /**
         * Certificate
         */
        cert: pulumi.Input<string>;
        /**
         * Private Key
         */
        key: pulumi.Input<string>;
    }

    /**
     * A complete Machine Secrets Certificates configuration
     */
    export interface Certificates {
        etcd: inputs.machine.Certificate;
        k8s: inputs.machine.Certificate;
        k8sAggregator: inputs.machine.Certificate;
        k8sServiceaccount: inputs.machine.Key;
        os: inputs.machine.Certificate;
    }

    /**
     * A complete Machine Secrets Certificates configuration
     */
    export interface CertificatesArgs {
        etcd: pulumi.Input<inputs.machine.CertificateArgs>;
        k8s: pulumi.Input<inputs.machine.CertificateArgs>;
        k8sAggregator: pulumi.Input<inputs.machine.CertificateArgs>;
        k8sServiceaccount: pulumi.Input<inputs.machine.KeyArgs>;
        os: pulumi.Input<inputs.machine.CertificateArgs>;
    }

    /**
     * A Client Configuration
     */
    export interface ClientConfiguration {
        /**
         * The client CA certificate
         */
        caCertificate: pulumi.Input<string>;
        /**
         * The client certificate
         */
        clientCertificate: pulumi.Input<string>;
        /**
         * The client private key
         */
        clientKey: pulumi.Input<string>;
    }

    /**
     * A Machine Secrets Cluster Info
     */
    export interface Cluster {
        /**
         * Certificate
         */
        id: string;
        /**
         * Private Key
         */
        secret: string;
    }

    /**
     * A Machine Secrets Cluster Info
     */
    export interface ClusterArgs {
        /**
         * Certificate
         */
        id: pulumi.Input<string>;
        /**
         * Private Key
         */
        secret: pulumi.Input<string>;
    }

    export interface ConfigurationApplyOnDestroy {
        /**
         * Graceful indicates whether node should leave etcd before the upgrade, it also enforces etcd checks before leaving. Default true
         */
        graceful?: pulumi.Input<boolean>;
        /**
         * Reboot indicates whether node should reboot or halt after resetting. Default false
         */
        reboot?: pulumi.Input<boolean>;
        /**
         * Reset the machine to the initial state (STATE and EPHEMERAL will be wiped). Default false
         */
        reset?: pulumi.Input<boolean>;
    }

    export interface GetDisksClientConfiguration {
        /**
         * The client CA certificate
         */
        caCertificate: string;
        /**
         * The client certificate
         */
        clientCertificate: string;
        /**
         * The client key
         */
        clientKey: string;
    }

    export interface GetDisksClientConfigurationArgs {
        /**
         * The client CA certificate
         */
        caCertificate: pulumi.Input<string>;
        /**
         * The client certificate
         */
        clientCertificate: pulumi.Input<string>;
        /**
         * The client key
         */
        clientKey: pulumi.Input<string>;
    }

    export interface GetDisksFilters {
        /**
         * Filter disks by bus path
         */
        busPath?: string;
        /**
         * Filter disks by modalias
         */
        modalias?: string;
        /**
         * Filter disks by model
         */
        model?: string;
        /**
         * Filter disks by name
         */
        name?: string;
        /**
         * Filter disks by serial number
         */
        serial?: string;
        /**
         * Filter disks by size
         */
        size?: string;
        /**
         * Filter disks by type
         */
        type?: string;
        /**
         * Filter disks by uuid
         */
        uuid?: string;
        /**
         * Filter disks by wwid
         */
        wwid?: string;
    }

    export interface GetDisksFiltersArgs {
        /**
         * Filter disks by bus path
         */
        busPath?: pulumi.Input<string>;
        /**
         * Filter disks by modalias
         */
        modalias?: pulumi.Input<string>;
        /**
         * Filter disks by model
         */
        model?: pulumi.Input<string>;
        /**
         * Filter disks by name
         */
        name?: pulumi.Input<string>;
        /**
         * Filter disks by serial number
         */
        serial?: pulumi.Input<string>;
        /**
         * Filter disks by size
         */
        size?: pulumi.Input<string>;
        /**
         * Filter disks by type
         */
        type?: pulumi.Input<string>;
        /**
         * Filter disks by uuid
         */
        uuid?: pulumi.Input<string>;
        /**
         * Filter disks by wwid
         */
        wwid?: pulumi.Input<string>;
    }

    export interface GetDisksTimeouts {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
         */
        read?: string;
    }

    export interface GetDisksTimeoutsArgs {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
         */
        read?: pulumi.Input<string>;
    }

    /**
     * A Machine Secrets Private Key
     */
    export interface Key {
        /**
         * Private Key
         */
        key: string;
    }

    /**
     * A Machine Secrets Private Key
     */
    export interface KeyArgs {
        /**
         * Private Key
         */
        key: pulumi.Input<string>;
    }

    /**
     * A Machine Secrets Bootstrap data
     */
    export interface KubernetesSecrets {
        /**
         * The aescbc encryption secret for the talos kubernetes cluster
         */
        aescbcEncryptionSecret?: string;
        /**
         * The bootstrap token for the talos kubernetes cluster
         */
        bootstrapToken: string;
        /**
         * The secretbox encryption secret for the talos kubernetes cluster
         */
        secretboxEncryptionSecret: string;
    }

    /**
     * A Machine Secrets Bootstrap data
     */
    export interface KubernetesSecretsArgs {
        /**
         * The aescbc encryption secret for the talos kubernetes cluster
         */
        aescbcEncryptionSecret?: pulumi.Input<string>;
        /**
         * The bootstrap token for the talos kubernetes cluster
         */
        bootstrapToken: pulumi.Input<string>;
        /**
         * The secretbox encryption secret for the talos kubernetes cluster
         */
        secretboxEncryptionSecret: pulumi.Input<string>;
    }

    /**
     * A complete Machine Secrets configuration
     */
    export interface MachineSecrets {
        certs: inputs.machine.Certificates;
        cluster: inputs.machine.Cluster;
        secrets: inputs.machine.KubernetesSecrets;
        trustdinfo: inputs.machine.TrustdInfo;
    }

    /**
     * A complete Machine Secrets configuration
     */
    export interface MachineSecretsArgs {
        certs: pulumi.Input<inputs.machine.CertificatesArgs>;
        cluster: pulumi.Input<inputs.machine.ClusterArgs>;
        secrets: pulumi.Input<inputs.machine.KubernetesSecretsArgs>;
        trustdinfo: pulumi.Input<inputs.machine.TrustdInfoArgs>;
    }

    export interface Timeout {
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
         */
        create?: pulumi.Input<string>;
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Setting a timeout for a Delete operation is only applicable if changes are saved into state before the destroy operation occurs.
         */
        delete?: pulumi.Input<string>;
        /**
         * A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
         */
        update?: pulumi.Input<string>;
    }

    /**
     * A Machine Secrets Trust daemon info
     */
    export interface TrustdInfo {
        /**
         * The trustd token for the talos kubernetes cluster
         */
        token: string;
    }

    /**
     * A Machine Secrets Trust daemon info
     */
    export interface TrustdInfoArgs {
        /**
         * The trustd token for the talos kubernetes cluster
         */
        token: pulumi.Input<string>;
    }
}
