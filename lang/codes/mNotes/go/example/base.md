###### 基本类型

* **bool**
  * *各个类型声明时都有其对应类型的初始默认值* [示例](/golang/example/base.go)
```
  bool类型: 1字节  [默认值: false]
    true, false

  byte类型: 1字节  [默认值: 0]
    uint8

  rune类型: 4字节  [默认值: 0]
    Unicode Code, Point, int32

  int,unit类型: 4或8字节  [默认值: 0]
    32位或64位

  int8,unit8类型: 1字节  [默认值: 0]
    uint8 == byte

  int16,uint16类型: 2字节  [默认值: 0]

  int32,uint32类型: 4字节  [默认值: 0]
    uint32 == rune

  int64,uint64类型: 8字节  [默认值: 0]

  float32类型: 4字节  [默认值: 0.0]

  float64类型: 8字节  [默认值: 0.0.]

  complex64类型: 8字节

  complex128类型: 16字节

  uintptr类型: 4或8字节
    存储指针类型: uint32或uint64

  array类型
    值类型

  struct类型
    值类型

  string类型  [默认值: ""]
    UTF-8字符串

  slice类型   [默认值: nil]
    引用类型

  map类型     [默认值: nil]
    引用类型

  channel类型  [默认值: nil]
    引用类型

  interface类型  [默认值: nil]
    接口类型

  func类型     [默认值: nil]
    函数类型
```