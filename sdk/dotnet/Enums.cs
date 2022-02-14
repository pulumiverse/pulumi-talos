// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.Talos
{
    [EnumType]
    public readonly struct TalosMachineConfigVersion : IEquatable<TalosMachineConfigVersion>
    {
        private readonly string _value;

        private TalosMachineConfigVersion(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        /// <summary>
        /// Talos Machine Configuration Version
        /// </summary>
        public static TalosMachineConfigVersion V1alpha1 { get; } = new TalosMachineConfigVersion("v1alpha1");

        public static bool operator ==(TalosMachineConfigVersion left, TalosMachineConfigVersion right) => left.Equals(right);
        public static bool operator !=(TalosMachineConfigVersion left, TalosMachineConfigVersion right) => !left.Equals(right);

        public static explicit operator string(TalosMachineConfigVersion value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is TalosMachineConfigVersion other && Equals(other);
        public bool Equals(TalosMachineConfigVersion other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
