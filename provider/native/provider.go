package native

import (
	"context"
	"fmt"

	goprovider "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/pkg/v3/resource/provider"
	pulumirpc "github.com/pulumi/pulumi/sdk/v3/proto/go"

	"github.com/pulumiverse/pulumi-talos/provider/native/machine"
)

type Provider struct {
	prov goprovider.Provider
}

func NewProvider() *Provider {
	inst := Provider{}
	prov, err := infer.NewProviderBuilder().
		WithNamespace("talos").
		WithComponents(
			infer.ComponentF(machine.NewSecrets),
		).
		Build()
	if err != nil {
		panic(fmt.Errorf("Error in infer.NewProviderBuilder: %w", err))
	}
	inst.prov = prov
	return &inst
}

func (p *Provider) GetSpec(ctx context.Context, name, version string) (schema.PackageSpec, error) {
	return goprovider.GetSchema(ctx, name, version, p.prov)
}

func (p *Provider) GetInstance(
	_ context.Context, name,
	version string,
	host *provider.HostClient) (pulumirpc.ResourceProviderServer, error) {
	return goprovider.RawServer(name, version, p.prov)(host)
}
