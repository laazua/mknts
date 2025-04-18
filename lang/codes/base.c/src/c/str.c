#include <stdio.h>
#include <string.h>
#include <ctype.h> // 字符判断头文件

int main()
{
    char a = 'a';
    printf("%c\n", a);
    printf("%d\n", a);

    char *s = "abc";
    printf("%s\n", s);
    size_t slen = strlen(s);
    printf("%ld\n", slen);

    char s1[] = {'a', 'b', 'c'};
    char s2[] = {'a', 'b', 'c', '\0'};
    printf("%s\n", s1);  // out: abcabc
    printf("%s\n", s2);  // out: abc

    size_t s1len = strlen(s1);
    size_t s2len = strlen(s2);
    s1len > s2len ? printf("s1len = %ld\n", s1len) : printf("s2len = %ld\n", s2len);

    // 字符操作
    int r = isalpha('?');
    if (r == 0)
        printf("非字母\n");
    else
        printf("是字母\n");

    return 0;
}
