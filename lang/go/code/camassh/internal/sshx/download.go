package sshx

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	"golang.org/x/crypto/ssh"
)

// DownloadFile 从远程主机下载文件到本地
func (c *Client) DownloadFile(remotePath, localPath string) error {
	return c.DownloadFileWithProgress(remotePath, localPath, nil)
}

// DownloadFileWithProgress 带进度回调的文件下载
func (c *Client) DownloadFileWithProgress(remotePath, localPath string, callback ProgressCallback) error {
	// 检查远程文件是否存在
	exists, err := c.CheckRemoteFileExists(remotePath)
	if err != nil {
		return fmt.Errorf("check remote file failed: %w", err)
	}
	if !exists {
		return fmt.Errorf("remote file does not exist: %s", remotePath)
	}

	// 获取远程文件信息
	_, err = c.getRemoteFileInfo(remotePath)
	if err != nil {
		return fmt.Errorf("get remote file info failed: %w", err)
	}

	// 创建本地目录（如果需要）
	localDir := filepath.Dir(localPath)
	if localDir != "." && localDir != "" {
		if err := os.MkdirAll(localDir, defaultDirMode); err != nil {
			return fmt.Errorf("create local directory failed: %w", err)
		}
	}

	// 创建本地文件
	file, err := os.Create(localPath)
	if err != nil {
		return fmt.Errorf("create local file failed: %w", err)
	}
	defer file.Close()

	// 使用scp协议下载文件
	session, err := c.client.NewSession()
	if err != nil {
		return fmt.Errorf("create session failed: %w", err)
	}
	defer session.Close()

	stdout, err := session.StdoutPipe()
	if err != nil {
		return fmt.Errorf("get stdout pipe failed: %w", err)
	}

	stdin, err := session.StdinPipe()
	if err != nil {
		return fmt.Errorf("get stdin pipe failed: %w", err)
	}

	// 启动scp命令
	cmd := fmt.Sprintf("sudo scp -f %s", remotePath)
	if err := session.Start(cmd); err != nil {
		return fmt.Errorf("start scp command failed: %w", err)
	}

	// 发送确认信号
	if _, err := stdin.Write([]byte{0}); err != nil {
		return fmt.Errorf("send confirmation failed: %w", err)
	}

	// 读取文件头
	header := make([]byte, 1024)
	n, err := stdout.Read(header)
	if err != nil || n == 0 {
		return fmt.Errorf("read file header failed: %w", err)
	}

	// 解析文件头（格式如：C0644 1024 filename）
	headerStr := string(header[:n])
	if headerStr[0] != 'C' {
		return fmt.Errorf("invalid file header: %s", headerStr)
	}

	// 发送确认信号
	if _, err := stdin.Write([]byte{0}); err != nil {
		return fmt.Errorf("send confirmation failed: %w", err)
	}

	// 解析文件大小
	parts := strings.Split(headerStr[:strings.Index(headerStr, "\n")], " ")
	if len(parts) < 3 {
		return fmt.Errorf("invalid header format: %s", headerStr)
	}

	fileSize, err := strconv.ParseInt(parts[1], 10, 64)
	if err != nil {
		return fmt.Errorf("parse file size failed: %w", err)
	}

	// 下载文件内容
	var transferred int64
	buffer := make([]byte, bufferSize)
	totalRead := int64(0)

	for {
		// 计算还需要读取的字节数
		remaining := fileSize - totalRead
		if remaining <= 0 {
			break
		}

		// 调整读取大小以避免超出文件边界
		readSize := bufferSize
		if remaining < int64(readSize) {
			readSize = int(remaining)
		}

		n, err := stdout.Read(buffer[:readSize])
		if n > 0 {
			// 检查是否读到结束标记
			writeBuffer := buffer[:n]
			writeSize := n

			// 如果这是最后一块数据，检查是否有结束标记
			if totalRead+int64(n) >= fileSize {
				// 检查缓冲区末尾是否有结束标记 (0x00)
				for i := n - 1; i >= 0; i-- {
					if buffer[i] == 0 {
						writeSize = i
						break
					}
				}
				writeBuffer = buffer[:writeSize]
			}

			// 写入数据
			if writeSize > 0 {
				if _, err := file.Write(writeBuffer); err != nil {
					return fmt.Errorf("write to local file failed: %w", err)
				}
				transferred += int64(writeSize)
				totalRead += int64(writeSize)

				// 调用进度回调
				if callback != nil {
					progress := &FileTransferProgress{
						Filename:    filepath.Base(remotePath),
						TotalSize:   fileSize,
						Transferred: transferred,
						Percentage:  float64(transferred) / float64(fileSize) * 100,
					}
					callback(progress)
				}
			}

			// 如果文件传输完成，发送最终确认
			if totalRead >= fileSize {
				// 发送最终确认信号
				if _, err := stdin.Write([]byte{0}); err != nil {
					return fmt.Errorf("send final confirmation failed: %w", err)
				}

				// 尝试读取可能存在的目录结束标记 'E'
				go func() {
					// 短暂延迟后读取可能的额外数据
					time.Sleep(100 * time.Millisecond)
					tempBuf := make([]byte, 10)
					if n, _ := stdout.Read(tempBuf); n > 0 && tempBuf[0] == 'E' {
						stdin.Write([]byte{0}) // 确认目录结束
					}
				}()

				break
			}
		}

		if err != nil {
			if err == io.EOF {
				break
			}
			return fmt.Errorf("read from remote failed: %w", err)
		}
	}

	// 设置文件权限
	if len(parts) > 0 {
		modeStr := parts[0][1:] // 去掉开头的'C'
		mode, err := strconv.ParseInt(modeStr, 8, 32)
		if err == nil {
			os.Chmod(localPath, os.FileMode(mode))
		}
	}

	// 使用带超时的等待机制
	errChan := make(chan error, 1)
	go func() {
		errChan <- session.Wait()
	}()

	// 设置5秒超时
	select {
	case err := <-errChan:
		if err != nil {
			// 检查是否是正常的退出错误
			if exitErr, ok := err.(*ssh.ExitError); ok {
				// scp 成功执行后通常返回0，如果有错误但文件已下载完整，也认为是成功
				if exitErr.ExitStatus() == 0 || transferred == fileSize {
					return nil
				}
				return fmt.Errorf("scp failed with exit code %d", exitErr.ExitStatus())
			}
			return fmt.Errorf("session wait failed: %w", err)
		}
		return nil
	case <-time.After(5 * time.Second):
		// 超时后检查文件是否已完整下载
		if transferred == fileSize {
			// 文件已完整下载，强制关闭会话并返回成功
			session.Close()
			return nil
		}
		// 文件未完整下载，返回错误
		session.Close()
		return fmt.Errorf("download timeout, downloaded %d/%d bytes", transferred, fileSize)
	}
}

