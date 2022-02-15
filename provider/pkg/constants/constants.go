package constants

import "time"

const (
	TalosMachineConfigVersion = "v1alpha1"
	TalosInstallDisk          = "/dev/sda"
	TalosInstallImageVersion  = "v0.14.2"
	TalosPersistConfig        = true
	TalosClusterDiscovery     = true
	TalosConfigDocs           = true
	TalosConfigExamples       = true
)

// Talos bootstrap resource constants
const (
	TalosBootstrapResourceDelayBetweenRetries    = 10 * time.Second
	TalosBootstrapResourceMaxDelayBetweenRetries = 60 * time.Second
	TalosBootstrapResourceTimeout                = 600
)
