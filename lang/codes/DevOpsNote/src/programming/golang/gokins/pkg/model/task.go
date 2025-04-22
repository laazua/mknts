package model

import "time"

// -------task任务--------
type step struct {
	Name string `yaml:"name"`
	Cmd  string `yaml:"cmd"`
}

type task struct {
	Name  string `yaml:"name"`
	Steps []step `yaml:"steps"`
}

type TaskTemplate struct {
	Task task `yaml:"task"`
}

type TaskForm struct {
	Name       string        `json:"name"`
	Webhook    string        `json:"webHook"`
	SecuretKey string        `json:"securetKey"`
	Template   TaskTemplate  `json:"template"`
	IsDelete   bool          `json:"isDelete"`
	CreateTime time.Duration `json:"createTime"`
}
