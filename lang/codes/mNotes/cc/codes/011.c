#include <stdio.h>

#define YES
// 如果YES定义了NUM=5
#ifdef YES
    #define NUM 5
#else
    #define NUM 6
#endif


#define SYS 1

#if SYS == 1
    #define VAL 100
#elif SYS == 2
    #define VAL 200
#else
    #define VAL 300
#endif

#if defined (YES)
    #define STR "YES"
#elif defined (VAL)
    #define STR "VAL"
#else
    #define STR "NIL"
#endif


int main(void) 
{
    printf("%d\n", NUM);
    printf("%d\n", VAL);
    printf("%s\n", STR);

    // 预定义宏
    printf("%s\n", __DATE__);
    printf("%s\n", __TIME__);
    printf("%s\n", __FILE__);
    printf("%d\n", __LINE__);
    printf("%s\n", __func__);
    return 0;
}
