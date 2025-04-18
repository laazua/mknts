#include <iostream>
#include "calculate.h"

using namespace std;

// 构造函数
Calculate::Calculate(int a, int b)
{
    this->a = a;
    this->b = b;
}

// 析构函数
Calculate::~Calculate(void)
{
    std::cout << "析构函数: 无参数,无返回值\n";
}

int Calculate::add(void)
{
    return this->a + this->b;
}

int Calculate::sub(void)
{
    return this->a - this->b;
}

int Calculate::mul(void)
{
    return this->a * this->b;
}

int Calculate::div(void)
{
    return this->a / this->b;
}
