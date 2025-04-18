#include "struct.hh"

Animal::Animal(int age, std::string name)
  : _age(age), _name(name){}

int Animal::get_age()
{
  return _age;
}

std::string Animal::get_name()
{
  return _name;
}

