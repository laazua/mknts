package form

type LoginForm struct {
	UserName string `form:"username"`
	Password string `form:"password"`
}
