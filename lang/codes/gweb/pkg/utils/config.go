package utils

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"time"
)

var Setting *AppConfig

// 基础配置字段
type AppCon struct {
	// app1,app2都有的字段
	Ip       string
	Port     int
	ConfPath string
	KeyWord  string

	// app1有的字段
	RemotePort   int
	RunMode      string
	ReadTimeout  time.Duration
	WriteTimeout time.Duration

	// app2有的字段
	ZonePath string
	BinPath  string
}

// mysql配置字段(app1)
type MysqlCon struct {
	Host     string
	Port     int
	Dbname   string
	Username string
	Password string
}

// svn配置的字段(app2)
type SvnCon struct {
	Url      string
	Username string
	Password string
}

type AppConfig struct {
	App   AppCon
	Mysql MysqlCon
	Svn   SvnCon
}

func (con *AppConfig) MapJson() {
	if _, err := os.Stat(con.App.ConfPath); err != nil {
		panic(err)
	}
	if data, err := ioutil.ReadFile(con.App.ConfPath); err != nil {
		panic(err)
	} else {
		err = json.Unmarshal(data, con)
		if err != nil {
			panic(err)
		}
	}
}

func LoadCon(name string) {
	os.Chdir("../../")
	pwd, err := os.Getwd()
	if err != nil {
		pwd = "."
	}
	switch name {
	case "app1":
		Setting = &AppConfig{
			App: AppCon{
				Ip:           "127.0.0.1",
				Port:         8888,
				ConfPath:     pwd + "/conf/app1.json",
				ReadTimeout:  10,
				WriteTimeout: 10,
			},
		}
		Setting.MapJson()
	case "app2":
		Setting = &AppConfig{
			App: AppCon{
				Ip:       "127.0.0.1",
				Port:     8888,
				ConfPath: pwd + "/conf/app2.json",
			},
		}
		Setting.MapJson()
	}
}
