package utils

import (
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"errors"
)

type Cryto struct {
	KeyWord []byte
}

func NewCryto() *Cryto {
	return &Cryto{
		KeyWord: []byte(Setting.App.KeyWord),
	}
}

//PKCS7 填充模式
func (c Cryto) PKCS7Padding(ciphertext []byte, blockSize int) []byte {
	padding := blockSize - len(ciphertext)%blockSize
	padtext := bytes.Repeat([]byte{byte(padding)}, padding)
	return append(ciphertext, padtext...)
}

//填充的反向操作，删除填充字符串
func (c Cryto) PKCS7UnPadding(origData []byte) ([]byte, error) {
	//获取数据长度
	length := len(origData)
	if length == 0 {
		return nil, errors.New("加密字符串错误！")
	} else {
		//获取填充字符串长度
		unpadding := int(origData[length-1])
		//截取切片，删除填充字节，并且返回明文
		return origData[:(length - unpadding)], nil
	}
}

//实现加密
func (c Cryto) AesEncrypt(origData []byte) ([]byte, error) {
	//创建加密算法实例
	block, err := aes.NewCipher(c.KeyWord)
	if err != nil {
		return nil, err
	}
	//获取块的大小
	blockSize := block.BlockSize()
	//对数据进行填充，让数据长度满足需求
	origData = c.PKCS7Padding(origData, blockSize)
	//采用AES加密方法中CBC加密模式
	blocMode := cipher.NewCBCEncrypter(block, c.KeyWord[:blockSize])
	crypted := make([]byte, len(origData))
	//执行加密
	blocMode.CryptBlocks(crypted, origData)
	return crypted, nil
}

//实现解密
func (c Cryto) AesDeCrypt(cypted []byte) ([]byte, error) {
	//创建加密算法实例
	block, err := aes.NewCipher(c.KeyWord)
	if err != nil {
		return nil, err
	}
	//获取块大小
	blockSize := block.BlockSize()
	//创建加密客户端实例
	blockMode := cipher.NewCBCDecrypter(block, c.KeyWord[:blockSize])
	origData := make([]byte, len(cypted))
	//这个函数也可以用来解密
	blockMode.CryptBlocks(origData, cypted)
	//去除填充字符串
	origData, err = c.PKCS7UnPadding(origData)
	if err != nil {
		return nil, err
	}
	return origData, err
}

//加密
func (c Cryto) EnData(data []byte) (string, error) {
	// (参数GlbCon.App.KeyWord 必须是 16、24 或者 32 位的 [] byte，
	// 分别对应 AES-128, AES-192 或 AES-256 算法
	ret, err := c.AesEncrypt(data)
	if err != nil {
		return "", err
	}
	return base64.StdEncoding.EncodeToString(ret), err
}

//解密
func (c Cryto) DeData(data string) ([]byte, error) {
	//解密base64字符串
	dataByte, err := base64.StdEncoding.DecodeString(data)
	if err != nil {
		return nil, err
	}
	// 执行AES解密
	// (参数GlbCon.App.KeyWord 必须是 16、24 或者 32 位的 [] byte，
	// 分别对应 AES-128, AES-192 或 AES-256 算法
	return c.AesDeCrypt(dataByte)
}
