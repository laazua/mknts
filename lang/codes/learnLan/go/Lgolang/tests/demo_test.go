// 单元测试
// 如果需要测试package main下的calc.go中的函数,只需要新建dome_test.go文件,在dome_test.go中新建测试用例即可
package main

import (
	"testing"
)

func TestAdd(t *testing.T) {
	if res := add(1, 2); res != 3 {
		t.Error("add(1, 2) should be equal to 3")
	}
}

// 运行 go test -v 将自动运行当前package下的所有测试用例
