package app

import (
	"os"
	"log/slog"

	"chatroom/pkg/server"
	"chatroom/pkg/utils"

	"github.com/spf13/cobra"
)

var config string

var rootCmd = &cobra.Command{
	Use:   "chatroom",
	Short: "chatroom 使用信息",
	Long:  "chatroom 是一个简单的聊天室服务器程序支持多人进行聊天.",
	Run: func(cmd *cobra.Command, args []string) {
		if config == "" {
			slog.Error("运行: chatroot --help")
			return
		}
		utils.LoadConfig(config)
		server := server.NewChatServer()
		server.Run()
	},
}

func init() {
	rootCmd.PersistentFlags().StringVarP(&config, "config", "c", "", "config file name")
}

func Excute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}
