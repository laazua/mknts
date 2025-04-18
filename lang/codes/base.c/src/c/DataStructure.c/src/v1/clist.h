/*
// 环型链表
// 增删改查
*/

#ifndef _DLIST_H_
#define _DLIST_H_

#define CLIST

// 节点
typedef struct CListNode {
    int num;
    struct CListNode *prev;
    struct CListNode *next;
} CListNode;

CListNode *new_list_node(int num);
void delete_list_node(CListNode *node);

#endif
