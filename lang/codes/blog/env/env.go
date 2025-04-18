package env

import (
	"strconv"

	"github.com/joho/godotenv"
)

func Load() {
	// load default .env file
	err := godotenv.Load()
	if err != nil {
		panic(err)
	}
}

// 字符串转int
func Atoint(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return num
}

// 字符串转列表
func Atolist(s string) {

}
