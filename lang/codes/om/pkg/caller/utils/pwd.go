// password hash and very
package utils

import "golang.org/x/crypto/bcrypt"

func HashPwd(pwd []byte) string {
	if hash, err := bcrypt.GenerateFromPassword(pwd, bcrypt.MinCost); err != nil {
		return ""
	} else {
		return string(hash)
	}
}

func VeryPwd(hashPwd, plainPwd string) bool {
	if err := bcrypt.CompareHashAndPassword([]byte(hashPwd), []byte(plainPwd)); err != nil {
		return false
	} else {
		return true
	}
}
