package main

import "intf/pkg"

func main() {
    baoMa := pkg.NewBaoMa("BaoMa")
    runCar(baoMa)

    benZi := pkg.NewBenZi("BenZi")
    runCar(benZi)
}

// baoMa类和benZi类都依赖Car接口
// 进行调用, 调用者不需要关心他们
// 的具体实现
func runCar(car pkg.Car) {
    car.Run()
}
