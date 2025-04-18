#include <stdio.h>
#include <stdlib.h>

struct PriorityQueue {
    int *data;
    int size;
    int capactity;
};

struct PriorityQueue *new_priority_queue(int capactity)
{
    struct PriorityQueue *pq = NULL;
    pq = (struct PriorityQueue *)malloc(sizeof(struct PriorityQueue));
    if (pq == NULL) return NULL;

    pq->data = (int *)malloc(sizeof(int) * (capactity + 1));
    pq->size = 0;
    pq->capactity = capactity;

    return pq;    
}

// 向上调整堆
void heap_up(struct PriorityQueue *pq, int index)
{
    while (index > 1 && pq->data[index/2] < pq->data[index]) {
        int tmp = pq->data[index];
        pq->data[index] = pq->data[index/2];
        pq->data[index/2] = tmp;
        index /= 2;
    }
}

// 向下调整堆
void heap_down(struct PriorityQueue *pq, int index)
{
    int largest = index;
    int left = 2 * index;
    int right = 2 * index + 1;
    
    if (left <= pq->size && pq->data[left] > pq->data[largest]) largest = left;
    if (right <= pq->size && pq->data[right] > pq->data[largest]) largest = right;
    if (largest != index) {
        int tmp = pq->data[index];
        pq->data[index] = pq->data[largest];
        pq->data[largest] = tmp;
        heap_down(pq, largest);
    }
}

void insert_priority_queue(struct PriorityQueue *pq, int value)
{
    if (pq == NULL) return;
    if (pq->size > pq->capactity) return;  // 队列已满
    pq->size++;
    pq->data[pq->size] = value;
    heap_up(pq, pq->size);
}

int delete_max_element(struct PriorityQueue *pq)
{
    if (pq == NULL) return -1;
    if (pq->size == 0) return -2;  // 队列为空
    int max_value = pq->data[1];
    pq->data[1] = pq->data[pq->size];
    pq->size--;
    heap_down(pq, 1);

    return max_value;
}

void print_priority_queue(struct PriorityQueue *pq)
{
    if (pq == NULL) return;
    for (int idx=1; idx<pq->size; idx++) fprintf(stdout, "%d\n", pq->data[idx]);
}

void delete_priority_queue(struct PriorityQueue *pq) {
    if (pq == NULL)  return;
    free(pq->data);
    pq->data = NULL;
    free(pq);
    pq = NULL;
}

int main()
{
    struct PriorityQueue *pq = new_priority_queue(10);

    insert_priority_queue(pq, 34);
    insert_priority_queue(pq, 39);
    insert_priority_queue(pq, 67);
    insert_priority_queue(pq, 75);
    insert_priority_queue(pq, 98);
    insert_priority_queue(pq, 77);
    insert_priority_queue(pq, 45);
 //   insert_priority_queue(pq, 34);
 //   insert_priority_queue(pq, 21);
 //   insert_priority_queue(pq, 33);
 //   insert_priority_queue(pq, 55);
 //   insert_priority_queue(pq, 99);

    print_priority_queue(pq);
    fprintf(stdout, "max value: %d\n", delete_max_element(pq));
    print_priority_queue(pq);
    delete_priority_queue(pq);

    return 0;
}
