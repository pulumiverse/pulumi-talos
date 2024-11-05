// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package talos

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-talos/sdk/go/talos/internal"
)

// The image factory extensions versions data source provides a list of available extensions for a specific talos version from the image factory.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-talos/sdk/go/talos"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := talos.GetImageFactoryExtensionsVersions(ctx, &talos.GetImageFactoryExtensionsVersionsArgs{
//				TalosVersion: "v1.7.5",
//				Filters: talos.GetImageFactoryExtensionsVersionsFilters{
//					Names: []string{
//						"amdgpu",
//						"tailscale",
//					},
//				},
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetImageFactoryExtensionsVersions(ctx *pulumi.Context, args *GetImageFactoryExtensionsVersionsArgs, opts ...pulumi.InvokeOption) (*GetImageFactoryExtensionsVersionsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetImageFactoryExtensionsVersionsResult
	err := ctx.Invoke("talos:index/getImageFactoryExtensionsVersions:getImageFactoryExtensionsVersions", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getImageFactoryExtensionsVersions.
type GetImageFactoryExtensionsVersionsArgs struct {
	// The filter to apply to the extensions list.
	Filters *GetImageFactoryExtensionsVersionsFilters `pulumi:"filters"`
	// The talos version to get extensions for.
	TalosVersion string `pulumi:"talosVersion"`
}

// A collection of values returned by getImageFactoryExtensionsVersions.
type GetImageFactoryExtensionsVersionsResult struct {
	// The list of available extensions for the specified talos version.
	ExtensionsInfos []GetImageFactoryExtensionsVersionsExtensionsInfo `pulumi:"extensionsInfos"`
	// The filter to apply to the extensions list.
	Filters *GetImageFactoryExtensionsVersionsFilters `pulumi:"filters"`
	// The ID of this resource.
	Id string `pulumi:"id"`
	// The talos version to get extensions for.
	TalosVersion string `pulumi:"talosVersion"`
}

func GetImageFactoryExtensionsVersionsOutput(ctx *pulumi.Context, args GetImageFactoryExtensionsVersionsOutputArgs, opts ...pulumi.InvokeOption) GetImageFactoryExtensionsVersionsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetImageFactoryExtensionsVersionsResultOutput, error) {
			args := v.(GetImageFactoryExtensionsVersionsArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetImageFactoryExtensionsVersionsResult
			secret, err := ctx.InvokePackageRaw("talos:index/getImageFactoryExtensionsVersions:getImageFactoryExtensionsVersions", args, &rv, "", opts...)
			if err != nil {
				return GetImageFactoryExtensionsVersionsResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetImageFactoryExtensionsVersionsResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetImageFactoryExtensionsVersionsResultOutput), nil
			}
			return output, nil
		}).(GetImageFactoryExtensionsVersionsResultOutput)
}

// A collection of arguments for invoking getImageFactoryExtensionsVersions.
type GetImageFactoryExtensionsVersionsOutputArgs struct {
	// The filter to apply to the extensions list.
	Filters GetImageFactoryExtensionsVersionsFiltersPtrInput `pulumi:"filters"`
	// The talos version to get extensions for.
	TalosVersion pulumi.StringInput `pulumi:"talosVersion"`
}

func (GetImageFactoryExtensionsVersionsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetImageFactoryExtensionsVersionsArgs)(nil)).Elem()
}

// A collection of values returned by getImageFactoryExtensionsVersions.
type GetImageFactoryExtensionsVersionsResultOutput struct{ *pulumi.OutputState }

func (GetImageFactoryExtensionsVersionsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetImageFactoryExtensionsVersionsResult)(nil)).Elem()
}

func (o GetImageFactoryExtensionsVersionsResultOutput) ToGetImageFactoryExtensionsVersionsResultOutput() GetImageFactoryExtensionsVersionsResultOutput {
	return o
}

func (o GetImageFactoryExtensionsVersionsResultOutput) ToGetImageFactoryExtensionsVersionsResultOutputWithContext(ctx context.Context) GetImageFactoryExtensionsVersionsResultOutput {
	return o
}

// The list of available extensions for the specified talos version.
func (o GetImageFactoryExtensionsVersionsResultOutput) ExtensionsInfos() GetImageFactoryExtensionsVersionsExtensionsInfoArrayOutput {
	return o.ApplyT(func(v GetImageFactoryExtensionsVersionsResult) []GetImageFactoryExtensionsVersionsExtensionsInfo {
		return v.ExtensionsInfos
	}).(GetImageFactoryExtensionsVersionsExtensionsInfoArrayOutput)
}

// The filter to apply to the extensions list.
func (o GetImageFactoryExtensionsVersionsResultOutput) Filters() GetImageFactoryExtensionsVersionsFiltersPtrOutput {
	return o.ApplyT(func(v GetImageFactoryExtensionsVersionsResult) *GetImageFactoryExtensionsVersionsFilters {
		return v.Filters
	}).(GetImageFactoryExtensionsVersionsFiltersPtrOutput)
}

// The ID of this resource.
func (o GetImageFactoryExtensionsVersionsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetImageFactoryExtensionsVersionsResult) string { return v.Id }).(pulumi.StringOutput)
}

// The talos version to get extensions for.
func (o GetImageFactoryExtensionsVersionsResultOutput) TalosVersion() pulumi.StringOutput {
	return o.ApplyT(func(v GetImageFactoryExtensionsVersionsResult) string { return v.TalosVersion }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetImageFactoryExtensionsVersionsResultOutput{})
}
