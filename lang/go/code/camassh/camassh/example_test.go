// 使用示例
package main

import (
	"bytes"
	"fmt"
	"log"
	"os"

	"camassh/internal/sshx"
)

func Tmain() {
	// 示例1：使用密码连接
	config := &sshx.Config{
		Host:     "192.168.1.100",
		Port:     22,
		Username: "your_username",
		Password: "your_password",
		Timeout:  10,
	}
	client, err := sshx.NewClient(config)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Close()

	// 测试连接
	if err := client.TestConnection(); err != nil {
		log.Fatal("Connection test failed:", err)
	}

	// 执行单条命令
	result, err := client.Run("ls -la")
	if err != nil {
		log.Printf("Command failed: %v", err)
	} else {
		fmt.Printf("Exit Code: %d\n", result.ExitCode)
		fmt.Printf("Output:\n%s\n", result.Stdout)
	}

	// 示例2：批量执行命令
	commands := []string{
		"hostname",
		"date",
		"whoami",
		"pwd",
	}

	results, err := client.RunMultiple(commands)
	if err != nil {
		log.Printf("Batch execution error: %v", err)
	}

	for i, result := range results {
		fmt.Printf("\n=== Command %d ===\n", i+1)
		fmt.Printf("Output: %s", result.Stdout)
	}

	// 示例3：流式输出
	fmt.Println("\n=== Streaming Output ===")
	err = client.Stream("tail -f /var/log/syslog", os.Stdout, os.Stderr)
	if err != nil {
		log.Printf("Stream error: %v", err)
	}

	// 示例4：使用私钥连接（假设）
	// privateKey, _ := os.ReadFile("/path/to/private_key")
	// client2, err := sshx.NewClient("host", 22, "user", "", privateKey)

	// ------------------ 上传示例 ------------------
	// 简单上传文件
	err = client.UploadFile("/local/path/file.txt", "/remote/path/file.txt")

	// 带进度显示的上传
	progressCallback := func(p *sshx.FileTransferProgress) {
		fmt.Printf("Uploading %s: %.2f%%\n", p.Filename, p.Percentage)
	}
	err = client.UploadFileWithProgress("/local/path/file.txt", "/remote/path/file.txt", progressCallback)

	// 上传整个目录
	err = client.UploadDirectory("/local/dir", "/remote/dir")

	// 上传字节数据
	data := []byte("Hello, World!")
	err = client.UploadBytes(data, "/remote/path/data.txt")

	// 检查文件是否存在
	_, err = client.CheckRemoteFileExists("/remote/path/file.txt")
	if err != nil {
		log.Printf("Check file exists error: %v", err)
	}

	// ------------------ 下载示例 ------------------
	// 简单下载文件
	err = client.DownloadFile("/remote/path/file.txt", "/local/path/file.txt")

	// 带进度显示下载
	progressCallback = func(p *sshx.FileTransferProgress) {
		fmt.Printf("Downloading %s: %.2f%%\n", p.Filename, p.Percentage)
	}
	err = client.DownloadFileWithProgress("/remote/path/file.txt", "/local/path/file.txt", progressCallback)

	// 下载整个目录
	err = client.DownloadDirectory("/remote/dir", "/local/dir")

	// 下载为字节数据
	data, err = client.DownloadBytes("/remote/path/file.txt")
	if err == nil {
		fmt.Printf("Downloaded %d bytes\n", len(data))
	}

	// 下载到自定义Writer
	var buf bytes.Buffer
	err = client.DownloadToWriter("/remote/path/file.txt", &buf)

	// 获取远程文件信息
	info, err := client.GetRemoteFileInfo("/remote/path/file.txt")
	if err == nil {
		fmt.Printf("File size: %d, Mode: %v\n", info.Size, info.Mode)
	}

	// 列出远程目录
	files, err := client.ListRemoteDirectory("/remote/dir")
	if err == nil {
		for _, file := range files {
			fmt.Println(file)
		}
	}

	// 比较本地和远程文件
	same, err := client.CompareFiles("/local/path/file.txt", "/remote/path/file.txt")
	if err == nil && same {
		fmt.Println("Files are identical")
	}

	// 断点续传下载
	err = client.ResumeDownload("/remote/path/largefile.zip", "/local/path/largefile.zip")
}
