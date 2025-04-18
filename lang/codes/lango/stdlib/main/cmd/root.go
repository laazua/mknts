package main

import (
	"cmdline"
	"flag"
	"fmt"
	"os"
)

var rootCmd = &cmdline.Command{
	Name:  "example",
	Desc:  "example of flag.FlagSet",
	Flags: flag.NewFlagSet("example", flag.ContinueOnError),
	Run: func(args []string) {
		if len(args) <= 0 {
			help()
		}
	},
}

func init() {
	// 添加 flags
	var version string
	rootCmd.Flags.StringVar(&version, "version", "0.0.1", "")

	// 加入子命令
	rootCmd.AddCmd(versionCmd)
}

func help() {
	fmt.Printf(`Usage of %s:
sub cmd:
	version    print version

flags:
	-h|--help    print help info
	-v|--version print version
`, os.Args[0])
}
