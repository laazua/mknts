#include <iostream>
#include "calc.h"
#include "bubble.h"

using namespace std;

int main(void)
{
    Calc c(6, 3);
    cout << "加法: " << c.add() << endl;
    cout << "减法: " << c.sub() << endl;
    cout << "乘法: " << c.mul() << endl;
    cout << "除法: " << c.div() << endl;

    int numbers[4] = {10, 6 ,7, 78};
    Bubble b(4, numbers);
    b.sort();

    return 0;
}
