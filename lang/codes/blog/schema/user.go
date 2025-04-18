package schema

type Auth struct {
	Email    string `form:"email"`
	Password string `form:"password"`
}

type User struct {
	Auth
	Name   string `form:"name"`
	Avator string `form:"avator"`
}
