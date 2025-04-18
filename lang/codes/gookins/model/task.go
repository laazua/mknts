package model

import "gorm.io/gorm"

type Task struct {
	gorm.Model
	Name        string `gorm:"name"`
	Description string `gomr:"description"`
	PipeLine    string `gorm:"pipeline;type:text"`
	Disabled    bool   `gorm:"disabled;default:false"`
}

type TaskForm struct {
	Id          string `form:"id"`
	Name        string `form:"name" binding:"required"`
	Description string `form:"description" binding:"required"`
	PipeLine    string `form:"pipeline" binding:"required"`
}
