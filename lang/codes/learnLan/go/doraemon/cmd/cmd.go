package cmd

import (
	"log"
	"net/http"
	"os"

	"sunflower/config"
	"sunflower/db"
	"sunflower/model"
	"sunflower/router"

	"github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var (
	cfgFile string
	logger  = &logrus.Logger{}
	rootCmd = &cobra.Command{}
)

func initConfig() {
	config.MustInit(os.Stdout, cfgFile)
}

func init() {
	cobra.OnInitialize(initConfig)
	rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "config\\dev.yaml", "config file (default is $HOME\\.cobra.yaml)")
	rootCmd.PersistentFlags().Bool("debug", true, "开启debug")
	viper.SetDefault("gin.mode", rootCmd.PersistentFlags().Lookup("debug"))
}

// Execute is a fucntion to execute in main.
func Execute() error {
	rootCmd.RunE = func(cmd *cobra.Command, args []string) error {
		_, err := db.Mysql(
			viper.GetString("db.hostname"),
			viper.GetString("db.username"),
			viper.GetString("db.password"),
			viper.GetString("db.dbname"),
			viper.GetInt("db.port"),
		)
		if err != nil {
			return err
		}

		db.DB.AutoMigrate(&model.User{})

		r := router.SetupRouter()
		r.Run()

		port := viper.GetString("port")
		log.Println("port = *** =", port)
		return http.ListenAndServe(port, nil) // listen and serve
	}

	return rootCmd.Execute()
}
