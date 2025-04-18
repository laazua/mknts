package test

import (
	"fmt"
	"msbn/utils"
	"testing"
)

func TestGetData(t *testing.T) {
	stime := "2022-01-01"
	etime := "2022-02-18"
	resp, err := utils.GetData(stime, etime, "997", 10, 1)
	if err != nil {
		t.Log(err)
	}
	fmt.Println(resp)
}
