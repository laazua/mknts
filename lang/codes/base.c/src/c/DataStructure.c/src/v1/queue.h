/*
 * 队列
 */

#ifndef _QUEUE_H_
#define _QUEUE_H_

#define QUEUE

typedef struct ListNode {

} ListNode;

typedef struct ListQueue {

} ListQueue;

ListQueue *new_list_queue(void);
void delete_list_queue(ListQueue *queue);
int size(ListQueue *queue);
void push(ListQueue *queue, int num);
int pop(ListQueue *queue);
int peek(ListQueue *queue);

#endif
