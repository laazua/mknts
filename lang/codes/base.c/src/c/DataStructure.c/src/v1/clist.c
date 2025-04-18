#include <stdlib.h>
#include "clist.h"


// 构造函数
CListNode *new_list_node(int num)
{
    CListNode *node = (CListNode *)malloc(sizeof(CListNode));
    if (!node)
	return NULL;
    node->num = num;
    node->prev = NULL;
    node->next = NULL;
    return node;
}


// 析构函数
void delete_list_node(CListNode *node)
{
    if (!node)
	free(node);
    node = NULL;
}

