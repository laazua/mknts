/*
// 双链表
// 增删改查
*/

#ifndef _DLIST_H_
#define _DLIST_H_

#define DLIST

// 节点
typedef struct DListNode {
    int num;
    struct DListNode *prev;
    struct DListNode *next;
} DListNode;

DListNode *new_list_node(int num);
void delete_list_node(DListNode *node);

#endif
