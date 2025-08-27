package config

import (
	"os"
	"path/filepath"
	"sync"

	"gopkg.in/yaml.v3"
)

func init() {
	// 设置启动默认配置
	var err error
	if os.Getenv("LOG_PATH") == "" {
		err = os.Setenv("LOG_PATH", "./logs")
	}
	if os.Getenv("LOG_LEVEL") == "" {
		err = os.Setenv("LOG_LEVEL", "info")
	}
	if err != nil {
		os.Exit(0)
	}
}

var (
	repBot *RepBotCon
	once   sync.Once
)

// RepBotCon RepBot程序配置
type RepBotCon struct {
	Address    string `yaml:"address" default:"localhost"` // RepoBot服务监听地址
	DBHost     string `yaml:"dbHost" default:"127.0.0.1"`  // 数据库Host
	DBPort     int    `yaml:"dbPort" default:"5432"`       // 数据库端口
	DBName     string `yaml:"dbName" default:"repbot"`     // 数据库名
	DBUser     string `yaml:"dbUser" default:"root"`       // 数据库用户
	DBPass     string `yaml:"dbPass" default:"123456abc"`  // 数据库密码
	DBPool     int    `yaml:"dbPool" default:"10"`         // 数据库连接池
	DBIdle     int    `yaml:"dbIdle" default:"50"`         // 数据库idle
	DBLifeTime uint   `yaml:"dbLifeTime" default:"60"`     // 数据库连接时间
	LogPath    string `yaml:"logPath" default:"./logs"`
	LogFormat  string `yaml:"logFormat" default:"text"`
}

func InitConfig() error {
	fileName := filepath.Join(".", "config.yml")
	bytes, err := os.ReadFile(fileName)
	if err != nil {
		return err
	}
	// 从环境变量设置日志默认值
	repBot = &RepBotCon{
		LogPath:   os.Getenv("LOG_PATH"),
		LogFormat: os.Getenv("LOG_FORMAT"),
	}
	err = yaml.Unmarshal(bytes, &repBot)
	if err != nil {
		return err
	}
	return nil
}

// GetConfig 获取配置实例
func Get() *RepBotCon {
	if repBot == nil {
		once.Do(func() {
			err := InitConfig()
			if err != nil {
				panic(err)
			}
		})
	}
	return repBot
}
