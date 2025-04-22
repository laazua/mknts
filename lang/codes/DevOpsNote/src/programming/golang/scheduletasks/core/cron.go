package core

import "github.com/robfig/cron/v3"

func init() {
	go Cron.Run()
}

var Cron = cron.New()
