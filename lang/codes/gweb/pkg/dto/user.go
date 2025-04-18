package dto

import (
	"gweb/pkg/utils"
)

type UserDto struct {
	Username string
	Password string
}

func NewUserDto(username, passwd string) *UserDto {
	return &UserDto{
		Username: username,
		Password: passwd,
	}
}

func (u *UserDto) CheckUser() bool {
	sql := `
	SELECT username, password FROM user WHERE username = ?;
	`
	var username, password string
	if err := utils.Db.QueryRow(sql, u.Username).Scan(&username, &password); err != nil {
		return false
	}
	if pwd, _ := utils.NewCryto().DeData(password); string(pwd) != u.Password {
		return false
	}
	return true
}

func (u *UserDto) AddUser() bool {
	sql := `
	INSERT INTO user(username, password) VALUES(?, ?)
	`
	pwd, _ := utils.NewCryto().EnData([]byte(u.Password))
	stmt, _ := utils.Db.Prepare(sql)
	_, err := stmt.Exec(u.Username, pwd)
	return err == nil
}

func (u *UserDto) GetUser() (interface{}, error) {
	sql := `SELECT username FROM user;`
	var name string
	var names []string
	if rows, err := utils.Db.Query(sql); err != nil {
		return nil, err
	} else {
		defer rows.Close()
		for rows.Next() {
			rows.Scan(&name)
			names = append(names, name)
		}
		return names, nil
	}
}
func (u *UserDto) DeleteUser() bool {
	sql := `DELETE FROM user WHERE username = ?`
	stmt, err := utils.Db.Prepare(sql)
	if err != nil {
		return false
	}
	result, err := stmt.Exec(u.Username)
	if err != nil {
		return false
	}
	_, err = result.RowsAffected()
	return err == nil
}
