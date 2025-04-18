package utils

import "testing"

func TestHashPwd(t *testing.T) {
	pwd := HashPwd("123456")
	t.Log("Hash Pwd: ", pwd)
}
