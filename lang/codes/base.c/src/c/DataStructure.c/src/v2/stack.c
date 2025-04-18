/*
// 栈
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define SIZE 5

// 抽象栈
typedef struct {
    int top;  // 栈顶指针
    int element[SIZE]; // 栈元素数组
} Stack;

// 初始化栈
void stack_init(Stack *stack)
{
    stack->top = -1;
}

// 栈是否已空
bool stack_null(Stack *stack)
{
    return stack->top == -1;
}

// 栈是否已满
bool stack_full(Stack *stack)
{
    return stack->top == SIZE - 1;
}

// 元素入栈
void stack_push(Stack *stack, int value)
{
    if (stack_full(stack)) {
        fprintf(stderr, "栈已满!\n");
        return;
    }
    stack->element[++stack->top] = value;
}

// 元素出栈
int stack_pops(Stack *stack)
{
    if (stack_null(stack)) {
        fprintf(stderr, "栈已空!\n");
        exit(EXIT_FAILURE);
    }
    return stack->element[stack->top--];
}

// 获取栈顶元素
int stack_peek(Stack *stack)
{
    if (stack_null(stack)) {
        fprintf(stderr, "栈已空!\n");
        exit(EXIT_FAILURE);
    }
    return stack->element[stack->top];
}

int main()
{
    Stack stack;
    stack_init(&stack);
    stack_push(&stack, 10);
    stack_push(&stack, 17);
    stack_push(&stack, 25);
    stack_push(&stack, 18);
    stack_push(&stack, 21);
    //stack_push(&stack, 50);
    int element = stack_peek(&stack);
    fprintf(stderr, "获取栈顶元素: %d\n", element);

    int item;
    for (int i=0; i<5; i++) {
        item = stack_pops(&stack);
        fprintf(stderr, "出栈元素: %d\n", item);
    }

    return 0;
}
