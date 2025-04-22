package cmd

import (
	"os"

	"github.com/spf13/cobra"
)

var (
	jobFile   string
	extraVars string
)

var taskCmd = &cobra.Command{
	Use:   "task",
	Short: "Run task on the playbook line.",
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) == 0 {
			cmd.Help()
			os.Exit(1)
		}
	},
	Example: `1. taoist task -j task.yaml`,
}

func init() {
	rootCmd.AddCommand(taskCmd)
	taskCmd.PersistentFlags().StringVarP(&jobFile, "jobFile", "j", "", "job file of task")
	taskCmd.PersistentFlags().StringVarP(&extraVars, "extraVars", "e", "", "extra value of cli")
}
