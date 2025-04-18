#include <stdio.h>

// 枚举
enum color {red=1, yellow, green, oringe};

int main(void)
{
    int i;
    printf("输入颜色代码: ");
    scanf("%d", &i);
    switch (i) {
    case red:
        printf("red\n");
        break;
    case yellow:
        printf("yellow\n");
        break;
    case green:
        printf("green\n");
        break;
    case oringe:
        printf("oringe\n");
        break;
    default:
        printf("no color\n"); 
        break;
    }

    printf("%d\n", oringe);
    return 0;
}
