#include "struct.hh"

int main()
{
    Animal animal(6, "cat");
    std::cout << animal.get_name() << " " << animal.get_age() << std::endl;

    return 0;
}

// g++ struct_test.cc struct.cc
