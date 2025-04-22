package service

import (
	"context"
	"fmt"
	"log/slog"

	"gokins/pkg/core"
	"gokins/pkg/model"
)

type DbUser struct {
	db *core.Db
}

func NewDbUser(db *core.Db) *DbUser {
	return &DbUser{db: db}
}

func (du *DbUser) Add(user model.UserForm) bool {
	if _, err := du.db.Pool.Exec(context.Background(), `INSERT INTO "user" (name,email,password,avatar,token)
	    values ($1,$2,$3,$4,$5)`, user.Name, user.Email, core.HashPassword(user.Password), user.Avatar, user.Token); err != nil {
		slog.Error(fmt.Sprintf("## 数据入库失败: %v\n", err))
		return false
	}
	return true
}

func (du *DbUser) Auth(sign model.UserLoginForm) bool {
	var user model.UserLoginForm
	if err := du.db.Pool.QueryRow(
		context.Background(),
		`SELECT password FROM "user" WHERE name = $1`, sign.UserName).Scan(&user.Password); err != nil {
		slog.Error(fmt.Sprintf("查询数据库失败: %v\n", err))
		return false
	}
	if !core.VerifyPassword(user.Password, sign.Password) {
		return false
	}
	return true
}

func (du *DbUser) Query() ([]model.UserForm, error) {
	rows, err := du.db.Pool.Query(context.Background(), `SELECT name,email,is_delete FROM "user"`)
	if err != nil {
		slog.Error(fmt.Sprintf("## 查询用户列表失败: %v\n", err))
		return nil, err
	}
	var users []model.UserForm
	for rows.Next() {
		var user model.UserForm
		if err := rows.Scan(&user.Name, &user.Email, &user.IsDelete); err != nil {
			slog.Error(fmt.Sprintf("## Scan rows Failed: %v\n", err))
			return nil, err
		}
		users = append(users, user)
	}
	return users, nil
}

func (du *DbUser) Delete(user model.UserForm) bool {
	if _, err := du.db.Pool.Exec(context.Background(), `UPDATE "user" SET is_delete = $1 WHERE name = $2`,
		user.IsDelete, user.Name); err != nil {
		slog.Error(fmt.Sprintf("## 删除用户失败: %v\n", err))
		return false
	}
	return true
}

func (du *DbUser) Update() {}
