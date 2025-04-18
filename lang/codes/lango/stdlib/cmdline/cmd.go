package cmdline

import "flag"

type Command struct {
	Name    string
	Desc    string
	Flags   *flag.FlagSet
	Run     func(args []string)
	SubCmds []*Command
}

func (cmd *Command) Execute(args []string) {
	// 处理子命令
	if len(args) > 0 {
		for _, subCmd := range cmd.SubCmds {
			subCmd.Execute(args[1:])
			return
		}
	}
	// 处理标志
	cmd.Flags.Parse(args)
	// 执行命令的运行函数
	cmd.Run(cmd.Flags.Args())
}

func (cmd *Command) AddCmd(command *Command) {
	cmd.SubCmds = append(cmd.SubCmds, command)
}
