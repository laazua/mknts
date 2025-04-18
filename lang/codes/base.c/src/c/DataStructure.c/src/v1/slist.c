#include <stdlib.h>
#include "slist.h"


// 构造函数(新建节点)
SListNode *new_list_node(int num)
{
    SListNode *node, *next;
    node = (SListNode *)malloc(sizeof(SListNode));
    if (!node) {
        return NULL;
    }
    node->num = num;
    node->next = NULL;
    return node;
}


// 析构函数(清理节点)
void delete_list_node(SListNode *node)
{
    if (!node) 
        free(node);
    node = NULL;
}

