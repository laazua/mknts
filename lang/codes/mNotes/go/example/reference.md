###### 引用类型

* *slice*  [示例](/golang/example/slice.go)
```
  make()函数创建: make([]type, len, cap)
  arra := [...]int{0,1,2,3,4,5,6,7,8,9}   // 数组赋值并初始化
  slice := arra[:]   // 切片引用数组
```

* *map*  [示例](/golang/example/map.go)
```
  make()函数创建: m := make(map[string]int, 5)
  var m map[string]int = {"a":1, "b":2}
```

* *channel*  [示例](/golang/example/chan.go)
```
  make()函数创建: ch := make(chan int, 10)  // 有缓冲
  var ch chan int = make(chan int)  // 无缓冲
  var ch chan string = make(chan string)  // 无缓冲
```

* *new()*  [示例](/golang/example/new.go)
```
  用于给某个类型在堆内存上申请存储地址,返回的是对应类型的指针,用来创建值类型
```

* *make()*
```
  用于给slice, map, channel在堆上分配内存和初始化成员结构，返回对象而非指针
```