package utils

import (
	"os"

	"github.com/joho/godotenv"
)

// 初始化配置
func init() {
	print("init config")
	err := godotenv.Load(".env")
	if err != nil {
		panic(err)
	}
}

func GetEnv(key string) string {
	return os.Getenv(key)
}
