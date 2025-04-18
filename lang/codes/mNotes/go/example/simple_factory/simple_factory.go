package simplefactory

import "fmt"

// 对外暴露的接口
type SimpleApi interface {
	Sing() string
}

// 创建SimpleApi接口实例的函数
func NewSimpleApi(name string) SimpleApi {
	switch name {
	case "cat":
		return &Cat{
			Name: name,
		}
	case "dog":
		return &Dog{
			Name: name,
		}
	default:
		return nil
	}
}

// 实现了SimpleApi接口的类
type Cat struct {
	Name string
}

func (c *Cat) Sing() string {
	fmt.Println(c.Name)
	return c.Name
}

// 实现了SimpleApi接口的类
type Dog struct {
	Name string
}

func (d *Dog) Sing() string {
	fmt.Println(d.Name)
	return d.Name
}
