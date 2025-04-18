#include <iostream>
using namespace std;

int main() {
    cout << "hello c++" << endl;
    return 0;
}

/*
变量: 用于管理内存.
创建变量:  数据类型  变量名 = 变量初始值;

常量: 标记程序中不可更改的数据.
创建常量: 
    宏常量: #define 常量名 常量值  (通常定义在文件的开头)
    const修饰的变量: const 数据类型 常量名 = 常量值;

c++关键字:
    asm             do              if                return              typedef
    auto            aouble          inline            short               typeid
    bool            dynamic_cast    int               signed              typename
    break           else            long              sizeof              union
    case            enum            mutable           static              unsigned
    catch           explicit        namespace         static_cast         using
    char            export          new               struct              virtual
    class           extern          operator          switch              void
    const           false           private           template            volatile
    const_cast      float           protected         this                wchar_t
    continue        for             public            throw               while
    default         friend          register          true
    delete          goto            reinterpret_cast  try  

标识符命名规则:
    -- 标识符不能是关键字
    -- 标识符只能是字母数字下划线组成
    -- 第一个字符必须是字母和下划线
    -- 标识符中的字母是区分大小写的

数据类型：
    sizeof关键字统计数据类型所占内存大小
    整型：short, int, long, long long
    浮点型: float, double
    字符型: char
            char ch = '2';
    字符串型: c风格 => char 变量名[] = "字符串值";
             c++风格 => string 变量名 = "字符串值";
    布尔类型: bool flag = true;

运算符号:
    -- 算数运算
        +  -  *  /  %  ++  --
    -- 赋值运算
        =  +=  -=  *=  /=  %= 
    -- 比较运算
        ==  !=  <  >  <=  >=
    -- 逻辑运算
        !  &&  ||
    -- 三目运算符
        ? :

程序流程结构
    -- 顺序结构
    -- 选择结构
        单行格式if语句: 
        if(条件) {
            ...
        }
        else {
            ...
        }
        多行格式if语句:
        if(条件1) {
            ...
        }
        else if(条件2) {
            ...
        }
        ...
        else {
            ...
        }
        if嵌套！
        
        三目运算:
            表达式1?表达式2：表达式3
        
        switch(表达式) {
            case 结果1:  执行语句; break;
            case 结果2:  执行语句; break;
            ...
            default: 执行语句; break;
        }
    -- 循环结构
        while(条件) {
            ...
        }

        do {
            ...
        } while(条件);

        for(起始表达式;条件表达式;末尾循环体) {
            ...
        }

        break && continue

        goto 标记;

数组:
    数据类型 数组名[长度];
    数据类型 数组名[长度] = {值1, 值2, ...};
    数据类型 数组名[] = {值1, 值2, ...};

函数:
    返回类型 函数名 (参数类表) {
        函数体语句
        return 表达式;
    }

指针:
    数据类型* 变量名;
    int a = 10;
    int* p;
    //指针变量赋值
    p = &a;
    cout << &a << endl;  //打印数据a的地址
    cout << p << endl;   //打印指针变量p
    //指针的使用,通过*操作指针变量指向的内存地址
    cout << *p << endl;

    //空指针,初始化指针变量
    int* p = NULL;

    //野指针,指针变量指向非法的内存空间,程序中避免野指针
    int* p = (int*)0x1100;

    指针与数组
    指针与函数

结构体:
    struct 结构体名 {
        结构体成员列表
    };
    通过.访问结构体变量的属性

    结构体数组: 数组中的数据类型是结构体.
    结构体指针: 通过指针访问结构体中的成员, 利用操作符-> 可以通过结构体指针访问结构体属性.

    结构体嵌套结构体
*/  