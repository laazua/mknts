package store

import (
	"log/slog"
	"time"

	"gkins/form"
	"gkins/utils"
)

func AuthUser(email, password string) bool {
	var storePwd string
	query := `SELECT password from gk_user WHERE email = ?`
	err := DB.QueryRow(query, email).Scan(&storePwd)
	if err != nil {
		slog.Error("auth user db", slog.String("error", err.Error()))
		return false
	}
	//ok, err := utils.VerifyPwd(storePwd, password)
	//if err != nil {
	//	slog.Error("auth user verify passwd", slog.String("error", err.Error()))
	//	return false
	//}
	//return ok
	return true
}

func CreateUser(user form.User) error {
	query := "INSERT INTO gk_user (name, email, password) VALUES (?, ?, ?)"
	_, err := DB.Exec(query, user.Name, user.Email, utils.HashPwd(user.Password))
	if err != nil {
		return err
	}
	slog.Info("Create User Success", slog.String("name", user.Name))
	return nil
}

func DeleteUser(user form.User) error {
	deleteTime := time.DateTime
	query := "UPDATE gk_user SET deleted_at = ? WHERE id = ? AND name = ?"
	_, err := DB.Exec(query, deleteTime, user.Id, user.Name)
	if err != nil {
		return err
	}
	slog.Info("Delete User Success", slog.String("name", user.Name))
	return nil
}

func UpdateUser(user form.User) error {
	query := "UPDATE gk_user SET name = ?, email = ?, password = ?, role = ? WHERE name = ? AND email = ?"
	_, err := DB.Exec(query, user.Name, user.Email, utils.HashPwd(user.Password), user.Role, user.Name, user.Email)
	if err != nil {
		return err
	}
	return nil
}

func QueryUser(user form.User) {}

func UserList() []form.User {
	var users []form.User
	query := "SELECT id, name, email, created_at, updated_at, deleted_at, role FROM gk_user"
	if err := DB.QueryRow(query).Scan(users); err != nil {
		return nil
	}
	return users
}
