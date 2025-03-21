// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package machine

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-talos/sdk/go/talos/internal"
)

// Generate a machine configuration for a node type
//
// > **Note:** Since Talos natively supports `.machine.install.diskSelector`, the `machine.getDisks` data source maybe just used to query disk information that could be used elsewhere. It's recommended to use `machine.install.diskSelector` in Talos machine configuration.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-talos/sdk/go/talos/machine"
//
// )
// func main() {
// pulumi.Run(func(ctx *pulumi.Context) error {
// thisSecrets, err := machine.NewSecrets(ctx, "this", nil)
// if err != nil {
// return err
// }
// this := machine.GetDisksOutput(ctx, machine.GetDisksOutputArgs{
// ClientConfiguration: thisSecrets.ClientConfiguration,
// Node: pulumi.String("10.5.0.2"),
// Filters: &machine.GetDisksFiltersArgs{
// Size: pulumi.String("> 100GB"),
// Type: pulumi.String("nvme"),
// },
// }, nil);
// ctx.Export("nvmeDisks", this.ApplyT(func(this machine.GetDisksResult) ([]*string, error) {
// var splat0 []*string
// for _, val0 := range this.Disks {
// splat0 = append(splat0, val0.Name)
// }
// return splat0, nil
// }).(pulumi.[]*stringOutput))
// return nil
// })
// }
// ```
func GetDisks(ctx *pulumi.Context, args *GetDisksArgs, opts ...pulumi.InvokeOption) (*GetDisksResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetDisksResult
	err := ctx.Invoke("talos:machine/getDisks:getDisks", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDisks.
type GetDisksArgs struct {
	// The client configuration data
	ClientConfiguration GetDisksClientConfiguration `pulumi:"clientConfiguration"`
	// endpoint to use for the talosclient. If not set, the node value will be used
	Endpoint *string `pulumi:"endpoint"`
	// Filters to apply to the disks
	Filters *GetDisksFilters `pulumi:"filters"`
	// controlplane node to retrieve the kubeconfig from
	Node     string            `pulumi:"node"`
	Timeouts *GetDisksTimeouts `pulumi:"timeouts"`
}

// A collection of values returned by getDisks.
type GetDisksResult struct {
	// The client configuration data
	ClientConfiguration GetDisksClientConfiguration `pulumi:"clientConfiguration"`
	// The disks that match the filters
	Disks []GetDisksDisk `pulumi:"disks"`
	// endpoint to use for the talosclient. If not set, the node value will be used
	Endpoint string `pulumi:"endpoint"`
	// Filters to apply to the disks
	Filters *GetDisksFilters `pulumi:"filters"`
	// The generated ID of this resource
	Id string `pulumi:"id"`
	// controlplane node to retrieve the kubeconfig from
	Node     string            `pulumi:"node"`
	Timeouts *GetDisksTimeouts `pulumi:"timeouts"`
}

func GetDisksOutput(ctx *pulumi.Context, args GetDisksOutputArgs, opts ...pulumi.InvokeOption) GetDisksResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetDisksResultOutput, error) {
			args := v.(GetDisksArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("talos:machine/getDisks:getDisks", args, GetDisksResultOutput{}, options).(GetDisksResultOutput), nil
		}).(GetDisksResultOutput)
}

// A collection of arguments for invoking getDisks.
type GetDisksOutputArgs struct {
	// The client configuration data
	ClientConfiguration GetDisksClientConfigurationInput `pulumi:"clientConfiguration"`
	// endpoint to use for the talosclient. If not set, the node value will be used
	Endpoint pulumi.StringPtrInput `pulumi:"endpoint"`
	// Filters to apply to the disks
	Filters GetDisksFiltersPtrInput `pulumi:"filters"`
	// controlplane node to retrieve the kubeconfig from
	Node     pulumi.StringInput       `pulumi:"node"`
	Timeouts GetDisksTimeoutsPtrInput `pulumi:"timeouts"`
}

func (GetDisksOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDisksArgs)(nil)).Elem()
}

// A collection of values returned by getDisks.
type GetDisksResultOutput struct{ *pulumi.OutputState }

func (GetDisksResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDisksResult)(nil)).Elem()
}

func (o GetDisksResultOutput) ToGetDisksResultOutput() GetDisksResultOutput {
	return o
}

func (o GetDisksResultOutput) ToGetDisksResultOutputWithContext(ctx context.Context) GetDisksResultOutput {
	return o
}

// The client configuration data
func (o GetDisksResultOutput) ClientConfiguration() GetDisksClientConfigurationOutput {
	return o.ApplyT(func(v GetDisksResult) GetDisksClientConfiguration { return v.ClientConfiguration }).(GetDisksClientConfigurationOutput)
}

// The disks that match the filters
func (o GetDisksResultOutput) Disks() GetDisksDiskArrayOutput {
	return o.ApplyT(func(v GetDisksResult) []GetDisksDisk { return v.Disks }).(GetDisksDiskArrayOutput)
}

// endpoint to use for the talosclient. If not set, the node value will be used
func (o GetDisksResultOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v GetDisksResult) string { return v.Endpoint }).(pulumi.StringOutput)
}

// Filters to apply to the disks
func (o GetDisksResultOutput) Filters() GetDisksFiltersPtrOutput {
	return o.ApplyT(func(v GetDisksResult) *GetDisksFilters { return v.Filters }).(GetDisksFiltersPtrOutput)
}

// The generated ID of this resource
func (o GetDisksResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetDisksResult) string { return v.Id }).(pulumi.StringOutput)
}

// controlplane node to retrieve the kubeconfig from
func (o GetDisksResultOutput) Node() pulumi.StringOutput {
	return o.ApplyT(func(v GetDisksResult) string { return v.Node }).(pulumi.StringOutput)
}

func (o GetDisksResultOutput) Timeouts() GetDisksTimeoutsPtrOutput {
	return o.ApplyT(func(v GetDisksResult) *GetDisksTimeouts { return v.Timeouts }).(GetDisksTimeoutsPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDisksResultOutput{})
}
