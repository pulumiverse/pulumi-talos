package machine

import (
	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Secrets struct {
	pulumi.ResourceState
	SecretsArgs
	HardcodedOutput pulumi.StringOutput `pulumi:"hardcodedOutput"`
}

type SecretsArgs struct {
}

// NewSecrets creates a new instance of the Secrets resource.
func NewSecrets(ctx *pulumi.Context, name string, compArgs *SecretsArgs, opts ...pulumi.ResourceOption) (*Secrets, error) {
	comp := &Secrets{}
	err := ctx.RegisterComponentResource(p.GetTypeToken(ctx.Context()), name, comp, opts...)
	if err != nil {
		return nil, err
	}

	comp.HardcodedOutput = pulumi.String("This is a hardcoded output string from a nested module.").ToStringOutput()

	return comp, nil
}
