package shim

import (
	"context"

	"github.com/siderolabs/terraform-provider-talos/internal/talos"

	pftfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
)

func ShimmedProvider() shim.Provider {
	t := talos.New()
	return pftfbridge.MuxShimWithPF(
		context.Background(),
		shimv2.NewProvider(talos.Provider()),
		t(),
	)
}
