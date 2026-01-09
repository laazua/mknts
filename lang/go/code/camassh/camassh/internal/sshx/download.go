package sshx

import (
	// ... 原有导入
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
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
	cmd := fmt.Sprintf("scp -f %s", remotePath)
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

	for {
		n, err := stdout.Read(buffer)
		if n > 0 {
			// 检查是否到达文件结束标记
			if n >= 1 && buffer[n-1] == 0 {
				// 写入除了结束标记外的所有数据
				if n-1 > 0 {
					if _, err := file.Write(buffer[:n-1]); err != nil {
						return fmt.Errorf("write to local file failed: %w", err)
					}
					transferred += int64(n - 1)
				}
				break
			}

			// 写入数据
			if _, err := file.Write(buffer[:n]); err != nil {
				return fmt.Errorf("write to local file failed: %w", err)
			}

			transferred += int64(n)

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

	return session.Wait()
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
	return session.Run(cmd)
}
