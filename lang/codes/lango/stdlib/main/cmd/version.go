package main

import (
	"cmdline"
	"flag"
	"fmt"
)

var version = "0.0.1"

var versionCmd = &cmdline.Command{
	Name:  "version",
	Desc:  "print this app version",
	Flags: flag.NewFlagSet("version", flag.ContinueOnError),
	Run: func(args []string) {
		fmt.Println("version: ", version)
	},
}
