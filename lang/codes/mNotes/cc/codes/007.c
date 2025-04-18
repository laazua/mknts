// 程序控制
#include <stdio.h>

int main(void) {
    // if-else
    int num = 5;
    if (num >3) {
        printf("xxx\n");
    } 
    else if (num < 2) {
        printf("yyy\n");
    } 
    else {
        printf("ooo\n");
    }

    // 条件逻辑只有单句结构可以简写:
    // if (num > 3)
    //     printf("xxx\n");
    // else if (num < 2)
    //     printf("yyy\n");
    // else
    //     printf("ooo\n");    

    // for loop
    int i;
    for(i=0;i<num;i++) {
        printf("%d\n", i);
    }

    // while loop
    while(i<6) {
        printf("while\n");
        i++;
    }

    // do while loop
    do {
        printf("do\n");
        i++;
    }
    while(i<10);

    // break, continue

    // switch case
    char ch = 'a';
    switch(ch) {
        case 'a':
            printf("a = %d\n", ch);
            break;
        case 'b':
            printf("b = %d\n", ch);
            break;
        default:
            printf("hahaha\n");
    }

    // goto label
    while(i<100) {
        if(i == 20) {
            goto jump;
        }
        i++;
    }

jump:
    printf("goto\n");

    return 0;
}
