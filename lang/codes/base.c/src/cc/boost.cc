/*
* http://zh.highscore.de/cpp/boost/
* ubuntu: sudo apt-get install libboost-all-dev
*/
#include <string>
#include <iostream>
#include <boost/any.hpp>
#include <boost/array.hpp>
#include <boost/bimap.hpp>

int main()
{
    // any.hpp
    boost::any a = 100;
    boost::any b = 3.14;
    boost::any c = std::string("hello world");
    std::cout << boost::any_cast<int>(a) << std::endl;
    std::cout << boost::any_cast<double>(b) << std::endl;
    std::cout << boost::any_cast<std::string>(c) << std::endl;
    // array.hpp
    boost::array<std::string, 3> colors = {"red", "green", "blue"};
    std::cout << "size: " << colors.size() << std::endl;
    std::cout << "max size: " << colors.size() << std::endl;
    for (auto item = colors.begin(); item != colors.end(); item++)
        std::cout << *item << std::endl;
    // bimap.hpp
    boost::bimap<std::string, std::string> bidict;
    bidict.insert(boost::bimap<std::string, std::string>::value_type("name", "张三"));
    bidict.insert(boost::bimap<std::string, std::string>::value_type("addr", "北京"));
    bidict.insert(boost::bimap<std::string, std::string>::value_type("score", "100"));
    for (auto item = bidict.begin(); item != bidict.end(); item++)
        std::cout << item->left << ": " << item->right << std::endl;

    return 0;
}
