// test源码文件格式: *_test.go
package test

import (
	"fmt"
	"io/ioutil"
	"testing"
)

var req Request

func TestLogin(t *testing.T) {
	// 发送请求
	req.Key = "Content-Type"
	req.Value = "application/json"
	formData := []byte(`{"name": "admin", "pass": "admin123"}`)
	resp, err := req.Post(formData, "http://127.0.0.1:8880/user/api/login")
	if err != nil {
		t.Log(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		t.Log(err)
	}
	fmt.Println(string(body))
}

func TestAddUser(t *testing.T) {
	// 发送请求
	formData := []byte(`{"name": "admin", "passone": "admin123", "passtow": "admin123"}`)
	resp, err := req.Post(formData, "http://127.0.0.1:8880/user/api/users")
	if err != nil {
		t.Log(err)
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		t.Log(err)
	}
	fmt.Println(string(body))
}
