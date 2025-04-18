package cmd

import "github.com/spf13/cobra"

var (
	cdcfg string
	cdCmd = &cobra.Command{
		Use:   "cd",
		Short: "cd is a subcommand to cd job",
		Run:   func(cmd *cobra.Command, args []string) {},
	}
)

func init() {
	rootCmd.AddCommand(cdCmd)
	cdCmd.PersistentFlags().StringVar(&cdcfg, "config", "", "cd job yaml file")
}
