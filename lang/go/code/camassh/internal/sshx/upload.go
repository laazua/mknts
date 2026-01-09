package sshx

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
)

const (
	// 默认文件权限
	defaultFileMode = 0644
	// 默认目录权限
	defaultDirMode = 0755
	// 缓冲区大小
	bufferSize = 32 * 1024
)

// 添加文件传输相关的结构体
type FileTransferProgress struct {
	Filename    string
	TotalSize   int64
	Transferred int64
	Percentage  float64
}

// 进度回调函数类型
type ProgressCallback func(*FileTransferProgress)

// UploadFile 上传本地文件到远程主机
func (c *Client) UploadFile(localPath, remotePath string) error {
	return c.UploadFileWithProgress(localPath, remotePath, nil)
}

// UploadFileWithProgress 带进度回调的文件上传
func (c *Client) UploadFileWithProgress(localPath, remotePath string, callback ProgressCallback) error {
	// 打开本地文件
	file, err := os.Open(localPath)
	if err != nil {
		return fmt.Errorf("open local file failed: %w", err)
	}
	defer file.Close()

	// 获取文件信息
	fileInfo, err := file.Stat()
	if err != nil {
		return fmt.Errorf("get file info failed: %w", err)
	}

	// 获取文件大小
	fileSize := fileInfo.Size()

	// 创建远程目录（如果需要）
	remoteDir := filepath.Dir(remotePath)
	if remoteDir != "." && remoteDir != "/" {
		if err := c.createRemoteDir(remoteDir); err != nil {
			return fmt.Errorf("create remote directory failed: %w", err)
		}
	}

	// 使用scp协议上传文件
	session, err := c.client.NewSession()
	if err != nil {
		return fmt.Errorf("create session failed: %w", err)
	}
	defer session.Close()

	// 创建管道用于数据传输
	stdin, err := session.StdinPipe()
	if err != nil {
		return fmt.Errorf("get stdin pipe failed: %w", err)
	}

	// 启动scp命令
	cmd := fmt.Sprintf("scp -t %s", remotePath)
	if err := session.Start(cmd); err != nil {
		return fmt.Errorf("start scp command failed: %w", err)
	}

	// 发送文件信息头
	mode := fileInfo.Mode().Perm()
	fmt.Fprintf(stdin, "C%04o %d %s\n", mode, fileSize, filepath.Base(remotePath))

	// 复制文件内容
	var transferred int64
	buffer := make([]byte, bufferSize)

	for {
		n, err := file.Read(buffer)
		if n > 0 {
			_, writeErr := stdin.Write(buffer[:n])
			if writeErr != nil {
				return fmt.Errorf("write to remote failed: %w", writeErr)
			}

			transferred += int64(n)

			// 调用进度回调
			if callback != nil {
				progress := &FileTransferProgress{
					Filename:    filepath.Base(localPath),
					TotalSize:   fileSize,
					Transferred: transferred,
					Percentage:  float64(transferred) / float64(fileSize) * 100,
				}
				callback(progress)
			}
		}

		if err != nil {
			if err == io.EOF {
				break
			}
			return fmt.Errorf("read local file failed: %w", err)
		}
	}

	// 发送结束标志
	fmt.Fprint(stdin, "\x00")
	stdin.Close()

	// 等待命令完成
	return session.Wait()
}

// UploadDirectory 上传整个目录到远程主机
func (c *Client) UploadDirectory(localDir, remoteDir string) error {
	return c.UploadDirectoryWithProgress(localDir, remoteDir, nil)
}

// UploadDirectoryWithProgress 带进度回调的目录上传
func (c *Client) UploadDirectoryWithProgress(localDir, remoteDir string, callback ProgressCallback) error {
	// 确保本地目录存在
	info, err := os.Stat(localDir)
	if err != nil {
		return fmt.Errorf("access local directory failed: %w", err)
	}
	if !info.IsDir() {
		return fmt.Errorf("%s is not a directory", localDir)
	}

	// 创建远程目录
	if err := c.createRemoteDir(remoteDir); err != nil {
		return err
	}

	// 遍历本地目录
	return filepath.Walk(localDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		// 计算相对路径
		relPath, err := filepath.Rel(localDir, path)
		if err != nil {
			return err
		}

		remotePath := filepath.Join(remoteDir, relPath)

		if info.IsDir() {
			// 创建远程目录
			return c.createRemoteDir(remotePath)
		} else {
			// 上传文件
			return c.UploadFileWithProgress(path, remotePath, callback)
		}
	})
}

// UploadBytes 上传字节数据到远程文件
func (c *Client) UploadBytes(data []byte, remotePath string) error {
	// 创建临时文件
	tmpFile, err := os.CreateTemp("", "sshx_upload_*")
	if err != nil {
		return fmt.Errorf("create temp file failed: %w", err)
	}
	defer os.Remove(tmpFile.Name())
	defer tmpFile.Close()

	// 写入数据
	if _, err := tmpFile.Write(data); err != nil {
		return fmt.Errorf("write temp file failed: %w", err)
	}

	// 确保数据刷到磁盘
	if err := tmpFile.Sync(); err != nil {
		return err
	}

	// 重置文件指针
	if _, err := tmpFile.Seek(0, 0); err != nil {
		return err
	}

	// 上传文件
	session, err := c.client.NewSession()
	if err != nil {
		return fmt.Errorf("create session failed: %w", err)
	}
	defer session.Close()

	stdin, err := session.StdinPipe()
	if err != nil {
		return err
	}

	// 启动scp命令
	cmd := fmt.Sprintf("scp -t %s", remotePath)
	if err := session.Start(cmd); err != nil {
		return err
	}

	// 发送文件信息头
	mode := defaultFileMode
	fmt.Fprintf(stdin, "C%04o %d %s\n", mode, len(data), filepath.Base(remotePath))

	// 发送数据
	if _, err := stdin.Write(data); err != nil {
		return err
	}

	// 发送结束标志
	fmt.Fprint(stdin, "\x00")
	stdin.Close()

	return session.Wait()
}

// createRemoteDir 创建远程目录（内部方法）
func (c *Client) createRemoteDir(remoteDir string) error {
	// 检查目录是否已存在
	checkCmd := fmt.Sprintf("test -d %s || mkdir -p %s", remoteDir, remoteDir)
	_, err := c.Run(checkCmd)
	return err
}

// GetFileInfo 获取远程文件信息
func (c *Client) GetFileInfo(remotePath string) (string, error) {
	cmd := fmt.Sprintf("stat -c '%%A,%%s,%%Y' %s 2>/dev/null || stat -f '%%Sp,%%z,%%m' %s", remotePath, remotePath)
	result, err := c.Run(cmd)
	if err != nil {
		return "", fmt.Errorf("get file info failed: %w", err)
	}
	return result.Stdout, nil
}

// CheckRemoteFileExists 检查远程文件是否存在
func (c *Client) CheckRemoteFileExists(remotePath string) (bool, error) {
	cmd := fmt.Sprintf("test -e %s && echo 'exists' || echo 'not exists'", remotePath)
	result, err := c.Run(cmd)
	if err != nil {
		return false, err
	}
	return result.Stdout == "exists\n", nil
}
