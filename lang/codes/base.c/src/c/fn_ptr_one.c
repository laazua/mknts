/*
* 回调
*/
#include <stdio.h>

// 回调类型
typedef void (*CallBackFn)(int);

// 注册回调函数
void RegisterFun(CallBackFn fn)
{
    //调用回调函数
    fn(250);
}

// 实现回调函数
void MCallBack(int value)
{
    fprintf(stdout, "callback invoke with value: %d\n", value);
}

int main()
{
    RegisterFun(MCallBack);
    
    return 0;
}
