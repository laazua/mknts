// io包
package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func main() {
	// io.Reader接口只包含Read()方法
	// 所有实现了Read()方法的类型都满足io.Reader接口
	// io.Writer接口只包含Write()方法
	// 所有实现了Write()方法的类型都满足io.Writer接口

	/*
			os.File 同时实现了 io.Reader 和 io.Writer
			strings.Reader 实现了 io.Reader
			bufio.Reader/Writer 分别实现了 io.Reader 和 io.Writer
		    bytes.Buffer 同时实现了 io.Reader 和 io.Writer
			bytes.Reader 实现了 io.Reader
			compress/gzip.Reader/Writer 分别实现了 io.Reader 和 io.Writer
			crypto/cipher.StreamReader/StreamWriter 分别实现了 io.Reader 和 io.Writer
			crypto/tls.Conn 同时实现了 io.Reader 和 io.Writer
			encoding/csv.Reader/Writer 分别实现了 io.Reader 和 io.Writer
			mime/multipart.Part 实现了 io.Reader
			net/conn 分别实现了 io.Reader 和 io.Writer(Conn接口定义了Read/Write)
			io包本身:
				实现了 Reader 的类型：LimitedReader、PipeReader、SectionReader
				实现了 Writer 的类型：PipeWriter
	*/

	/*
			func Create(name string) (file *File, err Error)
		      根据提供的文件名创建新的文件，返回一个文件对象，默认权限是0666
			func NewFile(fd uintptr, name string) *File
			  根据文件描述符创建相应的文件，返回一个文件对象
			func Open(name string) (file *File, err Error)
			  只读方式打开一个名称为name的文件
			func OpenFile(name string, flag int, perm uint32) (file *File, err Error)
		 	  打开名称为name的文件，flag是打开的方式，只读、读写等，perm是权限
			func (file *File) Write(b []byte) (n int, err Error)
			  写入byte类型的信息到文件
			func (file *File) WriteAt(b []byte, off int64) (n int, err Error)
			  在指定位置开始写入byte类型的信息
			func (file *File) WriteString(s string) (ret int, err Error)
			  写入string信息到文件
			func (file *File) Read(b []byte) (n int, err Error)
			  读取数据到b中
			func (file *File) ReadAt(b []byte, off int64) (n int, err Error)
			  从off开始读取数据到b中
			func Remove(name string) Error
			  删除文件名为name的文件
	*/
}

func openFile() {
	// read only
	if file, err := os.Open("./test.txt"); err != nil {
		return
	} else {
		defer file.Close()
		var buffer [64]byte
		var content []byte
		for {
			if n, err := file.Read(buffer[:]); err != nil {
				return
			} else if err == io.EOF {
				// 读取结束
				break
			} else {
				content = append(content, buffer[:n]...)
			}
		}
		file.WriteString("aaaa")
	}
}

func copyFile() {
	// 打开源文件
	srcFile, err := os.Open("./xxx.txt")
	defer srcFile.Close()
	if err != nil {
		return
	}

	// 创建目标文件
	dstFile, err := os.Open("./yyy.txt")
	defer dstFile.Close()
	if err != nil {
		return
	}

	// 缓冲读取
	buffer := make([]byte, 1024)
	for {
		n, err := srcFile.Read(buffer)
		if err == io.EOF {
			fmt.Println("读取完毕")
			break
		}
		if err != nil {
			fmt.Println("source file read error: ", err)
			return
		}
		dstFile.Write(buffer[:n])
	}
}

// bufio带缓冲读写,是对文件读写的封装
func bufioWrite() {
	fd, err := os.OpenFile("./xxx.txt", os.O_CREATE|os.O_WRONLY, 0666)
	defer fd.Close()
	if err != nil {
		fmt.Println("Open file error: ", err)
		return
	}

	// 获取w对象,并写入数据
	w := bufio.NewWriter(fd)
	w.WriteString("test")
	// 刷新缓冲区,强制写出
	w.Flush()
}

func bufioRead() {
	fd, err := os.Open("./xxx.txt")
	defer fd.Close()
	if err != nil {
		fmt.Println("open file error: ", err)
		return
	}

	r := bufio.NewReader(fd)
	for {
		line, _, err := r.ReadLine()
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println("read file error: ", err)
			return
		}
		fmt.Println(string(line))
	}
}

// ioutil工具包读取文件
func ioutilWrite() {
	if err := ioutil.WriteFile("./xxx.txt", []byte("hahaha"), 0666); err != nil {
		fmt.Println("ioutil write file error: ", err)
		return
	}
}

func ioutilRead() {
	content, err := ioutil.ReadFile("./xxx.txt")
	if err != nil {
		fmt.Println("ioutil read file error: ", err)
		return
	}

	fmt.Println(string(content))
}
