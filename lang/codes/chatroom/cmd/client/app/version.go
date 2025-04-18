package app

import (
	"fmt"

	"github.com/spf13/cobra"
)

var description = "程序chatclient的当前版本为: 0.0.1"

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "显示版本信息",
	Long:  "version 子命令用于显示当前程序的版本信息",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println(description)
	},
}

func init() {
	rootCmd.AddCommand(versionCmd)
}
