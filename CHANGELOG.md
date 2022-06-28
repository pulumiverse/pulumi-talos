## [pulumi-provider-talos 0.1.0-alpha.2](https://github.com/siderolabs/pulumi-provider-talos/releases/tag/v0.1.0-alpha.2) (2022-06-28)

Welcome to the 0.1.0-alpha.2 release of pulumi-provider-talos!  
*This is a pre-release of pulumi-provider-talos*



Please try out the release binaries and report any issues at
https://github.com/siderolabs/pulumi-provider-talos/issues.

### Secrets and GenConfig resource changes

The talosconfig output has now been moved to the Secrets Resource and there is no talosconfig output for the GenConfig resource


### Contributors

* Noel Georgi
* Spencer Smith
* Spencer Smith

### Changes
<details><summary>28 commits</summary>
<p>

* [`28004e1`](https://github.com/siderolabs/pulumi-provider-talos/commit/28004e1814eeae39c55d5bab54476c434d3120d9) chore: bump machinery to v1.1.0
* [`8b9d250`](https://github.com/siderolabs/pulumi-provider-talos/commit/8b9d2507e9f33c1f6244e67893dfc5649186a717) release(v0.1.0-alpha.1): prepare release
* [`572775a`](https://github.com/siderolabs/pulumi-provider-talos/commit/572775a1b3116a16cc21cf31e5ed160196b4a4a1) feat: move talosconfig to secrets resource
* [`a42cd3c`](https://github.com/siderolabs/pulumi-provider-talos/commit/a42cd3c5e855978f4b0eee805cc2710a71343241) release(v0.1.0-alpha.0): prepare release
* [`2073e17`](https://github.com/siderolabs/pulumi-provider-talos/commit/2073e17399a756a69d32a7602d5ca1ba022f5e13) feat: build multiple architectures
* [`811dfa6`](https://github.com/siderolabs/pulumi-provider-talos/commit/811dfa6d2d3a9460da9f2a77dd07b3e8c97202ca) feat: add further CI functionality
* [`bfc411f`](https://github.com/siderolabs/pulumi-provider-talos/commit/bfc411f8abe0ad80d13c2f418fa0c632071a531a) feat: add CI testing
* [`03f43ea`](https://github.com/siderolabs/pulumi-provider-talos/commit/03f43ea60bc54847e21e9c2518b6fb6cea4d4d0d) fix: update all frezbo refs to siderolabs
* [`e11dd36`](https://github.com/siderolabs/pulumi-provider-talos/commit/e11dd361ccdffcee14b327c44fa62020a24f30f6) chore: support applying config
* [`6e068b0`](https://github.com/siderolabs/pulumi-provider-talos/commit/6e068b030b37814c3d96bccb1e35d1f487c06c06) Merge pull request  [#1](https://github.com/siderolabs/pulumi-provider-talos/pull/1) from rsmitty/main
* [`bdd1e8d`](https://github.com/siderolabs/pulumi-provider-talos/commit/bdd1e8dd95e136ce011acfcb897faf331760db28) fix: ensure additional sans are processed correctly
* [`ee48675`](https://github.com/siderolabs/pulumi-provider-talos/commit/ee4867569269e4376aefd6cf227e7ff8a34dae90) chore: bump talos to v1.0.0-beta.2
* [`d9ceba5`](https://github.com/siderolabs/pulumi-provider-talos/commit/d9ceba523c250e72cc6e472af69bb7773cf9b191) chore: update example
* [`08fd1fd`](https://github.com/siderolabs/pulumi-provider-talos/commit/08fd1fd91e659e8321199d527ae064ff3a0df831) chore: update to go 1.18
* [`09edb09`](https://github.com/siderolabs/pulumi-provider-talos/commit/09edb09055a7bad12b86f4f1624dede410aba064) chore: mark outputs as secrets
* [`cf613aa`](https://github.com/siderolabs/pulumi-provider-talos/commit/cf613aaaabdd2017aba892ed0c84eecf19ccfab3) chore: use talos/machinery from latest
* [`6642479`](https://github.com/siderolabs/pulumi-provider-talos/commit/6642479878e313e89ced2725b2c0343ce78af6dc) feat: add GetKubeConfig resource
* [`09771e3`](https://github.com/siderolabs/pulumi-provider-talos/commit/09771e3d4c0f974462b39ce65b0a0ee0cdea2c56) fix: bootstrap timeout handling
* [`836f66b`](https://github.com/siderolabs/pulumi-provider-talos/commit/836f66bd6510b0819e7b23ebf1c6d65452f8b6e8) fix: bootstrap timeout
* [`941d8f5`](https://github.com/siderolabs/pulumi-provider-talos/commit/941d8f533d88b3a513885b9c87623ca50a33736c) feat: improve patch UX
* [`141d690`](https://github.com/siderolabs/pulumi-provider-talos/commit/141d690bdea26efc3524c1a6a41b1daea4584af5) fix: casting from pulumi map to int
* [`38a41ab`](https://github.com/siderolabs/pulumi-provider-talos/commit/38a41aba8500be93cf19362d0a0d1f323545ebcf) fix: bootstrap provider
* [`eda59ca`](https://github.com/siderolabs/pulumi-provider-talos/commit/eda59cae9770f12c544c0c11f2422a6346b1208f) chore: use fork to fix grpc error
* [`2f44d32`](https://github.com/siderolabs/pulumi-provider-talos/commit/2f44d3277f2563d42f12f2d4df5ed92afe6339be) feat: add NodeBootstrap resource
* [`1e37daf`](https://github.com/siderolabs/pulumi-provider-talos/commit/1e37daf3e01bfc630853a6e0ca2246e1d4d0140b) feat: add ClusterConfig and ClusterSecrets resources
* [`8300bfa`](https://github.com/siderolabs/pulumi-provider-talos/commit/8300bfa1ea9a42e2bd9748a4ccf8d36d7af7ec54) feat: secretsBundle Create() works
* [`67b66fe`](https://github.com/siderolabs/pulumi-provider-talos/commit/67b66fec94a93bd507d06aa4d8dc1f4452c1376b) chore: first pass
* [`ecf31c0`](https://github.com/siderolabs/pulumi-provider-talos/commit/ecf31c085e9e912837e66940f80f30b23b2a0339) Initial commit
</p>
</details>

### Dependency Changes

This release has no dependency changes

## [pulumi-provider-talos 0.1.0-alpha.1](https://github.com/siderolabs/pulumi-provider-talos/releases/tag/v0.1.0-alpha.1) (2022-06-06)

Welcome to the 0.1.0-alpha.1 release of pulumi-provider-talos!  
*This is a pre-release of pulumi-provider-talos*



Please try out the release binaries and report any issues at
https://github.com/siderolabs/pulumi-provider-talos/issues.

### Secrets and GenConfig resource changes

The talosconfig output has now been moved to the Secrets Resource and there is no talosconfig output for the GenConfig resource


### Contributors

* Noel Georgi
* Spencer Smith
* Spencer Smith

### Changes
<details><summary>26 commits</summary>
<p>

* [`572775a`](https://github.com/siderolabs/pulumi-provider-talos/commit/572775a1b3116a16cc21cf31e5ed160196b4a4a1) feat: move talosconfig to secrets resource
* [`a42cd3c`](https://github.com/siderolabs/pulumi-provider-talos/commit/a42cd3c5e855978f4b0eee805cc2710a71343241) release(v0.1.0-alpha.0): prepare release
* [`2073e17`](https://github.com/siderolabs/pulumi-provider-talos/commit/2073e17399a756a69d32a7602d5ca1ba022f5e13) feat: build multiple architectures
* [`811dfa6`](https://github.com/siderolabs/pulumi-provider-talos/commit/811dfa6d2d3a9460da9f2a77dd07b3e8c97202ca) feat: add further CI functionality
* [`bfc411f`](https://github.com/siderolabs/pulumi-provider-talos/commit/bfc411f8abe0ad80d13c2f418fa0c632071a531a) feat: add CI testing
* [`03f43ea`](https://github.com/siderolabs/pulumi-provider-talos/commit/03f43ea60bc54847e21e9c2518b6fb6cea4d4d0d) fix: update all frezbo refs to siderolabs
* [`e11dd36`](https://github.com/siderolabs/pulumi-provider-talos/commit/e11dd361ccdffcee14b327c44fa62020a24f30f6) chore: support applying config
* [`6e068b0`](https://github.com/siderolabs/pulumi-provider-talos/commit/6e068b030b37814c3d96bccb1e35d1f487c06c06) Merge pull request  [#1](https://github.com/siderolabs/pulumi-provider-talos/pull/1) from rsmitty/main
* [`bdd1e8d`](https://github.com/siderolabs/pulumi-provider-talos/commit/bdd1e8dd95e136ce011acfcb897faf331760db28) fix: ensure additional sans are processed correctly
* [`ee48675`](https://github.com/siderolabs/pulumi-provider-talos/commit/ee4867569269e4376aefd6cf227e7ff8a34dae90) chore: bump talos to v1.0.0-beta.2
* [`d9ceba5`](https://github.com/siderolabs/pulumi-provider-talos/commit/d9ceba523c250e72cc6e472af69bb7773cf9b191) chore: update example
* [`08fd1fd`](https://github.com/siderolabs/pulumi-provider-talos/commit/08fd1fd91e659e8321199d527ae064ff3a0df831) chore: update to go 1.18
* [`09edb09`](https://github.com/siderolabs/pulumi-provider-talos/commit/09edb09055a7bad12b86f4f1624dede410aba064) chore: mark outputs as secrets
* [`cf613aa`](https://github.com/siderolabs/pulumi-provider-talos/commit/cf613aaaabdd2017aba892ed0c84eecf19ccfab3) chore: use talos/machinery from latest
* [`6642479`](https://github.com/siderolabs/pulumi-provider-talos/commit/6642479878e313e89ced2725b2c0343ce78af6dc) feat: add GetKubeConfig resource
* [`09771e3`](https://github.com/siderolabs/pulumi-provider-talos/commit/09771e3d4c0f974462b39ce65b0a0ee0cdea2c56) fix: bootstrap timeout handling
* [`836f66b`](https://github.com/siderolabs/pulumi-provider-talos/commit/836f66bd6510b0819e7b23ebf1c6d65452f8b6e8) fix: bootstrap timeout
* [`941d8f5`](https://github.com/siderolabs/pulumi-provider-talos/commit/941d8f533d88b3a513885b9c87623ca50a33736c) feat: improve patch UX
* [`141d690`](https://github.com/siderolabs/pulumi-provider-talos/commit/141d690bdea26efc3524c1a6a41b1daea4584af5) fix: casting from pulumi map to int
* [`38a41ab`](https://github.com/siderolabs/pulumi-provider-talos/commit/38a41aba8500be93cf19362d0a0d1f323545ebcf) fix: bootstrap provider
* [`eda59ca`](https://github.com/siderolabs/pulumi-provider-talos/commit/eda59cae9770f12c544c0c11f2422a6346b1208f) chore: use fork to fix grpc error
* [`2f44d32`](https://github.com/siderolabs/pulumi-provider-talos/commit/2f44d3277f2563d42f12f2d4df5ed92afe6339be) feat: add NodeBootstrap resource
* [`1e37daf`](https://github.com/siderolabs/pulumi-provider-talos/commit/1e37daf3e01bfc630853a6e0ca2246e1d4d0140b) feat: add ClusterConfig and ClusterSecrets resources
* [`8300bfa`](https://github.com/siderolabs/pulumi-provider-talos/commit/8300bfa1ea9a42e2bd9748a4ccf8d36d7af7ec54) feat: secretsBundle Create() works
* [`67b66fe`](https://github.com/siderolabs/pulumi-provider-talos/commit/67b66fec94a93bd507d06aa4d8dc1f4452c1376b) chore: first pass
* [`ecf31c0`](https://github.com/siderolabs/pulumi-provider-talos/commit/ecf31c085e9e912837e66940f80f30b23b2a0339) Initial commit
</p>
</details>

### Dependency Changes

This release has no dependency changes

## [pulumi-provider-talos 0.1.0-alpha.0](https://github.com/siderolabs/pulumi-provider-talos/releases/tag/v0.1.0-alpha.0) (2022-06-04)

Welcome to the v0.1.0-alpha.0 release of pulumi-provider-talos!



Please try out the release binaries and report any issues at
https://github.com/siderolabs/pulumi-provider-talos/issues.

### Contributors

* Noel Georgi
* Spencer Smith
* Spencer Smith

### Changes
<details><summary>24 commits</summary>
<p>

* [`2073e17`](https://github.com/siderolabs/pulumi-provider-talos/commit/2073e17399a756a69d32a7602d5ca1ba022f5e13) feat: build multiple architectures
* [`811dfa6`](https://github.com/siderolabs/pulumi-provider-talos/commit/811dfa6d2d3a9460da9f2a77dd07b3e8c97202ca) feat: add further CI functionality
* [`bfc411f`](https://github.com/siderolabs/pulumi-provider-talos/commit/bfc411f8abe0ad80d13c2f418fa0c632071a531a) feat: add CI testing
* [`03f43ea`](https://github.com/siderolabs/pulumi-provider-talos/commit/03f43ea60bc54847e21e9c2518b6fb6cea4d4d0d) fix: update all frezbo refs to siderolabs
* [`e11dd36`](https://github.com/siderolabs/pulumi-provider-talos/commit/e11dd361ccdffcee14b327c44fa62020a24f30f6) chore: support applying config
* [`6e068b0`](https://github.com/siderolabs/pulumi-provider-talos/commit/6e068b030b37814c3d96bccb1e35d1f487c06c06) Merge pull request  [#1](https://github.com/siderolabs/pulumi-provider-talos/pull/1) from rsmitty/main
* [`bdd1e8d`](https://github.com/siderolabs/pulumi-provider-talos/commit/bdd1e8dd95e136ce011acfcb897faf331760db28) fix: ensure additional sans are processed correctly
* [`ee48675`](https://github.com/siderolabs/pulumi-provider-talos/commit/ee4867569269e4376aefd6cf227e7ff8a34dae90) chore: bump talos to v1.0.0-beta.2
* [`d9ceba5`](https://github.com/siderolabs/pulumi-provider-talos/commit/d9ceba523c250e72cc6e472af69bb7773cf9b191) chore: update example
* [`08fd1fd`](https://github.com/siderolabs/pulumi-provider-talos/commit/08fd1fd91e659e8321199d527ae064ff3a0df831) chore: update to go 1.18
* [`09edb09`](https://github.com/siderolabs/pulumi-provider-talos/commit/09edb09055a7bad12b86f4f1624dede410aba064) chore: mark outputs as secrets
* [`cf613aa`](https://github.com/siderolabs/pulumi-provider-talos/commit/cf613aaaabdd2017aba892ed0c84eecf19ccfab3) chore: use talos/machinery from latest
* [`6642479`](https://github.com/siderolabs/pulumi-provider-talos/commit/6642479878e313e89ced2725b2c0343ce78af6dc) feat: add GetKubeConfig resource
* [`09771e3`](https://github.com/siderolabs/pulumi-provider-talos/commit/09771e3d4c0f974462b39ce65b0a0ee0cdea2c56) fix: bootstrap timeout handling
* [`836f66b`](https://github.com/siderolabs/pulumi-provider-talos/commit/836f66bd6510b0819e7b23ebf1c6d65452f8b6e8) fix: bootstrap timeout
* [`941d8f5`](https://github.com/siderolabs/pulumi-provider-talos/commit/941d8f533d88b3a513885b9c87623ca50a33736c) feat: improve patch UX
* [`141d690`](https://github.com/siderolabs/pulumi-provider-talos/commit/141d690bdea26efc3524c1a6a41b1daea4584af5) fix: casting from pulumi map to int
* [`38a41ab`](https://github.com/siderolabs/pulumi-provider-talos/commit/38a41aba8500be93cf19362d0a0d1f323545ebcf) fix: bootstrap provider
* [`eda59ca`](https://github.com/siderolabs/pulumi-provider-talos/commit/eda59cae9770f12c544c0c11f2422a6346b1208f) chore: use fork to fix grpc error
* [`2f44d32`](https://github.com/siderolabs/pulumi-provider-talos/commit/2f44d3277f2563d42f12f2d4df5ed92afe6339be) feat: add NodeBootstrap resource
* [`1e37daf`](https://github.com/siderolabs/pulumi-provider-talos/commit/1e37daf3e01bfc630853a6e0ca2246e1d4d0140b) feat: add ClusterConfig and ClusterSecrets resources
* [`8300bfa`](https://github.com/siderolabs/pulumi-provider-talos/commit/8300bfa1ea9a42e2bd9748a4ccf8d36d7af7ec54) feat: secretsBundle Create() works
* [`67b66fe`](https://github.com/siderolabs/pulumi-provider-talos/commit/67b66fec94a93bd507d06aa4d8dc1f4452c1376b) chore: first pass
* [`ecf31c0`](https://github.com/siderolabs/pulumi-provider-talos/commit/ecf31c085e9e912837e66940f80f30b23b2a0339) Initial commit
</p>
</details>

### Dependency Changes

This release has no dependency changes

