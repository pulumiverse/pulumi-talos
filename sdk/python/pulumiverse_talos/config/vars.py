# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

import types

__config__ = pulumi.Config('talos')


class _ExportableConfig(types.ModuleType):
    @property
    def image_factory_url(self) -> Optional[str]:
        """
        The URL of Image Factory to generate schematics. If not set defaults to https://factory.talos.dev.
        """
        return __config__.get('imageFactoryUrl')

