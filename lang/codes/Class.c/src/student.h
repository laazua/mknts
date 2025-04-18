// c和c++的链接

#ifndef _STUDENT_H_
#define _STUDENT_H_

#include <stdio.h>

// ==========================
// 开始条件编译
// 判断当前编译环境是否为 C++
#if __cplusplus
extern "C" {
#endif

    // 声明语句
    void study(void);

// 束条件编译块结束
#if __cplusplus
}
#endif
// =========================

#endif // _STUDENT_H_
