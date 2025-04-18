#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char *name;
    char *address;
} Person;


int main()
{
    // 定义指针的时候初始化成NULL
    Person *pointer = NULL;
    pointer = (Person *)malloc(sizeof(Person));
    if (pointer == NULL)
        return -1;
    pointer->name = "zhangsan";
    pointer->address = "chengdu";

    fprintf(stderr, "name    = %s\n", pointer->name);
    fprintf(stderr, "address = %s\n", pointer->address);

    if (pointer != NULL) {
        free(pointer);
        // 释放指针所指的内存空间的时候将指针重新指向NULL
        pointer = NULL;
    }

    // void * 通用指针
    void *generic_pointer; // 定义一个void *通用指针
    int num = 10;
    
    generic_pointer = &num; // 将int类型的指针赋值给void *通用指针
    // 不能通过通用指针去访问具体类型的值,会报错
    // printf("%d\n", *generic_pointer);

    // 必须将void *通用指针转换为int类型的指针，并使用int型指针访问所指向的值
    int *int_pointer = (int *)generic_pointer;
    printf("The value of num is: %d\n", *int_pointer);


    return 0;
}
