//该示例展示在go中如何使用hash password
//go get  golang.org/x/crypto/bcrypt
package main

import (
	"fmt"
	"golang.org/x/crypto/bcrypt"
)

func HashPassword(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), 14)
	return string(bytes), err
}

func CheckPasswordHash(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nill
}

func main(){
	password := "secret"
	hash, _ := HashPassword(password)  //ignore error for the sake of simplicity

	fmt.Println("Password: ", password)
	fmt.Println("Hash:     ", hash)

	match := CheckPasswordHash(password, hash)
	fmt.Println("Match:    ", match)
}