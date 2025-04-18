#include <iostream>

// 类中的匿名函数
class Lambda
{
private:
    int value;
public:
    void set_value(int v) {
         auto set = [this](int v) {
             value = v;
         };
         set(v);
    }
    int get_value() {
         auto get = [this]() {
             return value;
         };
         return get();
    }
};

int main()
{
    Lambda lambda;
    lambda.set_value(100);

    std::cout << lambda.get_value() << std::endl;

    // [capture list] (parameters) -> return_type { 函数体 }
    // capture list: 用来捕获外部变量，在lambda表达式内部可以使用外部作用域的变量。捕获列表可以为空，也可以通过值捕获、引用捕获等方式捕获外部变量
    // parameters: 形参列表，与普通函数的形参列表类似，可以为空
    // return_type: 返回类型，可以省略，编译器会自动推导返回类型
    // {}: 函数体，与普通函数体一样，用来定义函数的执行逻辑
    auto num = 10;
    auto add = [&num](int other) -> int { return num + other; };
    std::cout << "lambda func: " << add(20) << std::endl;

    return 0;
}

// g++ lambda.cc -std=c++11
