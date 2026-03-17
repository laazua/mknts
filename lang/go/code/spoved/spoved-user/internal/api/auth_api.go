// AuthHandler handles authentication-related requests
package api

import (
	"net/http"
	"spoved-user/internal/dto"
	"spoved-user/internal/service"

	"github.com/gin-gonic/gin"
)

type AuthHandler struct {
	// You can add dependencies here, such as a user service or database connection
	service *service.AuthService
}

func NewAuthHandler() (*AuthHandler, error) {
	service, err := service.NewAuthService()
	if err != nil {
		return nil, err
	}
	return &AuthHandler{
		service: service,
	}, nil
}

// 密码登录接口
func (h *AuthHandler) PwdLogin(ctx *gin.Context) {
	var req dto.PwdLoginRequest
	if err := ctx.ShouldBindJSON(&req); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"code": 400, "message": "Invalid request", "error": err.Error()})
		return
	}
	token, err := h.service.PwdLogin(req.Account, req.Password)
	if err != nil {
		ctx.JSON(http.StatusUnauthorized, gin.H{"code": 401, "message": "Authentication failed", "error": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"code": 200, "message": "Login successful", "data": gin.H{"token": token, "user": req.Account}})
}

// 短信登录接口
func (h *AuthHandler) SmsLogin(ctx *gin.Context) {
	var req dto.SmsLoginRequest
	if err := ctx.ShouldBindJSON(&req); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"code": 400, "message": "Invalid request", "error": err.Error()})
		return
	}
	token, err := h.service.SmsLogin(req.Phone, req.Code)
	if err != nil {
		ctx.JSON(http.StatusUnauthorized, gin.H{"code": 401, "message": "Authentication failed", "error": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"code": 200, "message": "Login successful", "data": gin.H{"token": token, "phone": req.Phone}})
}

// endSMSCode 发送短信验证码接口
func (h *AuthHandler) SendSmsCode(ctx *gin.Context) {
	var req dto.SendCodeRequest
	if err := ctx.ShouldBindJSON(&req); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"code": 400, "message": "Invalid request", "error": err.Error()})
		return
	}
	if err := h.service.SendSmsCode(req.Phone); err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{"code": 500, "message": "Failed to send SMS code", "error": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"code": 200, "message": "SMS code sent successfully"})
}

// 邮箱登录接口
func (h *AuthHandler) EmailLogin(ctx *gin.Context) {
	var req dto.EmailLoginRequest
	if err := ctx.ShouldBindJSON(&req); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"code": 400, "message": "Invalid request", "error": err.Error()})
		return
	}
	token, err := h.service.EmailLogin(req.Email)
	if err != nil {
		ctx.JSON(http.StatusUnauthorized, gin.H{"code": 401, "message": "Authentication failed", "error": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"code": 200, "message": "Login successful", "data": gin.H{"token": token, "email": req.Email}})
}

// 邮箱

// 登出接口
func (h *AuthHandler) Logout(ctx *gin.Context) {
	// Implement logout logic here
}
