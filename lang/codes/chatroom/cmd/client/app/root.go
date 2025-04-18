package app

import (
	"os"
	"log/slog"

	"chatroom/pkg/client"
	"chatroom/pkg/utils"

	"github.com/spf13/cobra"
)

var config string

var rootCmd = &cobra.Command{
	Use:   "chatclient",
	Short: "chatclient 使用信息",
	Long:  "chatclient 是一个简单聊天室服务器程序的客户端,用于测试chatroot.",
	Run: func(cmd *cobra.Command, args []string) {
		if config == "" {
			slog.Error("运行: chatclient --help")
			return
		}
		utils.LoadConfig(config)
		client := client.NewChatClient()
		client.Run()
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
