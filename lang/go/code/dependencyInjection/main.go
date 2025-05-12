package main

import "dependencyInjection/pkg"

func main() {
    baoMa := pkg.NewBaoMa("BaoMa")
    people := pkg.NewPeople(baoMa)
    people.RunCar()
}
