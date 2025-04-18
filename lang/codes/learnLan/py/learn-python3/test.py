# -*- coding:utf-8 -*-

sign = 'dDdsfwdf&^%L6fVgPaIf1'

d = {"a":1,"b":2,"c":3,"d":4,"e":9,"f":6,"g":7}
for i in range(len(d)):
    try:
        print(d[i]["d"])
    except:
        print("aa")
