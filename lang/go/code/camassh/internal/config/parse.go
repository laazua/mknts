package config

import (
	"os"
	"sync"

	"go.yaml.in/yaml/v3"
)

// 1. 定义配置结构
type config struct {
	ca      ca
	bastion bastion
}

type ca struct {
	host    string
	path    string
	logPath string
	nets    []string
}

type bastion struct {
	host string
}

var (
	cfg  *config
	once sync.Once
	err  error
)

// 2. 定义用于解析的原始结构
var raw struct {
	CA struct {
		Host    string   `yaml:"host"`
		Path    string   `yaml:"path"`
		LogPath string   `yaml:"log_path"`
		Nets    []string `yaml:"nets"`
	} `yaml:"ca"`
	Bastion struct {
		Host string `yaml:"host"`
	} `yaml:"bastion"`
}

func load() {
	cfg = &config{}

	data, e := os.ReadFile("config.yaml")
	if e != nil {
		err = e
		return
	}

	if err = yaml.Unmarshal(data, &raw); err != nil {
		err = e
		return
	}

	// 3. 赋值到配置结构体
	cfg.ca = ca{
		host:    raw.CA.Host,
		path:    raw.CA.Path,
		logPath: raw.CA.LogPath,
		nets:    raw.CA.Nets,
	}
	cfg.bastion = bastion{
		host: raw.Bastion.Host,
	}
}

func Get() *Reader {
	once.Do(load)
	return &Reader{}
}

func init() {
	if err := Get().Err(); err != nil {
		panic("加载配置失败: " + err.Error())
	}
}
