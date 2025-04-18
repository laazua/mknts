// 接口实现多态
#include <stdio.h>

// 函数指针进行接口抽象 
typedef struct {
    void (*run)(void);
    void (*waa)(void);
} behavior;

// dog 实现 behavior
void dog_run(void) 
{
    printf("dog run ...\n");
}

void dog_waa(void)
{
    printf("dog waa ...\n");
}

// cat 实现 behavior
void cat_run(void)
{
    printf("cat run ...\n");
}

void cat_waa(void)
{
    printf("cat waa ...\n");
}

// 使用接口进行不同动物的行为展示
void animal_behavior(behavior *animal)
{
    animal->run();
    animal->waa();
}

int main()
{
    behavior dog = {
        .run = dog_run,
        .waa = dog_waa,
    };

    behavior cat = {
        .run = cat_run,
        .waa = cat_waa,
    };

    animal_behavior(&dog);
    animal_behavior(&cat);
}
