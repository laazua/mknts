#include <iostream>
#include "calc.h"

using namespace std;

int main(void)
{
    Calc c(6, 3);
    cout << "加法: " << c.add() << endl;
    cout << "减法: " << c.sub() << endl;
    cout << "乘法: " << c.mul() << endl;
    cout << "除法: " << c.div() << endl;

    return 0;
}
