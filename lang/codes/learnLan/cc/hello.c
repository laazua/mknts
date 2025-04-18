/*
https://www.tutorialspoint.com/tutorialslibrary.htm

c程序组成:
    -- 预处理命令
    -- 函数
    -- 变量
    -- 语句和表达式
    -- 注释
    
setup:
    1. 定义程序的目标
    2. 设计程序
    3. 编写代码
    4. 编译
    5. 运行程序
    6. 测试和调试程序
    7.维护和修改程序

gcc == (cc, clang)

程序编译调用不同的c标准:
    gcc -std=c99 hello.c
    gcc -std=c1x hello.c
    gcc -std=c11 hello.c

命名:
    1. 小写字母，大写字母，数字和下划线给变量或函数或结构体命名.
    2. 命名的字符不要超过63个字符.
    3. 命名要做到见名知义，如果不能就要解释说明该命名的意义.

关键字&&保留标识符:
    auto        extern         short       while
    break       float          signed      _Alignal
    case        for            sizeof      _Alignof
    char        goto           static      _Atomic
    const       if             struct      _Bool
    continue    inline         switch      _Complex
    default     int            typedef     _Generic
    do          long           union       _Imaginary
    double      register       unsigned    _Noreturn
    else        restrict       void        _Static_assert
    enum        return         volatile    _Thread_local 

变量类型:
    -- int(short,long，signed,unsigned)
    -- float(short,long,signed,unsigned)
    -- double(short,long,signed,unsigned)
    -- char(属于int型的一种)
    -- _Bool
    -- enum
    指针类型
    结构体类型
    联合类型
    空类型(void)

定义符号常量:
    #define 标识符 常量     --      #define PI 3.14

常量：
    const

类型转换:
    -- 不同数据对象进行操作,会数据转换

运算符：
    -- sizeof运算符
    -- 算数：+  -  *  /  %  ++  --
    -- 关系：>  <  >=  <=  !=  ==
    -- 逻辑：!  &&  ||
    -- 位：<<  >>  ~  |  ^  &
    -- 赋值：=
    -- 条件：表达式1?表达式2:表达式3

结构控制：
    ////
    if (表达式) {
        ...
    }
    ////
    if (表达式) {
        ...
    }
    else if (表达式) {
        ...
    }
    else {
        ...
    }
    ////
    switch (表达式) {
        case 常量表达式1: 语句或程序块1
        case 常量表达式2: 语句或程序块2
        ...
        default: 语句或程序块
    }
    ////
    while (条件) {
        ...
    }
    ////
    do {
        ...
    } while (条件);
    ////
    for (初始化;条件判断;更新) {
        ...
    }
    ////
    break && continue

数组：
    -- char array[] = {'h', 'e', 'l', 'l', '0', '\0'};
    -- int array[100];

字符串处理：
    -- 字符串实际上是由空字符"\0"终止的一维字符数组,因此，以 null 结尾的字符串包含组成字符串的字符，后跟一个null
    -- char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    -- char greeting[] = "hello" 

    -- <string.h>
    -- strcat(字符串连接)
    -- strcmp(字符串比较)
    -- strcpy(字符串拷贝)
    -- strlen(字符串长度)
    ...

指针:
   -- type *varName;

    -- char a = 'c';
       char *p = &a;
    -- 指针&&数组
       指针是一个左值,数组名只是一个地址
    -- 指针数组 && 数组指针
       int *p1[5];   指针数组    是一个数组
       int (*p2)[5]; 数组指针    是一个指针
    -- void指针(万能指针,可以指向任意类型,不能解引用,强转类型后可以解引用)
       指针解引前要检查指针是否为NULL
    -- NULL指针 == #define NULL ((void *)0)

结构体:
    struct [structure tag] {
        member definition;
        member definition;
        ...
        member definition;
    } [one or more structure variables];

    struct Books {
        char title[50];
        char author[50];
        char subject[100];
        int  id;
    } book;

    -- 访问成员(.)


联合:
    union [union tag] {
        member definition;
        member definition;
        ...
        member definition;
    } [one or more union variables];

    union Data {
        int i;
        float f;
        char str[20];
    } data;

    -- 访问成员(.)

位域:
    struct {
        type varName: width;
    };

    struct {
        int aa: 2;
    } status;

typedef:
    typedef type newType;
    typedef unsigned char BYTE;

    -- typedef解释由编译器执行，而#define语句由预处理器处理

预处理:
    -- 文本替换

    -- #define
       替换预处理器宏

    -- #include     
       引入头文件

    -- #undef
       取消定义预处理器宏

    -- #ifdef
       如果定义了此宏，则返回 true

    -- #ifndef
       如果未定义此宏，则返回 true

    -- #if
       测试编译时条件是否为真

    -- #else
       #if 的替代方案

    -- #elif
       #else 和 #if 在一个语句中

    -- #endif
       有条件地结束预处理器

    -- #error
       在 stderr 上打印错误消息

    -- #pragma
       使用标准化方法向编译器发出特殊命令

    -- 预处理器运算符
       宏连续 (\) 运算符： 宏通常限于一行。宏继续运算符 (\) 用于继续一个对于单行来说太长的宏
       #define  message_for(a, b)  \
           printf(#a " and " #b ": We love you!\n")
       
       字符串化 (#) 运算符: 字符串化或数字符号运算符 ( '#' ) 在宏定义中使用时，将宏参数转换为字符串常量。此运算符只能在具有指定参数或参数列表的宏中使用
        #define  message_for(a, b)  \
           printf(#a " and " #b ": We love you!\n")

        int main(void) {
        message_for(Carole, Debra);
        return 0;
        }

        令牌粘贴 (##) 运算符: 宏定义中的标记粘贴运算符 (##) 组合了两个参数。它允许将宏定义中的两个单独标记合并为一个标记
        #include <stdio.h>

        #define tokenpaster(n) printf ("token" #n " = %d", token##n)

        int main(void) {
        int token34 = 40;
        tokenpaster(34);
        return 0;
        }
        这个例子展示了 token##n 到 token34 的连接，这里我们同时使用了stringize和token- pasting

        Defined() 运算符: 预处理器定义的运算符用于常量表达式，以确定是否使用 #define 定义了标识符。如果定义了指定的标识符，则该值为真（非零）。如果未定义符号，则值为假（零）
        #include <stdio.h>

        #if !defined (MESSAGE)
        #define MESSAGE "You wish!"
        #endif

        int main(void) {
        printf("Here is the message: %s\n", MESSAGE);  
        return 0;
        }

        参数化宏: 带参数的宏在使用前必须使用#define指令定义。参数列表括在括号中，并且必须紧跟在宏名称之后。宏名称和左括号之间不允许有空格
        #include <stdio.h>

        #define MAX(x,y) ((x) > (y) ? (x) : (y))

        int main(void) {
        printf("Max between 20 and 10 is %d\n", MAX(10, 20));  
        return 0;
        }

头文件:
    -- 头文件是扩展名为.h的文件，其中包含要在多个源文件之间共享的 C 函数声明和宏定义。头文件有两种类型：程序员编写的文件和编译器附带的文件。
    -- 包含系统头文件: 在系统目录的标准列表中搜索名为“file”的文件。您可以在编译源代码时使用 -I 选项将目录添加到此列表中
       #include <file>
    -- 包含自己头文件: 在包含当前文件的目录中搜索名为“file”的文件。您可以在编译源代码时使用 -I 选项将目录添加到此列表中
       #include "file"

类型转换:
    (typeName) expression

错误处理:
    -- <error.h>

内存管理:
    -- <stdlib.h>
    void *calloc(int num, int size);
      此函数分配一个由num 个元素组成的数组，每个元素的大小（以字节为单位）都是size
    void free(void *address);
      该函数释放由地址指定的一块内存块
    void *malloc(size_t size);
      此函数分配一个num字节数组，并保持它们未初始化
    void *realloc(void *address, int newsize);
      此函数重新分配内存，将其扩展到newsize

    -- 动态分配内存,例子:
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>

        int main() {
            char name[100];
            char *description;

            strcpy(name, "Zara Ali");

            //allocate memory dynamically 
            description = malloc( 200 * sizeof(char) );
                
            if( description == NULL ) {
                fprintf(stderr, "Error - unable to allocate required memory\n");
            } else {
                strcpy( description, "Zara ali a DPS student in class 10th");
            }
            
            printf("Name = %s\n", name );
            printf("Description: %s\n", description );
             
            //release memory using free() function
            free(description);
        }

命令行参数: 
    -- argc是指传递的参数数量，而argv[]是指向传递给程序的每个参数的指针数组
    -- argv[0]保存了程序本身的名称，argv[1]是指向提供的第一个命令行参数的指针，而 *argv[n] 是最后一个参数
    #include <stdio.h>

    int main( int argc, char *argv[] )  {
        if( argc == 2 ) {
            printf("The argument supplied is %s\n", argv[1]);
        }
        else if( argc > 2 ) {
            printf("Too many arguments supplied.\n");
        }
        else {
            printf("One argument expected.\n");
        }
    }
    

*/
#include <stdio.h>

int main(int argc, char *argv[]) 
{

    printf("hello world.\n");
    return 0;
}