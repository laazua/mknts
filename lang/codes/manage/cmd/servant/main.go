package main

import "manage/internal/servant"

func main() {
	s := servant.NewServant()

	if err := s.Run(":8898"); err != nil {
		panic(err)
	}
}
