package main

import (
    "bytes"
    "context"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/spf13/viper"
    clientv3 "go.etcd.io/etcd/client/v3"
)

func main() {
    // 获取当前环境，默认为 "dev"
    env := os.Getenv("APP_ENV")
    if env == "" {
        env = "dev"
    }
    
    // 本地默认配置文件路径
    defaultConfigFile := "config." + env + ".yaml"

    // 创建 etcd 客户端
    cli, err := clientv3.New(clientv3.Config{
        Endpoints:   []string{"localhost:23379"}, // etcd 地址
        DialTimeout: 5 * time.Second,
    })
    if err != nil {
        log.Printf("Failed to connect to etcd: %v", err)
        loadLocalConfig(defaultConfigFile) // 如果连接 etcd 失败，加载本地配置
        return
    }
    defer cli.Close()

    // 从 etcd 中加载配置
    configKey := "/config/app/" + env // 根据环境变量动态设置 etcd 中的 key
    if !loadConfigFromEtcd(cli, configKey) {
        // 如果从 etcd 中获取配置失败，加载本地默认配置
        loadLocalConfig(defaultConfigFile)
    }

    // 模拟读取配置信息
    fmt.Println("App Name:", viper.GetString("app_name"))
    fmt.Println("Server Host:", viper.GetString("server.host"))
    fmt.Println("Server Port:", viper.GetInt("server.port"))
}

// 从 etcd 中加载配置
func loadConfigFromEtcd(cli *clientv3.Client, key string) bool {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    resp, err := cli.Get(ctx, key)
    if err != nil {
        log.Printf("Error fetching config from etcd: %v", err)
        return false
    }

    if len(resp.Kvs) > 0 {
        viper.SetConfigType("yaml")
        // 使用 bytes.NewReader 读取 etcd 中的配置内容
        err := viper.ReadConfig(bytes.NewReader(resp.Kvs[0].Value))
        if err != nil {
            log.Printf("Error reading config from etcd: %v", err)
            return false
        }
        fmt.Println("Config loaded from etcd for environment:", key)
        return true
    }

    log.Printf("No config found in etcd for key: %s", key)
    return false
}

// 加载本地配置文件
func loadLocalConfig(fileName string) {
    viper.SetConfigFile(fileName)

    if err := viper.ReadInConfig(); err != nil {
        log.Fatalf("Error reading local config file: %s, %v", fileName, err)
    }
    fmt.Println("Config loaded from local file:", fileName)
}

