package cmd

import (
	"os"

	"github.com/mitchellh/go-homedir"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var (
	cfgFile = "../king.yaml"
	rootCmd = &cobra.Command{
		Use:   "King",
		Short: "ci/cd",
		Long:  `King is a cli ci/cd tool`,
		Run: func(cmd *cobra.Command, args []string) {

		},
		Example:           "King ci --config test.yaml",
		CompletionOptions: cobra.CompletionOptions{HiddenDefaultCmd: true},
	}
)

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		os.Exit(1)
	}
}

func init() {
	cobra.OnFinalize(initConfig)
	rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "king.yaml", "king's config file")
	viper.BindPFlag("config", rootCmd.PersistentFlags().Lookup("config"))
}

func initConfig() {
	if cfgFile != "" {
		viper.SetConfigFile(cfgFile)
	} else {
		home, err := homedir.Dir()
		if err != nil {
			os.Exit(1)
		}
		viper.AddConfigPath(home)
		viper.SetConfigName(".cobra")
	}
	if err := viper.ReadInConfig(); err != nil {
		os.Exit(1)
	}
}
