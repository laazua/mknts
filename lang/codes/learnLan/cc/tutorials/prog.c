// 程序结构

// 局部变量: 声明在函数内部的变量
int test_local_variable(void)
{
    // 变量a只在test_local_variable函数内部有效(自动存储等价:auto int a)
    // 变量a在函数返回后失效
    int a;  
}

int test_static_variable(void)
{
    // 静态变量a在程序的整个执行期间都有效(静态存储)
    // 变量a在函数返回后仍有效，但是该变量只在函数作用域内有效
    // 将来调用同一个函数,该变量上的数据仍可以用
    static int a;  
}

int test_argument_variable(int a)
{
    // 形参a和局部变量有一样的性质(即自动存储: auto)
}

// 外部变量(全局变量): 声明在任何函数体外
// 拥有静态存储期限(即保存早外部变量上的值在程序整个生命期有效)
// 外部变量作用在本文件作用域, 声明在外部变量后的函数都可以访问它
int a;