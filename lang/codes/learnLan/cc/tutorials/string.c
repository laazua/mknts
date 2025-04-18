// 字符串
// 字符串库: <string.h>

void test_string(void)
{
    char *p;
    p = "abcd";    // 将指针指向字符串第一个字符

    int i;
    for(i=0;i<5;i++) {
        if (*p != '\0')
            printf("%c\n", *p);
        p += 1; 
    }
}

int main(void)
{
    test_string();
    return 0;
}