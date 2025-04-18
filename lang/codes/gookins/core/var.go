package core

import (
	"errors"
	"sync"

	"gorm.io/gorm"
)

var (
	once sync.Once

	Db     *gorm.DB
	Config config
	Tp     *TaskPool

	ErrCreateToken    = errors.New("创建token失败")
	ErrUnexpSigMethod = errors.New("未知的签名方法")
	ErrParseToken     = errors.New("验证token失败")
	ErrTokenExpire    = errors.New("token已经过期")
	ErrTokenVaild     = errors.New("token不可用")
)
