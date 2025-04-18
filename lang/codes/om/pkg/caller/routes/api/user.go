// user api
package api

import (
	"vanGogh/pkg/caller/utils"

	"github.com/gin-gonic/gin"
)

// user login
func CUserSign(ctx *gin.Context) {
	// check user

	utils.Success(ctx, "user sign success", nil)
}

// get user info
func CUserInfo(ctx *gin.Context) {

	utils.Success(ctx, "get user's info", nil)
}

// add user
func CAddUser(ctx *gin.Context) {

	utils.Success(ctx, "add user success", nil)
}

// del user
func CDelUser(ctx *gin.Context) {

	utils.Success(ctx, "del user success", nil)
}

// modify user
func CPutUser(ctx *gin.Context) {

	utils.Success(ctx, "mod user success", nil)
}

// get user list
func CGetUser(ctx *gin.Context) {

	utils.Success(ctx, "get users success", nil)
}
