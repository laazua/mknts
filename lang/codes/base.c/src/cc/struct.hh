#ifndef _STRUCT_H_
#define _STRUCT_H_

#include <iostream>
#include <string>

struct Animal
{
public:
  Animal(int age, std::string name);
  int get_age();
  std::string get_name();
private:
    int _age;
    std::string _name;
};

#endif // _STRUCT_H_
