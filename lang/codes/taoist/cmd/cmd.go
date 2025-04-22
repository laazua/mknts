package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

var (
	module    string
	moduleArg string
)

var cmdCmd = &cobra.Command{
	Use:   "cmd",
	Short: "Run task at the command line.",
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) == 0 {
			cmd.Help()
			os.Exit(1)
		}
	},
	Example: `1. taoist cmd -m copy -a "src=a.txt, dst=b.txt"`,
}

func init() {
	rootCmd.AddCommand(cmdCmd)
	cmdCmd.PersistentFlags().StringVarP(&module, "module", "m", "", "module name")
	cmdCmd.PersistentFlags().StringVarP(&moduleArg, "moduleArg", "a", "", "module arg")
}
