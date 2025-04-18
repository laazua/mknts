package config

import (
	"os"

	"gopkg.in/yaml.v3"
)

type Config struct {
	Address      string `yaml:"address"`
	SecuKey      string `yaml:"secuKey"`
	RunMode      string `yaml:"runMode"`
	TokenSign    string `yaml:"tokenSign"`
	TokenExpored uint   `yaml:"tokenExpored"`
	V2Address    string `yaml:"v2Address"`

	DbHost string `yaml:"dbHost"`
	DbPort uint   `yaml:"dbPort"`
	DbUser string `yaml:"dbUser"`
	DbPass string `yaml:"dbPass"`
	DbName string `yaml:"dbName"`
}

func LoadConfig(filepath string) (*Config, error) {
	data, err := os.ReadFile(filepath)
	if err != nil {
		return nil, err
	}

	var config Config
	if err := yaml.Unmarshal(data, &config); err != nil {
		return nil, err
	}

	return &config, nil
}
