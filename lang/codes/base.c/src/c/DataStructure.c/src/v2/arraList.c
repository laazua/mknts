/*
// 线性数组(线性链表)操作
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// 抽象线性链表节点
typedef struct ArrList {
    int *ptr;  // 首元素地址
    int len;   // 线性数组长度
    int idx;   // 当前元素索引
} ArrList;

// 初始化数组链表
bool array_init(ArrList *array, int len)
{
    array->ptr = (int *)malloc(sizeof(int) * len);
    if (!array->ptr) {
        return false;
    } else {
        array->idx = 0;
        array->len = len;
    }
    return true;    
}

// 是否为空
bool array_null(ArrList *array)
{
    if (!array->idx) return true;
    else return false;
}

// 是否已满
bool array_full(ArrList *array)
{
    if (array->idx == array->len) return true;
    else return false;
}

// 在尾部追加元素
void array_append(ArrList *array, int value)
{
    if (!array->ptr) {
        fprintf(stderr, "非法的数组链表, 不允许追加元素!\n");
        return;
    }

    if (array_full(array)) {
        fprintf(stderr, "数组链表已满, 追加元素: %d失败!\n", value);
        return;
    }
    array->ptr[array->idx] = value;
    array->idx = array->idx + 1;
    fprintf(stderr, "数组链表追加元素: %d成功.\n", value);
}

// 打印链表元素
void array_show(ArrList *array)
{
    if (array_null(array)) {
        fprintf(stderr, "数组链表为空!\n");
        return;
    }
    for (int i=0; i<array->idx; i++) {
        fprintf(stderr, "%d\n", array->ptr[i]);
    }
}

// 在指定位置插入元素
void array_insert(ArrList *array, int pos, int value)
{
    if (array_full(array)) {
        fprintf(stderr, "数组链表已满, 不允许插入元素!\n");
        return;
    }
    if (pos > array->idx) {
        fprintf(stderr, "插入数组链表的位置为非法位置!\n");
        return;
    }

    for (int i=array->len - 1; i>pos-1; i--)
        array->ptr[i+1] = array->ptr[i];
    array->ptr[pos] = value;
    array->idx = array->idx + 1;
}

// 销毁数组链表
void array_destory(ArrList *array)
{
    if (array->ptr) free(array->ptr);
    else fprintf(stderr, "数组链表已经释放!\n");
}

int main()
{
    ArrList array;
    if(!array_init(&array, 6)) {
        fprintf(stderr, "初始化链表失败!\n");
        return -1;
    }
    array_append(&array, 100);
    array_append(&array, 500);
    array_append(&array, 800);
    array_append(&array, 1000);
    array_insert(&array, 4, 399);
    array_show(&array);
    array_destory(&array);

    return 0;
}
