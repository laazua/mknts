#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
// 获取命令行参数的头文件
//#include <getopt.h>
int main(int argc, char *argv[]) {
    int opt;

    // 使用循环逐个解析选项
    while ((opt = getopt(argc, argv, "a:b:cd")) != -1) {
        switch (opt) {
            case 'a':
                printf("选项 -a，参数：%s\n", optarg);
                break;
            case 'b':
                printf("选项 -b，参数：%s\n", optarg);
                break;
            case 'c':
                printf("选项 -c\n");
                break;
            case 'd':
                printf("选项 -d\n");
                break;
            case '?':
                printf("无效的选项：%c\n", optopt);
                break;
            default:
                printf("未知选项：%c\n", opt);
                break;
        }
    }

    // 处理剩余的非选项参数
    for (; optind < argc; optind++) {
        printf("非选项参数：%s\n", argv[optind]);
    }

    return 0;
}
