package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var (
	Aa string
	Bb string
)

var rootCmd = &cobra.Command{
	Use:   "clitest",
	Short: "cli command test.",
	Long:  "cli command 程序的描述信息.",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("xxx")
	},
}

func init() {
	rootCmd.PersistentFlags().StringVarP(&Aa, "aa", "", "", "")
	rootCmd.PersistentFlags().StringVarP(&Bb, "bb", "", "", "")
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}
