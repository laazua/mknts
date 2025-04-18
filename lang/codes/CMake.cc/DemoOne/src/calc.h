// calc

#ifndef _CALC_H_
#define _CALC_H_

class Calc {
private:
    int m;
    int n;
public:
    Calc(int m, int n);
    int add(void);
    int sub(void);
    int mul(void);
    int div(void);
};

#endif // _CALC_H_
