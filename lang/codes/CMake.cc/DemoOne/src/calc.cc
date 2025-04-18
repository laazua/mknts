#include "calc.h"


Calc::Calc(int m, int n)
{
    this->m = m;
    this->n = n;
}

int Calc::add(void)
{
    return this->m + this->n;
}

int Calc::sub(void)
{
    return this->m - this->n;
}

int Calc::mul(void)
{
    return this->m * this->m;
}

int Calc::div(void)
{
    return this->m / this->n;
}
