#include <stdio.h>
#include <assert.h>
#include <string.h>

#ifdef SLIST_UP
#include "slist.h"
#endif // SLIST_UP

#ifdef DLIST_UP
#include "dlist.h"
#endif // DLIST_UP

#ifdef CLIST_UP
#include "clist.h"
#endif // CLIST_UP

#ifdef STACK_UP
#include "stack.h"
#endif // STACK_UP

#ifdef QUEUE_UP
#include "queue.h"
#endif // QUEUE_UP

#ifdef MAP_UP
#include "map.h"
#endif // MAP_UP


int main(void)
{
#ifdef SLIST
    // single list
    SListNode *sn0, *sn1, *sn2;

    sn0 = new_list_node(0);
    sn1 = new_list_node(1);
    sn2 = new_list_node(2);
    sn0->next = sn1;
    sn1->next = sn2;
    sn2->next = NULL;

    printf("single list: %d, sn0 address: %p\n", sn0->num, &sn0);
    printf("single list: %d, sn1 address: %p\n", sn1->num, &sn1);
    printf("single list: %d, sn2 address: %p\n", sn2->num, &sn2);
 
    printf("single list sn0->sn1: %d\n", sn0->next->num);
    printf("single list sn1->sn2: %d\n", sn1->next->num);

    delete_list_node(sn0);
    delete_list_node(sn1);
    delete_list_node(sn2);
#endif // SLIST

#ifdef DLIST
    // double list
    DListNode *dn0, *dn1, *dn2;
    dn0 = new_list_node(0);
    dn1 = new_list_node(1);
    dn2 = new_list_node(2);
    dn0->prev = NULL;
    dn0->next = dn1;
    dn1->prev = dn0;
    dn1->next = dn2;
    dn2->prev = dn1;
    dn2->next = NULL;

    printf("double list: %d, dn0 address: %p\n", dn0->num, &dn0);
    printf("double list: %d, dn1 address: %p\n", dn1->num, &dn1);
    printf("double list: %d, dn2 address: %p\n", dn2->num, &dn2);

    printf("double list dn0->dn1: %d\n", dn0->next->num);
    printf("double list dn1->dn2: %d\n", dn1->next->num);
    printf("double list dn2->dn1: %d\n", dn2->prev->num);
    printf("double list dn1->dn0: %d\n", dn1->prev->num);
    
    delete_list_node(dn0);
    delete_list_node(dn1);
    delete_list_node(dn2);
#endif //DLIST

#ifdef CLIST
    // circle list
    CListNode *cn0, *cn1, *cn2;
    cn0 = new_list_node(0);
    cn1 = new_list_node(1);
    cn2 = new_list_node(2);
    cn0->prev = cn2;
    cn0->next = cn1;
    cn1->prev = cn0;
    cn1->next = cn2;
    cn2->prev = cn1;
    cn2->next = cn0;

    printf("circle list: %d, cn0 address: %p\n", cn0->num, &cn0);
    printf("circle list: %d, cn1 address: %p\n", cn1->num, &cn1);
    printf("circle lsit: %d, cn2 address: %p\n", cn2->num, &cn2);

    printf("circle list cn0->cn1: %d\n", cn0->next->num);
    printf("circle list cn1->cn2: %d\n", cn1->next->num);
    printf("circle list cn2->cn0: %d\n", cn2->next->num);
    printf("circle list cn0->cn2: %d\n", cn0->prev->num);
    printf("circle list cn1->cn0: %d\n", cn1->prev->num);
    printf("circle lsit cn2->cn1: %d\n", cn2->prev->num);
    delete_list_node(cn0);
    delete_list_node(cn1);
    delete_list_node(cn2);
#endif // CLIST

#ifdef STACK
    // stack
    ListStack *stack = new_list_stack();
    push(stack, 100);
    push(stack, 200);
    push(stack, 300);
    push(stack, 400);
    
    if (is_empty(stack))
	printf("stack is empty!  %d\n", stack->size);
    printf("%d\n", peek(stack));
    pop(stack);
    printf("%d\n", peek(stack));
    pop(stack);
    printf("%d\n", peek(stack));
    pop(stack);
    printf("%d\n", peek(stack));
    pop(stack);
    printf("%d\n", peek(stack));
    if (is_empty(stack))
	printf("stack is empty!\n");

    delete_list_stack(stack);
#endif // STACK

#ifdef QUEUE
    // queue
    ListQueue *queue = new_list_queue();
    if (!queue)
    push(queue, 1000);
    push(queue, 2000)
#endif // QUEUE

#ifdef MAP
    // map
    Map map;
    map(&map);
    
    Value i_value = {100};
    Value f_value = {3.14};
    Value s_value;
    strcopy(s_value.s_value, "hello");
    
    set_kv(&map, "i_value", &i_value, 0);
    set_kv(&map, "f_value", &f_value, 1);
    set_kv(&map, "s_value", &s_value, 2);

    Value i_v = get_kv(&map, "i_value");
    Value f_v = get_kv(&map, "f_value");
    Value s_v = get_kv(&map, "s_value");

    printf("i_v: %d\n", i_v);
    printf("f_v: %f\n", f_v);
    printf("s_v: %s\n", s_v);
#endif // MAP
    
    return 0;
}
