#include <iostream>

int operate(int a, int b)
{
  return a + b;
}

double operate(double a, double b)
{
  return a - b;
}

float operate(float a, float b, float c)
{
  return a * b * c;
}

int main()
{
  std::cout << operate(8, 4) << std::endl;
  std::cout << operate(4.5, 2.1) << std::endl;
  std::cout << operate(3.1, 4.6, 2.2) << std::endl;

  return 0;
}
