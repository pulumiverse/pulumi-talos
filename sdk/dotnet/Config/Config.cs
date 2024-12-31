// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumiverse.Talos
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("talos");

        private static readonly __Value<string?> _imageFactoryUrl = new __Value<string?>(() => __config.Get("imageFactoryUrl"));
        /// <summary>
        /// The URL of Image Factory to generate schematics. If not set defaults to https://factory.talos.dev.
        /// </summary>
        public static string? ImageFactoryUrl
        {
            get => _imageFactoryUrl.Get();
            set => _imageFactoryUrl.Set(value);
        }

    }
}