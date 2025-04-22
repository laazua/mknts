package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var ISettings map[string]any

var (
	cfg       string // config file
	inventory string
	user      string
	password  string
	port      int
	section   string
)

var (
	configInstance    *viper.Viper
	inventoryInstance *viper.Viper
)

var rootCmd = &cobra.Command{
	Use: "taoist",
	Long: `Taoist is inspired by ansible.
It is an open source tool for managing and deploying applications.
For more help,please run: taoist --help.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println(configInstance.GetString("rasKeyFile"))
	},
	Example: `1. taoist help
2. taoist -s web cmd -m ping
3. taoist -s web task -j task.yaml`,
	Version: "v0.0.1",
}

func init() {
	cobra.OnInitialize(initConfig, initInventory)
	// add root flag of inventory file, format like ini
	rootCmd.PersistentFlags().StringVarP(&cfg, "config", "f", "./taoist.yaml", "config file")
	rootCmd.PersistentFlags().StringVarP(&inventory, "inventory", "i", "./hosts", "inventory file")
	rootCmd.PersistentFlags().StringVarP(&section, "section", "s", "", "the section of inventory or specific IP")
	rootCmd.PersistentFlags().StringVarP(&user, "user", "u", "", "ssh user")
	rootCmd.PersistentFlags().StringVarP(&password, "password", "p", "", "ssh password")
	rootCmd.PersistentFlags().IntVarP(&port, "port", "P", 22, "ssh port")
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println("root cmd execute error: ", err)
		os.Exit(1)
	}
}

func initConfig() {
	configInstance = viper.New()
	var configFiles = []string{cfg, "./taoist.yaml", "/etc/taoist/taoist.yaml"}
	var configFile string
	for _, configFile = range configFiles {
		if !fileExists(configFile) {
			continue
		} else {
			break
		}
	}
	configInstance.SetConfigFile(configFile)
	if err := configInstance.ReadInConfig(); err != nil {
		fmt.Println("Please Set Config File")
		os.Exit(1)
	}
}

func initInventory() {
	inventoryInstance = viper.New()
	var inventoryFiles = []string{inventory, "./hosts", "/etc/taoist/hosts"}
	var inventoryFile string
	for _, inventoryFile = range inventoryFiles {
		if !fileExists(inventoryFile) {
			continue
		} else {
			break
		}
	}
	inventoryInstance.SetConfigFile(inventoryFile)
	inventoryInstance.SetConfigType("ini")
	if err := inventoryInstance.ReadInConfig(); err != nil {
		rootCmd.Help()
		os.Exit(1)
	}

	ISettings = inventoryInstance.AllSettings()
	fmt.Println(inventoryInstance.AllKeys())

}

func fileExists(filename string) bool {
	// 使用 os.Stat 检查文件信息
	_, err := os.Stat(filename)
	if os.IsNotExist(err) {
		return false // 文件不存在
	}
	return err == nil // 如果没有错误，文件存在
}
