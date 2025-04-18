#include <iostream>
#include <main.hpp>

int main()
{
    //std::cout << "hello world" << std::endl;
    std::printf("hello world\n");

    int8  m = -5;
    int16 a = -10;
    int32 b = -20;
    int64 c = -30;

    uint8 n  = 5;
    uint16 d = 10;
    uint32 e = 20;
    uint64 f = 30;

    float32 g = 2.5;
    float64 h = 8.9;

    std::string s = "hello world";

    std::cout << "int8[char]: " << sizeof(int8) << std::endl;
    std::cout << "int16[short]: " << sizeof(int16) << std::endl;
    std::cout << "int32[int]: " << sizeof(int32) << std::endl;
    std::cout << "int64[long]: " << sizeof(int64) << std::endl;
    std::cout << "uint8[unsigned char]: " << sizeof(uint8) << std::endl;
    std::cout << "int16[unsigned short]: " << sizeof(uint16) << std::endl;
    std::cout << "int32[unsigned int]: " << sizeof(int32) << std::endl;
    std::cout << "int8[unsigned long]: " << sizeof(int64) << std::endl;
    std::cout << "float32[float]: " << sizeof(float32) << std::endl;
    std::cout << "float64[double]: " << sizeof(float64) << std::endl;

    std::printf("%d\n", m);
    std::printf("%d\n", n);
    std::printf("%d\n", a);
    std::printf("%d\n", b);
    std::printf("%d\n", c);
    std::printf("%d\n", d);
    std::printf("%d\n", e);
    std::printf("%d\n", f);
    std::printf("%f\n", g);
    std::printf("%f\n", h);
    std::printf("%s\n", s.c_str());

    return 0;
}

// + - * / %
// ++ -- 
// += -= *= /= %=
// && || !
// &  |  ^
// ~
// << >>