// DownloadDirectory 下载整个远程目录到本地
func (c *Client) DownloadDirectory(remoteDir, localDir string) error {
	return c.DownloadDirectoryWithProgress(remoteDir, localDir, nil)
}

// DownloadDirectoryWithProgress 带进度回调的目录下载
func (c *Client) DownloadDirectoryWithProgress(remoteDir, localDir string, callback ProgressCallback) error {
	// 检查远程目录是否存在
	exists, err := c.CheckRemoteFileExists(remoteDir)
	if err != nil {
		return fmt.Errorf("check remote directory failed: %w", err)
	}
	if !exists {
		return fmt.Errorf("remote directory does not exist: %s", remoteDir)
	}

	// 获取远程目录结构
	files, err := c.listRemoteDirectory(remoteDir)
	if err != nil {
		return fmt.Errorf("list remote directory failed: %w", err)
	}

	// 创建本地目录
	if err := os.MkdirAll(localDir, defaultDirMode); err != nil {
		return fmt.Errorf("create local directory failed: %w", err)
	}

	// 下载目录中的所有文件
	for _, file := range files {
		remotePath := filepath.Join(remoteDir, file)
		localPath := filepath.Join(localDir, file)

		// 递归处理子目录
		isDir, err := c.isRemoteDirectory(remotePath)
		if err != nil {
			return err
		}

		if isDir {
			if err := c.DownloadDirectoryWithProgress(remotePath, localPath, callback); err != nil {
				return err
			}
		} else {
			if err := c.DownloadFileWithProgress(remotePath, localPath, callback); err != nil {
				return fmt.Errorf("download file %s failed: %w", remotePath, err)
			}
		}
	}

	return nil
}

// DownloadBytes 从远程文件下载为字节数据
func (c *Client) DownloadBytes(remotePath string) ([]byte, error) {
	// 检查远程文件是否存在
	exists, err := c.CheckRemoteFileExists(remotePath)
	if err != nil {
		return nil, fmt.Errorf("check remote file failed: %w", err)
	}
	if !exists {
		return nil, fmt.Errorf("remote file does not exist: %s", remotePath)
	}

	// 使用cat命令读取文件内容
	cmd := fmt.Sprintf("cat %s", remotePath)
	result, err := c.Run(cmd)
	if err != nil {
		return nil, fmt.Errorf("read remote file failed: %w", err)
	}

	return []byte(result.Stdout), nil
}

// DownloadToWriter 从远程文件下载并写入到io.Writer
func (c *Client) DownloadToWriter(remotePath string, writer io.Writer) error {
	// 使用cat命令读取文件内容并写入writer
	cmd := fmt.Sprintf("cat %s", remotePath)
	session, err := c.client.NewSession()
	if err != nil {
		return err
	}
	defer session.Close()

	session.Stdout = writer
	return session.Run(cmd)
}

// 内部辅助方法

