package cli

import (
	"flag"
	"fmt"
	"io"
	"os"
	"strings"
	"time"
)

// ==================== 接口定义 ====================

// Command 命令接口
type Command interface {
	// 基本信息
	Name() string
	Description() string

	// 命令配置（初始化标志等）
	Configure(*CommandConfig)

	// 命令执行
	Run(Context) error

	// 帮助信息（可选实现）
	Help() string
}

// Context 执行上下文
type Context struct {
	Args   []string       // 非标志参数
	Stdout io.Writer      // 标准输出
	Stderr io.Writer      // 标准错误输出
	Flags  *flag.FlagSet  // 解析后的标志集
	Data   map[string]any // 额外数据存储
}

// CommandConfig 命令配置
type CommandConfig struct {
	Flags *flag.FlagSet
	Usage string
}

// ==================== 基础命令实现 ====================

// BaseCommand 提供基础功能的命令
type BaseCommand struct {
	name        string
	description string
	config      *CommandConfig
	flagValues  map[string]any // 存储标志指针
}

// NewBaseCommand 创建基础命令
func NewBaseCommand(name, description string) *BaseCommand {
	return &BaseCommand{
		name:        name,
		description: description,
		flagValues:  make(map[string]any),
	}
}

// Name 返回命令名称
func (b *BaseCommand) Name() string {
	return b.name
}

// Description 返回命令描述
func (b *BaseCommand) Description() string {
	return b.description
}

// Configure 配置命令
func (b *BaseCommand) Configure(cfg *CommandConfig) {
	b.config = cfg
}

// Run 默认运行方法（子类应覆盖）
func (b *BaseCommand) Run(ctx Context) error {
	return fmt.Errorf("command '%s' not implemented", b.name)
}

// Help 生成帮助信息
func (b *BaseCommand) Help() string {
	if b.config == nil || b.config.Flags == nil {
		return fmt.Sprintf("%s: %s", b.name, b.description)
	}

	var help strings.Builder
	help.WriteString(fmt.Sprintf("命令: %s\n\n", b.name))
	help.WriteString(fmt.Sprintf("描述: %s\n\n", b.description))

	if b.config.Usage != "" {
		help.WriteString("用法:\n")
		help.WriteString("  " + b.config.Usage + "\n\n")
	}

	help.WriteString("选项:\n")
	b.config.Flags.VisitAll(func(f *flag.Flag) {
		defaultValue := f.DefValue
		if defaultValue == "" {
			defaultValue = "<空>"
		}
		help.WriteString(fmt.Sprintf("  -%-15s %s (默认值: %v)\n", f.Name, f.Usage, defaultValue))
	})

	help.WriteString("\n示例:\n")
	help.WriteString(fmt.Sprintf("  camassh %s [选项] [参数]\n", b.name))

	return help.String()
}

// ==================== 标志操作辅助方法 ====================

// StringFlag 添加字符串标志
func (b *BaseCommand) StringFlag(name, defaultValue, description string) *string {
	if b.config == nil || b.config.Flags == nil {
		panic("command not configured")
	}
	ptr := b.config.Flags.String(name, defaultValue, description)
	b.flagValues[name] = ptr
	return ptr
}

// IntFlag 添加整数标志
func (b *BaseCommand) IntFlag(name string, defaultValue int, description string) *int {
	if b.config == nil || b.config.Flags == nil {
		panic("command not configured")
	}
	ptr := b.config.Flags.Int(name, defaultValue, description)
	b.flagValues[name] = ptr
	return ptr
}

// BoolFlag 添加布尔标志
func (b *BaseCommand) BoolFlag(name string, defaultValue bool, description string) *bool {
	if b.config == nil || b.config.Flags == nil {
		panic("command not configured")
	}
	ptr := b.config.Flags.Bool(name, defaultValue, description)
	b.flagValues[name] = ptr
	return ptr
}

// DurationFlag 添加时长标志
func (b *BaseCommand) DurationFlag(name string, defaultValue time.Duration, description string) *time.Duration {
	if b.config == nil || b.config.Flags == nil {
		panic("command not configured")
	}
	ptr := b.config.Flags.Duration(name, defaultValue, description)
	b.flagValues[name] = ptr
	return ptr
}

// Float64Flag 添加浮点数标志
func (b *BaseCommand) Float64Flag(name string, defaultValue float64, description string) *float64 {
	if b.config == nil || b.config.Flags == nil {
		panic("command not configured")
	}
	ptr := b.config.Flags.Float64(name, defaultValue, description)
	b.flagValues[name] = ptr
	return ptr
}

// RequiredFlag 验证必需的标志（在Run方法中使用）
func (b *BaseCommand) RequiredFlag(name string) error {
	if b.config == nil || b.config.Flags == nil {
		return fmt.Errorf("command not configured")
	}

	value := b.flagValues[name]
	if value == nil {
		return fmt.Errorf("flag %s not found", name)
	}

	// 根据类型检查
	switch v := value.(type) {
	case *string:
		if *v == "" {
			return fmt.Errorf("flag --%s is required", name)
		}
	case *int:
		if *v == 0 {
			// 注意：0可能是有效值，这里只是示例
			// 可以根据具体需求调整验证逻辑
		}
	}

	return nil
}

// GetFlag 获取标志值
func (b *BaseCommand) GetFlag(name string) any {
	return b.flagValues[name]
}

// ==================== 其他辅助函数 ====================

// NewContext 创建执行上下文
func NewContext(args []string, flags *flag.FlagSet) Context {
	return Context{
		Args:   args,
		Stdout: os.Stdout,
		Stderr: os.Stderr,
		Flags:  flags,
		Data:   make(map[string]any),
	}
}

// NewCommandConfig 创建命令配置
func NewCommandConfig(name string) *CommandConfig {
	fs := flag.NewFlagSet(name, flag.ContinueOnError)
	fs.Usage = func() {} // 禁用默认的Usage

	return &CommandConfig{
		Flags: fs,
	}
}

// SetUsage 设置命令用法
func (c *CommandConfig) SetUsage(usage string) {
	c.Usage = usage
}

// PrintHelp 打印帮助信息
func PrintHelp(cmd Command, w io.Writer) {
	if helper, ok := cmd.(interface{ Help() string }); ok {
		fmt.Fprintln(w, helper.Help())
	} else {
		fmt.Fprintf(w, "%s: %s\n", cmd.Name(), cmd.Description())
	}
}
