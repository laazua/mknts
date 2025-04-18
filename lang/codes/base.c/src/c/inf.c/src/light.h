#ifndef __LIGHT_H
#define __LIGHT_H

typedef int (*LightOnFun)(void *self);
typedef int (*LightOffFun)(void *self);
typedef int (*LightStateFun)(void *self);

struct LightInterface {
    LightOnFun on;
    LightOffFun off;
    LightStateFun state;
};

// 从 self(即接口) 指针中解引用并调用相应的操作函数
static inline int LightOn(void *self)
{
    // self 是一个指向 struct LightInterface * 类型的指针的指针 (struct LightInterface **)。
    // *(struct LightInterface **)self 将 self 从 struct LightInterface ** 类型转换为 struct LightInterface * 类型，并解引用以获取实际的 LightInterface 结构体。
    // ->on(self) 是通过 LightInterface 结构体中的函数指针调用相应的函数。
    return (*(struct LightInterface **)self)->on(self);
}

static inline int LightOff(void *self)
{
    return (*(struct LightInterface **)self)->off(self);
}

static inline int LightState(void *self)
{
    return (*(struct LightInterface **)self)->state(self);
}

#endif // __LIGHT_H
