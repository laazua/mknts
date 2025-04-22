package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var (
        Vv string
        verison = "3.12.0"
)

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "show verison",
	Long:  "子命令version的描述信息.",
	Run: func(cmd *cobra.Command, args []string) {
                fmt.Println(Vv)
		fmt.Println(verison)
	},
}

func init() {
	rootCmd.AddCommand(versionCmd)
        versionCmd.PersistentFlags().StringVarP(&Vv, "vv", "", "", "")
}
