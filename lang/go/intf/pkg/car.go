package pkg

import "fmt"

// 汽车接口
type Car interface {
	Run()
}

// 实例化 baoMa 汽车
func NewBaoMa(name string) *baoMa {
    return &baoMa{
        name: name,
    }
}

// baoMa 类不允许导出
// baoMa 汽车实现Car接口
type baoMa struct{
    name string
}

func (b *baoMa) Run() {
	fmt.Println(b.name + " running ...")
}

// 实例化 benZi 汽车
func NewBenZi(name string) *benZi {
    return &benZi{
        name: name,
    }
}

// benZi 类不允许导出
// benZi 汽车实现Car接口
type benZi struct{
    name string
}

func (b *benZi) Run() {
    fmt.Println(b.name + " running ...")
}

// 确保 *BaoMa|*BenZi 类型实现了 Car 接口.
// 如果 *BaoMa|*BenZi 类型没有正确实现 Car 接口,
// 编译器会在编译时产生错误, 这样可以在编译前就发现接口实现的问题，提前修复
// var _ Car = (*BaoMa)(nil)
// var _ Car = (*BenZi)(nil)
