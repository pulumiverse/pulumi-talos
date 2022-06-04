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

gen_provider::
	(cd provider && VERSION=${VERSION} go generate cmd/${PROVIDER}/main.go)

provider_darwin_amd64::
	(cd provider && GOOS=darwin GOARCH=amd64 go build -o $(WORKING_DIR)/${ARTIFACTS}/${PROVIDER}-darwin-amd64 -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

provider_darwin_arm64::
	(cd provider && GOOS=darwin GOARCH=arm64 go build -o $(WORKING_DIR)/${ARTIFACTS}/${PROVIDER}-darwin-arm64 -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

provider_linux_amd64::
	(cd provider && GOOS=linux GOARCH=amd64 go build -o $(WORKING_DIR)/${ARTIFACTS}/${PROVIDER}-linux-amd64 -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

provider_linux_arm64::
	(cd provider && GOOS=linux GOARCH=arm64 go build -o $(WORKING_DIR)/${ARTIFACTS}/${PROVIDER}-linux-arm64 -ldflags "-X ${PROJECT}/${VERSION_PATH}=${VERSION}" $(PROJECT)/${PROVIDER_PATH}/cmd/$(PROVIDER))

provider:: gen_provider provider_darwin_amd64 provider_darwin_arm64 provider_linux_amd64 provider_linux_arm64
	
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
	wget -P /tmp https://github.com/pulumi/pulumictl/releases/download/v0.0.31/pulumictl-v0.0.31-linux-amd64.tar.gz
	tar -xvf /tmp/pulumictl-v0.0.31-linux-amd64.tar.gz -C /tmp 
	mv /tmp/pulumictl /usr/local/bin

.PHONY: release-notes
release-notes::
	mkdir -p $(ARTIFACTS)
	@ARTIFACTS=$(ARTIFACTS) ./hack/release.sh $@ $(ARTIFACTS)/RELEASE_NOTES.md $(TAG)

GO_TEST 	 := go test -v -count=1 -cover -timeout 2h -parallel ${TESTPARALLELISM}

test_all::
	cd provider/pkg && $(GO_TEST) ./...
	cd tests/sdk/go && $(GO_TEST) ./...

