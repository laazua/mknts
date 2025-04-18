#include <string>
#include <iostream>

class Person {

private:
    std::string name;
    std::string addr;
public:
    Person(std::string name, std::string addr) {
        this->name = name;
        this->addr = addr;
    }
    void PrintName() {
        std::cout << this->name << std::endl;
    }
    void PrintAddr() {
        std::cout << this->addr << std::endl;
    }
    // 友元(函数或类)可以声明在类中的任何位置
    friend void PrintNameAddr(Person *p) {
        std::cout << p->name + ": "  + p->addr << std::endl;
    }
    ~Person() {
        std::cout << "一些清理工作." << std::endl;
    }
};

int main()
{
    Person p("zhangsan", "beijingshi");
    p.PrintName();
    p.PrintAddr();
    PrintNameAddr(&p);

    return 0;
}
