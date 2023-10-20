// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package client

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ConfigurationClientConfiguration struct {
	// The client CA certificate
	CaCertificate string `pulumi:"caCertificate"`
	// The client certificate
	ClientCertificate string `pulumi:"clientCertificate"`
	// The client key
	ClientKey string `pulumi:"clientKey"`
}

// ConfigurationClientConfigurationInput is an input type that accepts ConfigurationClientConfigurationArgs and ConfigurationClientConfigurationOutput values.
// You can construct a concrete instance of `ConfigurationClientConfigurationInput` via:
//
//	ConfigurationClientConfigurationArgs{...}
type ConfigurationClientConfigurationInput interface {
	pulumi.Input

	ToConfigurationClientConfigurationOutput() ConfigurationClientConfigurationOutput
	ToConfigurationClientConfigurationOutputWithContext(context.Context) ConfigurationClientConfigurationOutput
}

type ConfigurationClientConfigurationArgs struct {
	// The client CA certificate
	CaCertificate pulumi.StringInput `pulumi:"caCertificate"`
	// The client certificate
	ClientCertificate pulumi.StringInput `pulumi:"clientCertificate"`
	// The client key
	ClientKey pulumi.StringInput `pulumi:"clientKey"`
}

func (ConfigurationClientConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationClientConfiguration)(nil)).Elem()
}

func (i ConfigurationClientConfigurationArgs) ToConfigurationClientConfigurationOutput() ConfigurationClientConfigurationOutput {
	return i.ToConfigurationClientConfigurationOutputWithContext(context.Background())
}

func (i ConfigurationClientConfigurationArgs) ToConfigurationClientConfigurationOutputWithContext(ctx context.Context) ConfigurationClientConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationClientConfigurationOutput)
}

type ConfigurationClientConfigurationOutput struct{ *pulumi.OutputState }

func (ConfigurationClientConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationClientConfiguration)(nil)).Elem()
}

func (o ConfigurationClientConfigurationOutput) ToConfigurationClientConfigurationOutput() ConfigurationClientConfigurationOutput {
	return o
}

func (o ConfigurationClientConfigurationOutput) ToConfigurationClientConfigurationOutputWithContext(ctx context.Context) ConfigurationClientConfigurationOutput {
	return o
}

// The client CA certificate
func (o ConfigurationClientConfigurationOutput) CaCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v ConfigurationClientConfiguration) string { return v.CaCertificate }).(pulumi.StringOutput)
}

// The client certificate
func (o ConfigurationClientConfigurationOutput) ClientCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v ConfigurationClientConfiguration) string { return v.ClientCertificate }).(pulumi.StringOutput)
}

// The client key
func (o ConfigurationClientConfigurationOutput) ClientKey() pulumi.StringOutput {
	return o.ApplyT(func(v ConfigurationClientConfiguration) string { return v.ClientKey }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationClientConfigurationInput)(nil)).Elem(), ConfigurationClientConfigurationArgs{})
	pulumi.RegisterOutputType(ConfigurationClientConfigurationOutput{})
}