package utils

import (
	"testing"
)

func TestLoadConfig(t *testing.T) {
	LoadConfig("../../config/server.yaml")
	LoadConfig("../../config/client.yaml")
}
