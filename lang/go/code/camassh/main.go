package main

import (
	"camassh/internal/cli"
	"camassh/internal/cli/cmds"
)

const appName = "camassh"
const appVersion = "1.0.0"

func main() {
	// fmt.Println("CA Host: ", config.Get().CA().Host())
	// fmt.Println("CA Path: ", config.Get().CA().Path())
	// fmt.Println("CA Nets: ", config.Get().CA().Nets())

	registry := cli.NewRegistry(appName, appVersion)
	registry.SetHelpText("一个用于设置ssh ca 证书管理的命令行工具")

	registry.Register(
		cmds.NewVersionCommand(appVersion, "build-20260108", "2026-01-08 17:23:00"),
		cmds.NewInitCommand(),
	)

	registry.Run()
}
