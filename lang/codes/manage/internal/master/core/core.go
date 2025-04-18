package core

import (
	"os"
	"path/filepath"
)

// 获取项目根目录
func RootPath() string {
	exePath, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exeDir := filepath.Dir(exePath)
	rootPath, err := filepath.Abs(
		filepath.Join(exeDir, "../.."))
	if err != nil {
		panic(err)
	}

	return rootPath
}
