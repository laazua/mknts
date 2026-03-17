package dto

// LoginRequest 登录请求基类
type LoginRequest struct {
	LoginType string `json:"login_type" binding:"required,oneof=sms password email"`
}

// SMSLoginRequest 短信登录请求
type SmsLoginRequest struct {
	Phone string `json:"phone" binding:"required,len=11"`
	Code  string `json:"code" binding:"required,len=6"`
}

// PasswordLoginRequest 密码登录请求
type PwdLoginRequest struct {
	Account  string `json:"account" binding:"required"` // 可以是手机号或邮箱
	Password string `json:"password" binding:"required,min=6"`
}

// EmailLoginRequest 邮箱免密登录请求
type EmailLoginRequest struct {
	Email string `json:"email" binding:"required,email"`
}

// SendCodeRequest 发送验证码请求
type SendCodeRequest struct {
	Phone string `json:"phone" binding:"required,len=11"`
}
