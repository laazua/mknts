//反射 reflect包
package main

import (
	"fmt"
	"reflect"
)

type Human struct {
	Name    string    `json:"name"`
	Age     int       `json:"age"`
}

func main(){
	person := Human{"bobo", 24}
	//使用reflect,分三步:
	//第一步,转化为reflect对象
	obj1 := reflect.TypeOf(person)      //得到元数据,通过obj1能获取x类型定义里面的所有元素
	obj2 := reflect.ValueOf(&person)     //得到实际值,通过ob获2取存储在x里面的值,还可以去改变x的值
	tag1 := obj1.Field(0).Tag
	tag2 := obj2.Type()

	fmt.Println(obj2.Elem())

	fmt.Println(tag1)
	fmt.Println(tag2)
	fmt.Println(person.Age)
}
