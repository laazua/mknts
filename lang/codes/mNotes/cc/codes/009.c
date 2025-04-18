// 存储类型

#include <stdio.h>


int main(void) {
    // auto, register, extern, static(默认auto)

    int ret1 = auto_add();
    printf("%d\n", ret1);
    
    int ret2 = auto_add();
    printf("%d\n", ret2);

    return 0;
}

int auto_add() {
    static num = 0;
    num++;
    return num;   
}
