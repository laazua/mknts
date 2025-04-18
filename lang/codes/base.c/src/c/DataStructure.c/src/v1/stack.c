#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "stack.h"


// 构造函数(新建一个栈)
ListStack *new_list_stack(void)
{
    ListStack *stack = (ListStack *)malloc(sizeof(ListStack));
    if (stack == NULL)
	return NULL;
    stack->top = NULL;
    stack->size = 0;
    return stack;
}


// 析构函数(清理一个栈)
void delete_list_stack(ListStack *stack)
{
    if (stack != NULL) 
	free(stack);
    stack = NULL;
}


// 获取栈大小
int size(ListStack *stack)
{
    return stack->size;
}


// 判断栈是否为空
bool is_empty(ListStack *stack)
{
    if (stack->size == 0) 
	return true;
    else return false;
}


// 获取栈顶元素
int peek(ListStack *stack)
{
    if (stack->size == 0) assert(stack);
    else return stack->top->num;
}


// 元素进栈操作
void push(ListStack *stack, int num)
{
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));
    node->next = stack->top;
    node->num = num;
    stack->top = node;
    stack->size++;
}


// 元素出栈操作
int pop(ListStack *stack)
{
    if (is_empty(stack)) 
	assert(stack);
    int num = peek(stack);
    ListNode *tmp = stack->top;
    stack->top = stack->top->next;
    free(tmp);
    tmp = NULL;
    stack->size--;
    return num;
}
