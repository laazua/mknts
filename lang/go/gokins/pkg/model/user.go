package model

// type User struct {
// 	ID       int64  `db:"id"`
// 	Name     string `db:"name"`
// 	Email    string `db:"email"`
// 	Password string `db:"password"`
// 	Avatar   string `db:"avatar"`
// 	Token    string `db:"token"`
// }

// type Role struct {
// 	ID          int64  `db:"id"`
// 	Name        string `db:"name"`
// 	Description string `db:"description"`
// }

// type Menu struct {
// 	ID          int64  `db:"id"`
// 	Name        string `db:"name"`
// 	Redirect    string `db:"redirect"`
// 	Path        string `db:"path"`
// 	Component   string `db:"component"`
// 	ParentId    int64  `db:"parent_id"`
// 	Meta        any    `db:"meta"`
// 	Description string `db:"description"`
// }

// type UserRole struct {
// 	UserId int64 `db:"user_id"`
// 	RoleId int64 `db:"role_id"`
// }

// type RoleMenu struct {
// 	RoleId int64 `db:"role_id"`
// 	MenuId int64 `db:"menu_id"`
// }

type UserLoginForm struct {
	UserName string `json:"username"`
	Password string `json:"password"`
}

type UserForm struct {
	Name     string `json:"name"`
	Email    string `json:"email"`
	Password string `json:"password"`
	Avatar   string `json:"avatar"`
	Token    string `json:"token"`
	IsDelete bool   `json:"isDelete"`
}
