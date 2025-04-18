package core

import (
	"os"

	"gopkg.in/yaml.v3"
)

type config struct {
	Address      string `yaml:"address"`
	RunMode      string `yaml:"run_mode"`
	JwtKey       string `yaml:"jwt_key"`
	SaltKey      string `yaml:"salt_key"`
	ExpiredTime  int64  `yaml:"expired_time"`
	TaskPoolSize int    `yaml:"task_pool_size"`
	WorkerCount  int    `yaml:"worker_count"`
	Strategy     string `yaml:"strategy"`
	DbHost       string `yaml:"db_host"`
	DbPort       uint   `yaml:"db_port"`
	DbUser       string `yaml:"db_user"`
	DbPass       string `yaml:"db_pass"`
	DbName       string `yaml:"db_name"`
	CodeUser     string `yaml:"code_user"`
	CodePass     string `yaml:"code_pass"`
	WorkSpace    string `yaml:"workspace"`
}

func init() {
	once.Do(func() {
		data, err := os.ReadFile("config.yaml")
		if err != nil {
			panic(err)
		}
		err = yaml.Unmarshal(data, &Config)
		if err != nil {
			panic(err)
		}
	})
}
