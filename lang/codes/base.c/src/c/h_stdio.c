#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp = fopen("../test.txt", "ab+");
    if (fp == NULL) {
        fprintf(stderr, "open file failure!\n");
        return -1;
    }

    // 写入数据
    char wbuffer[] = "this is a example!\n";
    fwrite(wbuffer, sizeof(char), strlen(wbuffer), fp);

    // 读取数据
    char rbuffer[512];
    fread(rbuffer, sizeof(char), strlen(rbuffer), fp);
    printf("%s\n", rbuffer);

    fclose(fp);

    return 0;
}
