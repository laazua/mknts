#include <stdio.h>
//#define NDEBUG // 禁用assert()调用
#include <assert.h>

int main()
{
     assert(2<1);
     fprintf(stderr, "hello world");
     return 0;
}
