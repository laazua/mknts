package cmd

import (
	"github.com/spf13/cobra"
)

var (
	cicfg string
	ciCmd = &cobra.Command{
		Use:   "ci",
		Short: "ci is a subcommand to ci job",
		Run:   func(cmd *cobra.Command, args []string) {},
	}
)

func init() {
	rootCmd.AddCommand(ciCmd)
	ciCmd.PersistentFlags().StringVar(&cicfg, "config", "", "ci job yaml file")
}
