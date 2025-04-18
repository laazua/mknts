package main

import (
	"crypto/md5"
	"crypto/sha256"
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"io"
)

func main() {
	testMd5()
	testSha224()
	testSha256()
	testSha384()
	testSha512()
}

// crypto/md5实现了MD5哈希算法
func testMd5() {
	h := md5.New() // 返回一个使用MD5校验的hash.Hash接口
	io.WriteString(h, "bar")
	io.WriteString(h, "foo")
	fmt.Printf("%x\n", h.Sum(nil))
}

//sha256包实现了SHA224和SHA256哈希算法
func testSha224() {
	h := sha256.New224()
	io.WriteString(h, "bar")
	io.WriteString(h, "foo")
	fmt.Printf("%x\n", h.Sum(nil))
}

func testSha256() {
	h := sha256.New()
	io.WriteString(h, "bar")
	io.WriteString(h, "foo")
	fmt.Printf("%x\n", h.Sum(nil))
}

// sha512包实现了SHA384和SHA512哈希算法
func testSha384() {
	h := sha512.New384()
	io.WriteString(h, "bar")
	io.WriteString(h, "foo")
	fmt.Printf("%x\n", h.Sum(nil))
}

func testSha512() {
	h := sha512.New()
	io.WriteString(h, "bar")
	io.WriteString(h, "foo")
	fmt.Printf("%x\n", h.Sum(nil))
}

// md5
func testMd51(str string) string {
	h := md5.New()
	h.Write([]byte(str))
	return hex.EncodeToString(h.Sum(nil))
}

func testMd52(str string) string {
	data := []byte(str)
	h := md5.Sum(data)
	return fmt.Sprintf("%x", h)
}

func testMd53(str string) string {
	w := md5.New()
	io.WriteString(w, str)
	return fmt.Sprintf("%x", w.Sum(nil))
}
