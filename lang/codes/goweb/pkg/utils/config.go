package utils

import (
	"encoding/json"
	"io/ioutil"
	"os"
)

// 基础配置字段
type App struct {
	// app1,app2都有的字段
	Ip       string
	Port     int
	ConfPath string
	KeyWord  string

	// app1存在的字段
	RemotePort int

	// app2存在的字段
	ZonePath string
	BinPath  string
}

// mysql配置的字段(app1)
type Mysql struct {
	Host     string
	Port     int
	Dbname   string
	Username string
	Password string
}

// svn配置的字段(app2)
type Svn struct {
	Url      string
	Username string
	Password string
}

// json配置文件映射的体
type AppConfig struct {
	App   App
	Mysql Mysql
	Svn   Svn
}

var AppCon *AppConfig

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
		AppCon = &AppConfig{
			App: App{
				Ip:       "127.0.0.1",
				Port:     8888,
				ConfPath: pwd + "/conf/app1.json",
			},
		}
		AppCon.MapJson()
	case "app2":
		AppCon = &AppConfig{
			App: App{
				Ip:       "127.0.0.1",
				Port:     8888,
				ConfPath: pwd + "/conf/app2.json",
			},
		}
		AppCon.MapJson()
	}
}
