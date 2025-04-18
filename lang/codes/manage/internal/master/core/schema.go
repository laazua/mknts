package core

type LoginModel struct {
	Name   string
	Passwd string
}

type TestModel struct {
	Aa string `json:"aa" binding:"required"`
	Bb string `json:"bb" binding:"required"`
}
