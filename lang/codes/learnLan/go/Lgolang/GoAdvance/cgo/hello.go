package main

/*
#include <stdio.h>
#include "hello.h"
static void SayHello(const char *s) {
    puts(s);
}
 */
import "C"

func main()  {
	//没有释放C语言创建的字符串会导致内存泄露,但是对于小程序来说没问题.程序退出时,操作系统会自动回收程序的所有资源
	//C.puts(C.CString("hello, world"))
	//C.SayHello(C.CString("你好, 世界"))
	C.SayGoodbye(C.CString("goodbye"))
}
