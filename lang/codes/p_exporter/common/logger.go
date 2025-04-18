package common

import (
	"github.com/go-kit/log"
	"github.com/prometheus/common/promlog"
)

var Logger log.Logger

func init() {
	Logger = logger()
}

func logger() log.Logger {
	promlogConfig := &promlog.Config{}

	log := promlog.New(promlogConfig)
	return log
}
