#include "namespace.hh"

int main()
{
    ABC::Person p;
    p.say_hello();    
    //std::cout << "hello world" << std::endl;

    return 0;
}

// g++ main.cc namespace.cc -o main