// getRemoteFileInfo 获取远程文件详细信息
func (c *Client) getRemoteFileInfo(remotePath string) (*RemoteFileInfo, error) {
	cmd := fmt.Sprintf("stat -c '%%s,%%a,%%Y,%%F' %s 2>/dev/null || stat -f '%%z,%%p,%%m,%%HT' %s", remotePath, remotePath)
	result, err := c.Run(cmd)
	if err != nil {
		return nil, err
	}

	parts := strings.Split(strings.TrimSpace(result.Stdout), ",")
	if len(parts) < 4 {
		return nil, fmt.Errorf("invalid stat output: %s", result.Stdout)
	}

	size, _ := strconv.ParseInt(parts[0], 10, 64)
	mode, _ := strconv.ParseInt(parts[1], 8, 32)
	modTime, _ := strconv.ParseInt(parts[2], 10, 64)
	fileType := parts[3]

	return &RemoteFileInfo{
		Size:    size,
		Mode:    os.FileMode(mode),
		ModTime: time.Unix(modTime, 0),
		IsDir:   strings.Contains(fileType, "directory"),
		IsFile:  strings.Contains(fileType, "regular") || strings.Contains(fileType, "file"),
	}, nil
}

// listRemoteDirectory 列出远程目录内容
func (c *Client) listRemoteDirectory(remoteDir string) ([]string, error) {
	cmd := fmt.Sprintf("find %s -mindepth 1 -maxdepth 1 -type f -o -type d | xargs -I {} basename {}", remoteDir)
	result, err := c.Run(cmd)
	if err != nil {
		return nil, err
	}

	if result.Stdout == "" {
		return []string{}, nil
	}

	files := strings.Split(strings.TrimSpace(result.Stdout), "\n")
	return files, nil
}

// isRemoteDirectory 检查远程路径是否为目录
func (c *Client) isRemoteDirectory(remotePath string) (bool, error) {
	cmd := fmt.Sprintf("test -d %s && echo 'directory' || echo 'not directory'", remotePath)
	result, err := c.Run(cmd)
	if err != nil {
		return false, err
	}
	return strings.TrimSpace(result.Stdout) == "directory", nil
}

// 添加远程文件信息结构体
type RemoteFileInfo struct {
	Size    int64
	Mode    os.FileMode
	ModTime time.Time
	IsDir   bool
	IsFile  bool
}

// GetRemoteFileInfo 公开方法获取远程文件信息
func (c *Client) GetRemoteFileInfo(remotePath string) (*RemoteFileInfo, error) {
	return c.getRemoteFileInfo(remotePath)
}

// ListRemoteDirectory 公开方法列出远程目录
func (c *Client) ListRemoteDirectory(remoteDir string) ([]string, error) {
	return c.listRemoteDirectory(remoteDir)
}

// CompareFiles 比较本地和远程文件是否相同
func (c *Client) CompareFiles(localPath, remotePath string) (bool, error) {
	// 获取本地文件哈希
	localHash, err := c.getFileHash(localPath)
	if err != nil {
		return false, fmt.Errorf("get local file hash failed: %w", err)
	}

	// 获取远程文件哈希
	remoteHash, err := c.getRemoteFileHash(remotePath)
	if err != nil {
		return false, fmt.Errorf("get remote file hash failed: %w", err)
	}

	return localHash == remoteHash, nil
}

// getFileHash 获取本地文件哈希
func (c *Client) getFileHash(filePath string) (string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return "", err
	}

	// 使用简单的哈希，实际使用时可以考虑更安全的哈希算法
	hash := sha256.Sum256(data)
	return hex.EncodeToString(hash[:]), nil
}

// getRemoteFileHash 获取远程文件哈希
func (c *Client) getRemoteFileHash(remotePath string) (string, error) {
	cmd := fmt.Sprintf("sha256sum %s | cut -d' ' -f1", remotePath)
	result, err := c.Run(cmd)
	if err != nil {
		return "", err
	}
	return strings.TrimSpace(result.Stdout), nil
}

// ResumeDownload 断点续传下载
func (c *Client) ResumeDownload(remotePath, localPath string) error {
	// 检查本地文件是否存在
	localInfo, err := os.Stat(localPath)
	localExists := err == nil

	if localExists {
		// 获取本地文件大小
		localSize := localInfo.Size()

		// 获取远程文件大小
		remoteInfo, err := c.getRemoteFileInfo(remotePath)
		if err != nil {
			return err
		}

		// 如果本地文件已经完整，直接返回
		if localSize == remoteInfo.Size {
			return nil
		}

		// 断点续传下载
		return c.resumeDownloadFromOffset(remotePath, localPath, localSize)
	} else {
		// 普通下载
		return c.DownloadFile(remotePath, localPath)
	}
}

// resumeDownloadFromOffset 从指定偏移量开始下载（内部方法）
func (c *Client) resumeDownloadFromOffset(remotePath, localPath string, offset int64) error {
	// 打开本地文件用于追加
	file, err := os.OpenFile(localPath, os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		return err
	}
	defer file.Close()

	// 使用dd命令从指定位置开始读取
	cmd := fmt.Sprintf("dd if=%s bs=1 skip=%d 2>/dev/null", remotePath, offset)
	session, err := c.client.NewSession()
	if err != nil {
		return err
	}
	defer session.Close()

	session.Stdout = file

	// 同样使用带超时的等待
	errChan := make(chan error, 1)
	go func() {
		errChan <- session.Run(cmd)
	}()

	select {
	case err := <-errChan:
		return err
	case <-time.After(30 * time.Second): // 断点续传可能需要更长时间
		session.Close()
		return fmt.Errorf("resume download timeout after 30 seconds")
	}
}
