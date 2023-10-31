---
title: Talos Linux Installation & Configuration
meta_desc: Information on how to install the Talos Linux provider for Pulumi.
layout: installation
---

## Installation

The Pulumiverse Talos Linux provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@pulumiverse/talos`](https://www.npmjs.com/package/@pulumiverse/talos)
* Python: [`pulumiverse_talos`](https://pypi.org/project/pulumiverse-talos/)
* Go: [`github.com/pulumiverse/pulumi-talos/sdk/go/talos`](https://pkg.go.dev/github.com/pulumiverse/pulumi-talos/sdk/go)
* .NET: [`Pulumiverse.Talos`](https://www.nuget.org/packages/Pulumiverse.Talos)

### Provider Binary

The Talos provider binary is a third party binary. It can be installed using the pulumi plugin command.

```bash
pulumi plugin install resource talos <version> --server github://api.github.com/pulumiverse
```

Replace the version string with your desired version.

## Setup

There are no provider configuration options. When accessing Talos Linux machines, use the `node` property on the machine related resources.
