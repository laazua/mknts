#include <string>
#include <iostream>

class Person
{
private:
    std::string name;
public:
    // 静态变量在所有对象中共享
    static std::string Address;
    Person(std::string name) {
        this->name = name;
    }
    void PrintAddress() {
        std::cout << this->name << std::endl;
        std::cout << this->Address << std::endl;
    }
};

// 类的静态变量必须在类外进行声明和初始化
std::string Person::Address = "beijingshi";

int main()
{
    Person p1("张三");
    p1.PrintAddress();

    Person p2("李四");
    p2.PrintAddress();

    return 0;
}
