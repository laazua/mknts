package main

import (
  "fmt"
)


//定义一个学生类型的结构体,属性字段包括名字,年龄,学号
type Student struct{
  name string
  age int
  id int
}


//跟Student结构体有相同的底层类型
type alias_t Student


func instanceStruct1() *Student{
  //创建一个Student结构体指针, 等价于 var s *Student = new(Student)
  s := new(Student)

  //对结构体进行具像化,即给属性赋值
  s.name = "bobo"
  s.age = 16
  s.id = 2
  //或者如下进行赋值
  //s := &Student{"bobo", 16, 2}
  //var s Student = Student{"bobo", 16, 2}

  return s
  //return &Student{"lili", 15, 1}
}


func instanceStruct2(p *Student) *Student{
  p.name = "qiqi"
  p.age = 18
  p.id = 3

  return p
}



//使用工厂方法创建结构体实例
type File struct {
  fd int
  name string
}
//File结构体对应的工厂方法，它返回一个指向结构体实例的指针
func NewFile(fd int, name string) *File {
  if fd < 0{
    return nil
  }

  return &File{fd, name}
}


func main(){
  //s := new(Student)
  s := instanceStruct1()
  fmt.Println(s)

  s = instanceStruct2(s)
  fmt.Println(s)

  //工厂方法调用
  //f := NewFile(10, "./test.txt")
}
