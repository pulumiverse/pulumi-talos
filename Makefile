PROJECT_NAME := Pulumi Talos Resource Provider

PACK             := talos
PACKDIR          := sdk
PROJECT          := github.com/siderolabs/pulumi-provider-talos

PROVIDER        := pulumi-resource-${PACK}
CODEGEN         := pulumi-gen-${PACK}
VERSION         ?= $(shell pulumictl get version)
PROVIDER_PATH   := provider
VERSION_PATH     := ${PROVIDER_PATH}/pkg/version.Version

SCHEMA_FILE     := provider/cmd/${PROVIDER}/schema.json

WORKING_DIR     := $(shell pwd)
TESTPARALLELISM := 4

ARTIFACTS := _out
TAG := $(shell git describe --tag --always --dirty)

ensure::
	cd provider && go mod tidy
	cd sdk && go mod tidy
	cd tests && go mod tidy

gen::
	(cd provider && go build -o $(WORKING_DIR)/${ARTIFACTS}/${CODEGEN} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" ${PROJECT}/${PROVIDER_PATH}/cmd/$(CODEGEN))

schema:: gen
	@echo "Generating Pulumi schema..."
	$(WORKING_DIR)/${ARTIFACTS}/${CODEGEN} schema "" $(CURDIR)
	@echo "Finished generating schema."

provider::
	(cd provider && VERSION=${VERSION} go generate cmd/${PROVIDER}/main.go)
	(cd provider && go build -o $(WORKING_DIR)/${ARTIFACTS}/${PROVIDER} -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

provider_debug::
	(cd provider && go build -o $(WORKING_DIR)/${ARTIFACTS}/${PROVIDER} -gcflags="all=-N -l" -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

test_provider::
	cd provider/pkg && go test -short -v -count=1 -cover -timeout 2h -parallel ${TESTPARALLELISM} ./...

go_sdk::
	rm -rf sdk/go
	$(WORKING_DIR)/${ARTIFACTS}/$(CODEGEN) -version=${VERSION} go $(SCHEMA_FILE) $(CURDIR)

.PHONY: build
build:: gen schema provider go_sdk

# Required for the codegen action that runs in pulumi/pulumi
only_build:: build

lint::
  ## TODO: re-add this

install-prereqs::
	wget https://github.com/pulumi/pulumictl/releases/download/v0.0.31/pulumictl-v0.0.31-linux-amd64.tar.gz
	tar -xvf pulumictl-v0.0.31-linux-amd64.tar.gz
	mv pulumictl /usr/local/bin

.PHONY: release-notes
release-notes::
	mkdir -p $(ARTIFACTS)
	@ARTIFACTS=$(ARTIFACTS) ./hack/release.sh $@ $(ARTIFACTS)/RELEASE_NOTES.md $(TAG)

GO_TEST 	 := go test -v -count=1 -cover -timeout 2h -parallel ${TESTPARALLELISM}

test_all::
	cd provider/pkg && $(GO_TEST) ./...
	cd tests/sdk/go && $(GO_TEST) ./...

