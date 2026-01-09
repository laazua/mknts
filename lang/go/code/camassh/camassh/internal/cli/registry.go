package cli

import (
	"flag"
	"fmt"
	"os"
	"sort"
	"strings"
)

// Registry 命令注册表
type Registry struct {
	name     string
	version  string
	commands map[string]Command
	helpText string
}

// NewRegistry 创建新的命令注册表
func NewRegistry(name, version string) *Registry {
	return &Registry{
		name:     name,
		version:  version,
		commands: make(map[string]Command),
		helpText: "A command-line application",
	}
}

// Register 注册命令
func (r *Registry) Register(cmds ...Command) {
	if cmds == nil {
		panic("cannot register nil command")
	}
	for _, cmd := range cmds {
		name := cmd.Name()
		if _, exists := r.commands[name]; exists {
			panic(fmt.Sprintf("command '%s' already registered", name))
		}
		r.commands[name] = cmd

	}
}

// Run 运行命令
func (r *Registry) Run() {
	if len(os.Args) < 2 {
		r.printGlobalHelp()
		os.Exit(1)
	}

	cmdName := os.Args[1]

	// 特殊命令处理
	if cmdName == "help" {
		if len(os.Args) > 2 {
			r.printCommandHelp(os.Args[2])
		} else {
			r.printGlobalHelp()
		}
		return
	}

	if cmdName == "--version" || cmdName == "-v" {
		r.printVersion()
		return
	}

	cmd, exists := r.commands[cmdName]
	if !exists {
		fmt.Fprintf(os.Stderr, "错误: 未知命令 '%s'\n\n", cmdName)
		r.printGlobalHelp()
		os.Exit(1)
	}

	// 创建命令配置
	config := NewCommandConfig(cmdName)
	cmd.Configure(config)

	// 解析命令行参数
	if err := config.Flags.Parse(os.Args[2:]); err != nil {
		if err == flag.ErrHelp {
			PrintHelp(cmd, os.Stdout)
			os.Exit(0)
		}
		fmt.Fprintf(os.Stderr, "参数解析错误: %v\n\n", err)
		PrintHelp(cmd, os.Stderr)
		os.Exit(1)
	}

	// 创建执行上下文
	ctx := NewContext(config.Flags.Args(), config.Flags)

	// 执行命令
	if err := cmd.Run(ctx); err != nil {
		fmt.Fprintf(os.Stderr, "执行错误: %v\n", err)
		os.Exit(1)
	}
}

// SetHelpText 设置全局帮助文本
func (r *Registry) SetHelpText(text string) {
	r.helpText = text
}

// printGlobalHelp 打印全局帮助
func (r *Registry) printGlobalHelp() {
	fmt.Fprintf(os.Stderr, "%s v%s\n\n", r.name, r.version)
	fmt.Fprintf(os.Stderr, "%s\n\n", r.helpText)
	fmt.Fprintf(os.Stderr, "用法: %s <命令> [参数]\n\n", r.name)

	// 收集并排序命令名称
	var names []string
	for name := range r.commands {
		names = append(names, name)
	}
	sort.Strings(names)

	// 计算最大名称长度用于对齐
	maxLen := 0
	for _, name := range names {
		if len(name) > maxLen {
			maxLen = len(name)
		}
	}

	fmt.Fprintf(os.Stderr, "可用命令:\n")
	for _, name := range names {
		cmd := r.commands[name]
		padding := strings.Repeat(" ", maxLen-len(name))
		fmt.Fprintf(os.Stderr, "  %s%s  %s\n", name, padding, cmd.Description())
	}

	fmt.Fprintf(os.Stderr, "\n特殊命令:\n")
	fmt.Fprintf(os.Stderr, "  help    显示帮助信息\n")
	fmt.Fprintf(os.Stderr, "  version 显示版本信息\n")

	fmt.Fprintf(os.Stderr, "\n使用 '%s help <命令>' 查看具体命令帮助\n", r.name)
}

// printCommandHelp 打印具体命令帮助
func (r *Registry) printCommandHelp(cmdName string) {
	cmd, exists := r.commands[cmdName]
	if !exists {
		fmt.Fprintf(os.Stderr, "错误: 未知命令 '%s'\n", cmdName)
		os.Exit(1)
	}

	PrintHelp(cmd, os.Stdout)
}

// printVersion 打印版本信息
func (r *Registry) printVersion() {
	fmt.Printf("%s v%s\n", r.name, r.version)
}
