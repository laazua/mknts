#include <iostream>

#include "calculate.h"
#include "student.h"

// 混编译在c++文件中
// 用以下方式引入c头文件
extern "C" {
    #include "person.h"
}

using namespace std;

int main(void)
{
    // 测试类
    Calculate c(200, 100);
    std::cout << c.add() << endl;
    std::cout << c.sub() << endl;
    std::cout << c.mul() << endl;
    std::cout << c.div() << endl;
    
    // 测试c代码调用1
    const Person person = {.num = 12, .name = "张三"};
    say_num(person);
    say_name(person);

    // 测试c代码调用2
    study();

    return 0;
}

