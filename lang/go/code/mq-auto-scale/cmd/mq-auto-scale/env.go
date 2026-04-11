package main

import (
	"fmt"
	"log"

	"mq-auto-scale/pkg/comm"
)

func main_example() {
	// 方式1：使用全局默认配置（推荐）
	if err := comm.LoadDefaultEnv(); err != nil {
		log.Fatal(err)
	}

	// 获取配置值 - API简洁明了
	appName := comm.Env().Str("APP_NAME", "default-app")
	port := comm.Env().Int("PORT", 3000)
	debug := comm.Env().Bool("DEBUG", false)
	timeout := comm.Env().Float("TIMEOUT", 30.5)

	fmt.Printf("App: %s\n", appName)
	fmt.Printf("Port: %d\n", port)
	fmt.Printf("Debug: %t\n", debug)
	fmt.Printf("Timeout: %.2f\n", timeout)

	// 获取列表
	hosts := comm.Env().StrList("ALLOWED_HOSTS")
	fmt.Printf("Hosts: %v\n", hosts)

	// 获取对象
	dbConfig := comm.Env().Obj("DATABASE")
	fmt.Printf("DB: %+v\n", dbConfig)
	fmt.Printf("DB Host: %v\n", dbConfig["host"])

	// 检查配置是否存在
	if comm.Env().Has("API_SECRET") {
		secret := comm.Env().Str("API_SECRET")
		fmt.Printf("Secret: %s\n", secret)
	}

	// 方式2：创建独立的配置实例（避免全局污染）
	cfg := comm.NewConfig()
	if err := cfg.LoadEnv(".env.production"); err != nil {
		log.Fatal(err)
	}

	prodPort := cfg.Int("PORT", 8080)
	fmt.Printf("Production Port: %d\n", prodPort)

	// 方式3：运行时设置配置
	comm.Env().Set("CUSTOM_KEY", "custom_value")
	fmt.Println(comm.Env().Str("CUSTOM_KEY"))

	// 获取所有配置
	for key, value := range comm.Env().All() {
		fmt.Printf("%s = %v (%T)\n", key, value, value)
	}
}
