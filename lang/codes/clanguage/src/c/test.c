#include <stdio.h>

int main()
{
    printf("char: %zu\n", sizeof(char));
    printf("short int: %zu\n", sizeof(short int));
    printf("int: %zu\n", sizeof(int));
    printf("long int: %zu\n", sizeof(long int));
    printf("long long: %zu\n", sizeof(long long));

    printf("unsigned char: %zu\n", sizeof(unsigned char));
    printf("unsigned short int: %zu\n", sizeof(unsigned short int));
    printf("unsigned int: %zu\n", sizeof(unsigned int));
    printf("unsigned long int: %zu\n", sizeof(unsigned long int));
    

    return 0;
}