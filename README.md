# Talos Resource Provider

The Talos Resource Provider lets you manage [Talos Linux](https://talos.dev) machines & clusters.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumiverse/talos
```

or `yarn`:

```bash
yarn add @pulumiverse/talos
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumiverse_talos
```
If you see an error as such.
```
import pulumiverse_talos
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/venv/lib/python3.12/site-packages/pulumiverse_talos/__init__.py", line 5, in <module>
    from . import _utilities
  File "/venv/lib/python3.12/site-packages/pulumiverse_talos/_utilities.py", line 11, in <module>
    import pkg_resources
ModuleNotFoundError: No module named 'pkg_resources'
```
Try installing
```
pip install setuptools
```
If you're using a Python Virtual Env
```
python3 -m venv venv
source venv/bin/activate
pip install setuptools
pip install pulumiverse_talos
# Test if the import works
python -c "import pulumiverse_talos"
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/pulumiverse/pulumi-talos/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumiverse.Talos
```

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/talos/api-docs/).
