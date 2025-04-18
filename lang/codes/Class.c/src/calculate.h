#ifndef _CALCULATE_
#define _CALCULATE_

class Calculate
{
private:
    int a;
    int b;
public:
    Calculate(int a, int b);
    ~Calculate(void);
    int add(void);
    int sub(void);
    int mul(void);
    int div(void);
};

#endif // _CALCULATE_
