package shim

import (
	tfpf "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/siderolabs/terraform-provider-talos/internal/talos"
)

func NewProvider() tfpf.Provider {
	return talos.New()
}
