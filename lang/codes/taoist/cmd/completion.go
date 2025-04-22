// 自动补全
// 依赖: sudo apt-get install bash-completion
// cat echo "
// # 确保 bash-completion 文件存在并加载
// if [ -f /etc/bash_completion ]; then
// . /etc/bash_completion
// elif [ -f /usr/local/etc/bash_completion ]; then
// . /usr/local/etc/bash_completion
// fi
// " >> ~/.bashrc

package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

var completionCmd = &cobra.Command{
	Use:   "completion [bash|zsh]",
	Short: "Generate the autocompletion script for the specified shell",
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		switch args[0] {
		case "bash":
			cmd.Root().GenBashCompletion(os.Stdout)
		case "zsh":
			cmd.Root().GenZshCompletion(os.Stdout)
		default:
			cmd.Println("不支持的 shell 类型")
		}
	},
}

func init() {
	rootCmd.AddCommand(completionCmd)
}
