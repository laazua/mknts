#include <stdlib.h>
#include "dlist.h"


// 构造函数
DListNode *new_list_node(int num)
{
    DListNode *node = (DListNode *)malloc(sizeof(DListNode));
    if (!node)
	return NULL;
    node->num = num;
    node->prev = NULL;
    node->next = NULL;
    return node;
}


// 析构函数
void delete_list_node(DListNode *node)
{
    if (!node)
	free(node);
    node = NULL;
}
