package core

import (
	"fmt"
	"os"

	"gopkg.in/yaml.v3"
)

var Setting config

type config struct {
	// gokins配置
	Address        string `yaml:"address"`
	TaskPath       string `yaml:"taskPath"`
	SaltKey        string `yaml:"saltKey"`
	SecurityKey    string `yaml:"securityKey"`
	SignExpireTime int    `yaml:"signExpireTime"`

	// 数据库配置
	DbPort        string `yaml:"dbPort"`
	DbHost        string `yaml:"dbHost"`
	DbUser        string `yaml:"dbUser"`
	DbPass        string `yaml:"dbPass"`
	DbName        string `yaml:"dbName"`
	DbConNum      int32  `yaml:"dbConNum"`
	DbConIdleTime uint   `yaml:"dbConIdleTime"`
}

func init() {
	content, err := os.ReadFile("./gokins.yml")
	if err != nil {
		panic(fmt.Sprintf("## 读取gokins.yml配置文件失败: %v", err))
	}
	err = yaml.Unmarshal(content, &Setting)
	if err != nil {
		panic(fmt.Sprintf("## 解析gokins.yml配置文件失败: %v", err))
	}
}
