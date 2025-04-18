#include "namespace.hh"

namespace ABC {

Person::Person()
{
    std::cout << "构造函数" << std::endl;
}

Person::~Person()
{
    std::cout << "析构函数" << std::endl;
}

void Person::say_hello()
{
    std::cout << "hello world" << std::endl;
}

}  // namespace ABC
