//接口是一组方法的签名，所有实现了接口中方法的类型都满足该接口；即所有需要接口的地方都可以传递接口中的方法所绑定的类型的实例
//接口可以被任意对象实现，只要接口中的方法被绑定到了一个对象上，那么该接口就可以被该对象实现；一个对象可以实现任意多个接口
//一个类型的实例实现了一个接口，则该实例可以执行该接口中的方法(接口中的所有方法必须与类型绑定的方法一致)
//interface{}类型可以存放一切类型
package main

import (
  "fmt"
)

//定义一个接口
type Shaper interface{
  Area() float32
}

//定义一个正方形结构体
type Square struct{
  side float32
}

//定义一个方形接口
type Rectangle struct{
  length, width float32
}

//Square结构体实现Area()方法
func (sq Square)Area() float32 {
  return sq.side * sq.side
}

//Rectangle结构体实现Area()方法
func (re Rectangle)Area() float32{
  return re.length * re.width
}

func main(){
  //sq1 := new(Square)    创建一个Square结构体指针,等价于sq1 *Square = new(Square)
  //sq1.side = 5          通过sq1指针给Square属性side赋值5
  //areaIntf := sq1       声明一个sq1类型的指针
  //fmt.Printf("The square has area: %f\n", areaIntf.Area())
  r := Rectangle{5, 3}    //声明并初始化一个Rectangle结构体对象
  q := Square{5}          //声明并初始化一个Square结构体对象
  s := []Shaper{r, q}     //声明并初始化一个接口对象
  for n, _ := range s{
    fmt.Println("Shape details: ", s[n])
    fmt.Println("Area: ", s[n].Area())
  }
}
