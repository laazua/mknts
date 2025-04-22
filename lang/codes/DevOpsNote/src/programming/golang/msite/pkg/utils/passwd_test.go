package utils

import (
	"testing"
)

func TestHashPasswd(t *testing.T) {
	pwd := HashPasswd("123456")
	t.Log("Hash Pwd: ", pwd)
}

func TestVerifyPasswd(t *testing.T) {
	ok, err := VerifyPasswd("$jZae727K08KaOmKSgOaGzww_XVqGr_PKEgIMkjrcbJI=", "123456")
	if err != nil {
		t.Errorf("Verify Error: %s", err.Error())
	}
	if ok == true {
		t.Log("Verify pass success")
	} else {
		t.Log("Verify pass failure")
	}

}

// 运行指定的测试函数:
// go test -v -run "Test(HashPasswd|VerifyPasswd)"

// 运行所有测试(根目录下执行):
// go test -v ./...
