package schema

type Auth struct {
	Name   string `json:"name"`
	Passwd string `json:"passwd"`
}

type User struct {
	Id     int    `json:"id"`
	Name   string `json:"name"`
	Passwd string `json:"passwd"`
	Email  string `json:"email"`
	Avator string `json:"avator"`
}
