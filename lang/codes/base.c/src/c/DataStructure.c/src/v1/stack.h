/* 栈:
 * push()
 * pop()
 * peek()
 */

#ifndef _STACK_H_
#define _STACK_H_

#include <stdbool.h>

#define STACK


typedef struct ListNode {
    int num;
    struct ListNode *next;
} ListNode;


typedef struct ListStack {
    int size;
    struct ListNode *top;
} ListStack;

ListStack *new_list_stack(void);
void delete_list_stack(ListStack *stack);
int size(ListStack *stack);
bool is_empty(ListStack *stack);
int peek(ListStack *stack);
void push(ListStack *stack, int num);
int pop(ListStack *stack);

#endif
