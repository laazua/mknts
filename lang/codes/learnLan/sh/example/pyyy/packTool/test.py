#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#print("\t{0}{1:*>20}{2:*>20}\n".format("AppID", "AppName", "描述"))

import sys
#a = 1

def foo():
    #global  b
    a = 1
    if a == 1:
        b = 2
    return b

if __name__ == '__main__':
    c = foo()
    print(c)
    sys.stdout.write("aaaa:")
    sys.stdout.flush()
    aa = input("bb")
    print(aa)