#include <stdio.h>

// 声明结构体 (struct Person {}是类型, p是该类型的一个变量)
struct Person {
    char *name;
    int  age;
} p;

// 定义结构体类型(定义名为student的类型)
typedef struct {
    char *name;
    int  score;
} student;

void print_s(student s)
{
    printf("name = %s\n", s.name);
    printf("score = %d\n", s.score);
}

student get_s(char *name, int score)
{
    student s = {name, score};
    return s;   
}

// 结构体嵌套
struct room {
    int num;
};
struct school {
    int num;
    struct room r;
};

int main(void)
{
    struct Person p = {"zhangsan", 12};
    printf("name = %s\n", p.name);
    printf("age = %d\n", p.age);
 
    student s = {"lisi", 90};
    printf("name = %s\n", s.name);
    printf("score = %d\n", s.score);

    // 结构体作为函数参数
    print_s(s);

    // 结构体作为函数返回值
    student ss = get_s("wangwu", 99);
    printf("name = %s\n", ss.name);
    printf("score = %d\n", ss.score);

    // 结构体嵌套
    struct school sc = {12, {14}};
    printf("%d\n", sc.r.num);

    return 0;
}

