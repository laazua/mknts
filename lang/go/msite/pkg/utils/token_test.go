package utils

import (
	"log"
	"msite/pkg/env"
	"os"
	"testing"
)

func TestCreateToken(t *testing.T) {
	// 切换工作目录到项目根目录
	err := os.Chdir("../..")
	if err != nil {
		log.Fatalf("Failed to change directory: %v", err)
	}
	env.LoadEnv(".env")
	// t.Skip()
	token, err := CreateToken("zhangsan")
	if err != nil {
		t.Errorf("create token error: %s", err.Error())
	} else {
		t.Logf("create token: %s", token)
	}
}

func TestParseToken(t *testing.T) {
	payLoad, err := ParseToken("eyJOYW1lIjoiemhhbmdzYW4iLCJFeHBpcmVzQXQiOjg4MDc0NTk4ODh9.b_c1HD1Y8-jMEu_RfEePP2LRe6f6zxSkG39ODGoUR_g=")
	if err != nil {
		t.Errorf("Parse token error: %s", err)
	} else {
		t.Log("parse token: ", payLoad.Name)
	}
}
