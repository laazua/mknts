#include <dlfcn.h>
#include "operation.h"


int main()
{
    /* 函数指针加载动态库 */
    void *lib_handle = dlopen("./operation.so", RTLD_LAZY);
    if (!lib_handle) {
        fprintf(stderr, "加载动态库失败!\n");
        return -1;
    }
    
    /* 从动态库中获取函数指针 */
    // 获取 |int add(int, int)| 函数
    Operation add = (Operation)dlsym(lib_handle, "add");
    if (!add) {
        fprintf(stderr, "获取add()函数失败!\n");
        dlclose(lib_handle);
        return -2;
    }
    fprintf(stderr, "lib.so add result: %d\n", add(2, 3));
    // 获取 |int sub(int, int)| 函数
    Operation sub = (Operation)dlsym(lib_handle, "sub");
    if (!sub) {
        fprintf(stderr, "获取sub()函数失败!\n");
        dlclose(lib_handle);
        return -2;
    }
    fprintf(stderr, "lib.so sub result: %d\n", sub(2, 3));

    // 关闭动态库句柄
    dlclose(lib_handle);

    return 0;
}

