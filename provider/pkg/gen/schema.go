package gen

import (
	"encoding/json"
	"fmt"
	"strings"

	"github.com/alecthomas/jsonschema"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/go/common/util/contract"
)

const (
	TalosMachineConfigVersion = "v1alpha1"
)

func PulumiSchema(swagger *jsonschema.Schema) schema.PackageSpec {
	pkg := schema.PackageSpec{
		Name:        "talos",
		Description: "A Pulumi package for creating and managing talos config",
		License:     "Apache-2.0",
		Keywords:    []string{"talos", "kubernetes", "pulumi"},
		Homepage:    "https://talos.dev",
		Repository:  "https://github.com/frezbo/pulumi-provider-talos",

		Config: schema.ConfigSpec{
			// Variables: map[string]schema.PropertySpec{
			// 	"talosVersion": {
			// 		TypeSpec:    schema.TypeSpec{Type: "string"},
			// 		Description: " the desired Talos version to generate config for (backwards compatibility, e.g. v0.8)",
			// 	},
			// 	"configVersion": {
			// 		TypeSpec:    schema.TypeSpec{Type: "string"},
			// 		Description: "the desired machine config version to generate (default \"v1alpha1\")",
			// 		Default:     "v1alpha1",
			// 	},
			// },
		},

		Provider: schema.ResourceSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Description: "The provider type for the Talos package",
				Type:        "object",
			},
			// InputProperties: map[string]schema.PropertySpec{
			// 	"talosVersion": {
			// 		TypeSpec:    schema.TypeSpec{Type: "string"},
			// 		Description: " the desired Talos version to generate config for (backwards compatibility, e.g. v0.8)",
			// 	},
			// 	"configVersion": {
			// 		TypeSpec:    schema.TypeSpec{Type: "string"},
			// 		Description: "the desired machine config version to generate (default \"v1alpha1\")",
			// 		Default:     "v1alpha1",
			// 	},
			// },
		},

		Types:     map[string]schema.ComplexTypeSpec{},
		Resources: map[string]schema.ResourceSpec{},
		Functions: map[string]schema.FunctionSpec{},
		Language:  map[string]schema.RawMessage{},
	}

	goImportPath := "github.com/frezbo/pulumi-provider-talos/sdk/v3/go/talos"

	pkgImportAliases := map[string]string{
		fmt.Sprintf("%s/%s", goImportPath, "bundle"): "bundle",
	}

	for defintion, definitionProperties := range swagger.Definitions {

		// defintionSmallCased := strings.ToLower(defintion)

		tok := fmt.Sprintf("talos:%s:%s", "bundle", defintion)

		objectSpec := schema.ObjectTypeSpec{
			Description: fmt.Sprintf("Talos %s", defintion),
			Type:        "object",
			Properties:  map[string]schema.PropertySpec{},
			Language:    map[string]schema.RawMessage{},
		}

		resourceSpec := schema.ResourceSpec{
			ObjectTypeSpec:  objectSpec,
			InputProperties: map[string]schema.PropertySpec{},
			RequiredInputs:  definitionProperties.Required,
		}

		// add the Clock field
		// if defintion == "SecretsBundle" {
		// 	definitionProperties.Properties.Set("Clock", &jsonschema.Type{
		// 		Type: "object",
		// 	})
		// 	definitionProperties.Required = append(definitionProperties.Required, "Clock")
		// }

		// pkgImportAliases[fmt.Sprintf("%s/%s", goImportPath, defintionSmallCased)] = defintionSmallCased

		for _, definitionPropertyKey := range definitionProperties.Properties.Keys() {
			if val, ok := definitionProperties.Properties.Get(definitionPropertyKey); ok {
				// the returned value is an interface
				// we need to cast it to jsonSchema.Type to access the fields
				definitionPropertyValue := val.(*jsonschema.Type)

				resourceOutputProperty := schema.PropertySpec{
					TypeSpec: schema.TypeSpec{
						Type: definitionPropertyValue.Type,
						Ref:  openAPISpecRefToPulumiRef(definitionPropertyValue.Ref),
					},
				}
				if definitionPropertyValue.Items != nil {
					resourceOutputProperty.TypeSpec.Items = &schema.TypeSpec{
						Type: definitionPropertyValue.Items.Type,
						Ref:  openAPISpecRefToPulumiRef(definitionPropertyValue.Items.Ref),
					}
				}

				resourceSpec.Properties[definitionPropertyKey] = resourceOutputProperty

				typeSpec := schema.ComplexTypeSpec{
					ObjectTypeSpec: schema.ObjectTypeSpec{
						Description: fmt.Sprintf("Talos %s type", defintion),
						Type:        "object",
						Properties:  resourceSpec.Properties,
						Language:    map[string]schema.RawMessage{},
					},
				}

				pkg.Types[tok] = typeSpec
			}
		}

		// let's add the secretsBundle resource
		pkg.Resources["talos:bundle:secretsBundle"] = schema.ResourceSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Description: "Talos secretsBundle resource",
				Type:        "string",
				Properties: map[string]schema.PropertySpec{
					"secretsBundle": {
						TypeSpec: schema.TypeSpec{
							Type: "string",
							Ref:  "#types/talos:bundle:SecretsBundle",
						},
					},
				},
				Required: []string{"secretsBundle"},
			},
			InputProperties: map[string]schema.PropertySpec{
				"talosVersion": {
					TypeSpec:    schema.TypeSpec{Type: "string"},
					Description: "the desired Talos version to generate config for (backwards compatibility, e.g. v0.8)",
				},
				"configVersion": {
					TypeSpec: schema.TypeSpec{
						OneOf: []schema.TypeSpec{
							{
								Type: "string",
							},
							{
								Type: "string",
								Ref:  "#types/talos:bundle:TalosMachineConfigVersion",
							},
						},
					},
					Description: "the desired machine config version to generate (default \"v1alpha1\")",
					Default:     "v1alpha1",
				},
			},
		}

		pkg.Types["talos:bundle:TalosMachineConfigVersion"] = schema.ComplexTypeSpec{
			ObjectTypeSpec: schema.ObjectTypeSpec{
				Type: "string",
			},
			Enum: []schema.EnumValueSpec{
				{
					Value:       TalosMachineConfigVersion,
					Description: "Talos ",
				},
			},
		}
	}

	pkg.Language["go"] = rawMessage(map[string]interface{}{
		"importBasePath":                 goImportPath,
		"packageImportAliases":           pkgImportAliases,
		"generateResourceContainerTypes": true,
	})

	pkg.Language["nodejs"] = rawMessage(map[string]interface{}{
		"dependencies": map[string]string{
			"@pulumi/pulumi": "^3.0.0",
		},
		"devDependencies": map[string]string{
			"typescript":  "^3.7.0",
			"@types/node": "^17.0.0",
		},
	})

	return pkg
}

func rawMessage(v interface{}) schema.RawMessage {
	bytes, err := json.Marshal(v)
	contract.Assert(err == nil)
	return bytes
}

func openAPISpecRefToPulumiRef(ref string) string {
	if ref != "" {
		// convert openAPI schema references to Pulumi schema reference
		// remove `definitions` and replace by `types`
		// ref: https://www.pulumi.com/docs/guides/pulumi-packages/schema/#
		ref = strings.ReplaceAll(ref, "#/definitions/", "")
		ref = fmt.Sprintf("%s/talos:%s:%s", "#/types", "bundle", ref)
		return ref
	}
	return ref
}
