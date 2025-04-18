package model

type Node struct {
	Name    string `gorm:"name"`
	Ip      string `gorm:"ip"`
	SshPort uint   `gorm:"sshPort"`
}
