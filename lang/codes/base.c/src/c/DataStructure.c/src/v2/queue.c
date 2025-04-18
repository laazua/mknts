/*
// 队列
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// 抽象队列
typedef struct {
    int *array;  // 存储队列元素的数组
    int cap;     // 队列的容量
    int head;    // 队列首指针
    int tail;    // 队列尾指针
    int size;    // 队列元素个数
} Queue;

// 初始化队列
Queue *queue_init(int cap)
{   
    // 分配队列内存空间
    Queue *queue = (Queue*)malloc(sizeof(Queue));
    if (!queue) {
        fprintf(stderr, "队列分配内存失败!\n");
        return NULL;
    }
    // 分配队列数组内存空间
    queue->array = (int*)malloc(sizeof(int));
    if (!queue->array) {
        fprintf(stderr, "队列数组分配内存失败!\n");
        return NULL;
    }

    queue->cap = cap;  // 初始化队列容量
    queue->head = 0;   // 初始化队列首指针
    queue->tail = -1;  // 初始化队列尾指针
    queue->size = 0;   // 初始化队列元素个数
    
    return queue;
}

// 判断队列是否为空
bool queue_null(Queue *queue)
{
    return (queue->size == 0);
}

// 判断队列是否已满
bool queue_full(Queue *queue)
{
    return (queue->size == queue->cap);
}

// 元素入队
void queue_push(Queue *queue, int value)
{
    if (queue_full(queue)) {
        fprintf(stderr, "队列已满, 元素无法入队!\n");
        return;
    }
    queue->tail = (queue->tail + 1) % queue->cap;  // 循环队列实现
    queue->array[queue->tail] = value;  // 队列尾部追加元素
    queue->size++;  // 队列元素个数加1
}

// 元素出队
int queue_pops(Queue *queue)
{
    if (queue_null(queue)) {
        fprintf(stderr, "队列已空, 没有元素出队!\n");
        exit(EXIT_FAILURE);
    }
    
    int element = queue->array[queue->head];
    queue->head = (queue->head + 1) % queue->cap;
    queue->size--;

    return element;
}

// 获取队首元素
int queue_peek(Queue *queue)
{
    if (queue_null(queue)) {
        fprintf(stderr, "队列已空, 无法获取队首元素!\n");
        exit(EXIT_FAILURE);
    }
    return queue->array[queue->head];
}

// 销毁队列
void queue_destroy(Queue *queue)
{
    if (queue) {
        if (queue->array)
            free(queue->array);
        free(queue);
    } else {
        fprintf(stderr, "队列内存已经释放!\n");
    }
}


int main()
{
     Queue *queue = queue_init(5);
     if (queue) {
         queue_push(queue, 100);
         queue_push(queue, 300);
         queue_push(queue, 500);
         queue_push(queue, 700);
         queue_push(queue, 900);
         queue_push(queue, 1100);
         int head_element = queue_peek(queue);
         fprintf(stderr, "head_element = %d\n", head_element);
         int pops_element = queue_pops(queue);
         fprintf(stderr, "pops_element = %d\n", pops_element);
         queue_push(queue, 1100);
         queue_destroy(queue);
     }

     return 0;
}
