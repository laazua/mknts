package cmds

import (
	"runtime"

	"camassh/internal/cli"
)

type VersionCommand struct {
	*cli.BaseCommand
	version string
	build   string
	date    string
}

func NewVersionCommand(version, build, date string) cli.Command {
	cmd := &VersionCommand{
		BaseCommand: cli.NewBaseCommand("version", "显示版本信息"),
		version:     version,
		build:       build,
		date:        date,
	}
	return cmd
}

func (v *VersionCommand) Configure(cfg *cli.CommandConfig) {
	v.BaseCommand.Configure(cfg)
	cfg.SetUsage("myapp version")

	v.BoolFlag("short", false, "简洁输出")
	v.BoolFlag("verbose", false, "详细信息")
}

func (v *VersionCommand) Help() string {
	helpText := v.BaseCommand.Help()
	extraHelp := "\n示例:\n" +
		"  camassh version\n" +
		"  camassh version --short\n" +
		"  camassh version --verbose\n"
	return helpText + extraHelp
}

func (v *VersionCommand) Run(ctx cli.Context) error {
	shortPtr := v.GetFlag("short").(*bool)
	verbosePtr := v.GetFlag("verbose").(*bool)

	if *shortPtr {
		ctx.Printf("%s\n", v.version)
		return nil
	}

	ctx.Printf("版本:    %s\n", v.version)
	ctx.Printf("构建:    %s\n", v.build)
	ctx.Printf("日期:    %s\n", v.date)

	if *verbosePtr {
		ctx.Printf("Go版本:  %s\n", runtime.Version())
		ctx.Printf("编译器:  %s\n", runtime.Compiler)
		ctx.Printf("操作系统:%s/%s\n", runtime.GOOS, runtime.GOARCH)
	}

	return nil
}
