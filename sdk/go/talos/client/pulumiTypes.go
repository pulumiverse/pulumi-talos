// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package client

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-talos/sdk/go/talos/internal"
)

var _ = internal.GetEnvOrDefault

type GetConfigurationClientConfiguration struct {
	// The client CA certificate
	CaCertificate string `pulumi:"caCertificate"`
	// The client certificate
	ClientCertificate string `pulumi:"clientCertificate"`
	// The client key
	ClientKey string `pulumi:"clientKey"`
}

// GetConfigurationClientConfigurationInput is an input type that accepts GetConfigurationClientConfigurationArgs and GetConfigurationClientConfigurationOutput values.
// You can construct a concrete instance of `GetConfigurationClientConfigurationInput` via:
//
//	GetConfigurationClientConfigurationArgs{...}
type GetConfigurationClientConfigurationInput interface {
	pulumi.Input

	ToGetConfigurationClientConfigurationOutput() GetConfigurationClientConfigurationOutput
	ToGetConfigurationClientConfigurationOutputWithContext(context.Context) GetConfigurationClientConfigurationOutput
}

type GetConfigurationClientConfigurationArgs struct {
	// The client CA certificate
	CaCertificate pulumi.StringInput `pulumi:"caCertificate"`
	// The client certificate
	ClientCertificate pulumi.StringInput `pulumi:"clientCertificate"`
	// The client key
	ClientKey pulumi.StringInput `pulumi:"clientKey"`
}

func (GetConfigurationClientConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetConfigurationClientConfiguration)(nil)).Elem()
}

func (i GetConfigurationClientConfigurationArgs) ToGetConfigurationClientConfigurationOutput() GetConfigurationClientConfigurationOutput {
	return i.ToGetConfigurationClientConfigurationOutputWithContext(context.Background())
}

func (i GetConfigurationClientConfigurationArgs) ToGetConfigurationClientConfigurationOutputWithContext(ctx context.Context) GetConfigurationClientConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetConfigurationClientConfigurationOutput)
}

type GetConfigurationClientConfigurationOutput struct{ *pulumi.OutputState }

func (GetConfigurationClientConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetConfigurationClientConfiguration)(nil)).Elem()
}

func (o GetConfigurationClientConfigurationOutput) ToGetConfigurationClientConfigurationOutput() GetConfigurationClientConfigurationOutput {
	return o
}

func (o GetConfigurationClientConfigurationOutput) ToGetConfigurationClientConfigurationOutputWithContext(ctx context.Context) GetConfigurationClientConfigurationOutput {
	return o
}

// The client CA certificate
func (o GetConfigurationClientConfigurationOutput) CaCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v GetConfigurationClientConfiguration) string { return v.CaCertificate }).(pulumi.StringOutput)
}

// The client certificate
func (o GetConfigurationClientConfigurationOutput) ClientCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v GetConfigurationClientConfiguration) string { return v.ClientCertificate }).(pulumi.StringOutput)
}

// The client key
func (o GetConfigurationClientConfigurationOutput) ClientKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetConfigurationClientConfiguration) string { return v.ClientKey }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GetConfigurationClientConfigurationInput)(nil)).Elem(), GetConfigurationClientConfigurationArgs{})
	pulumi.RegisterOutputType(GetConfigurationClientConfigurationOutput{})
}
