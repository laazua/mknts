package pkg

// Car 接口
type Car interface {
    Run()
}

// 实例化baoMa
func NewBaoMa(name string) *baoMa {
    return &baoMa{name: name}
}

// baoMa实现Car接口
type baoMa struct {
    name string
}

func (b *baoMa) Run() {
    println(b.name + " Running ...")
}

// 实例化Factory
// 通过依赖注入的方式,注入Car
func NewPeople(car Car) *people{
    return &people{car: car}
}

// people类依赖Car接口
type people struct {
    car Car
}

// 使用Car接口服务
func (p *people) RunCar() {
    p.car.Run()
}
