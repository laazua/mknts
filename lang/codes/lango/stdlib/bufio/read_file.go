package bufio

import (
	"bufio"
	"fmt"
	"os"
)

// ReadFile 使用bufio.Reader进行文件读取
func ReadFile() {
	file, err := os.Open("test.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	for {
		// 读取到指定分隔符为止,这里是读取到换行符为止
		line, err := reader.ReadString('\n')
		if err != nil {
			return
		}
		fmt.Println(line)
	}

	// Reader其他读取方法
}

// WriteFile 使用bufio.Writer进行文件写入
func WriteFile() {
	file, err := os.Create("test.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := bufio.NewWriter(file)

	_, err = writer.WriteString("hello world\n")
	if err != nil {
		fmt.Println(err.Error())
	}
	writer.Flush()

	// Writer其他的方法
}

// ScanFile 使用bufio.Scanner进行文件读取
func ScanFile() {
	file, err := os.Open("test.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println("line: ", scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err.Error())
	}
}
