package main

import (
	"manage/internal/master/api"
)

func main() {

	r := api.NewMaster()

	if err := r.Run(":8899"); err != nil {
		panic(err)
	}
}
