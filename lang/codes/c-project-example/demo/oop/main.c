#include <stdio.h>
#include <stdlib.h>

// 定义一个结构体作为类
typedef struct {
    int num1;
    int num2;
    int (*add)(int, int);
} Math;

// 定义一个函数作为类的方法
int add(int num1, int num2) {
    return num1 + num2;
}

// 定义一个函数用于创建类的实例
Math* create_math(int num1, int num2) {
    Math* math = (Math*) malloc(sizeof(Math));
    math->num1 = num1;
    math->num2 = num2;
    math->add = add;
    return math;
}

// 定义一个函数用于销毁类的实例
void destroy_math(Math* math) {
    free(math);
}

int main() {
    // 创建类的实例
    Math* math = create_math(1, 2);
    // 调用类的成员函数
    printf("%d\n", math->add(math->num1, math->num2));
    // 销毁类的实例
    destroy_math(math);
    return 0;
}
