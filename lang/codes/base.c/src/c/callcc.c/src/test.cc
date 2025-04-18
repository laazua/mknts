#include <vector>
#include <string>
#include <iostream>

extern "C" {
    void cppFunction() {
        std::cout << "run c++ code" << std::endl;
    }

    void testString() {
        std::string s = "abc";
        std::cout << s << std::endl;
    }

    void testVector() {
        std::vector<int> vec;
        vec.push_back(10);
        vec.push_back(20);
        vec.push_back(30);

        std::cout << vec.size() << std::endl;

        for(int v : vec)
            std::cout << v << std::endl;
    }

}

