/*
/ 单链表
/ 增删改查
*/

#ifndef _SLIST_H_
#define _SLIST_H_

#define SLIST

// 节点
typedef struct SListNode {
    int num;
    struct SListNode *next;
} SListNode;

SListNode *new_list_node(int num);
void delete_list_node(SListNode *node);

#endif
