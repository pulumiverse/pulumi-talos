package main

import (
	"fmt"
	"testing"
	"time"

	"github.com/alecthomas/jsonschema"
)

type SecretsBundle struct {
	Clock   Clock
	Cluster string
}

type Clock interface {
	Now() time.Time
}

func TestSecret(t *testing.T) {
	// schema := jsonschema.Reflect(&generate.SecretsBundle{})
	schema := jsonschema.Reflect(&SecretsBundle{})
	bytes, _ := schema.MarshalJSON()
	fmt.Println(string(bytes))
}
