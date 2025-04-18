/*
// 离散链表
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 抽象离散链表节点
typedef struct Node {
     int data;  // 数据域
     struct Node *next;  // 指针域   
} Node;

// 生成指定范围内的随机整数
int generate_random_num(int value) {
    static unsigned int last_seed = 0;
    unsigned int current_time = (unsigned int)time(NULL) + value;
    // 如果上一次使用的种子值与当前时间相同，则增加种子值，确保每次都不同
    if (last_seed == current_time) {
        current_time++;
    }
    last_seed = current_time;    
    srand((unsigned int)current_time);
    
    // 生成随机值，并映射到[min, max]范围内
    int random_value = rand() % ((100 - 1) * 100);
    
    return random_value;
}

// 创建长度为len的链表
// 并给节点随机赋值整数
Node *list_init(int len)
{
    if (len) {
        fprintf(stderr, "创建的离散链表长度不能为0\n");
        return NULL;
    }

    Node *head = (Node *)malloc(sizeof(Node));
    if (!head) {
        fprintf(stderr, "head节点分配内存失败!\n");
        return NULL;
    }
    Node *tail = head;
    tail->next = NULL;       

    for (int i=0; i<len; i++) {
        Node *node = (Node *)malloc(sizeof(Node));
        if (!node) {
            fprintf(stderr, "node节点分配内存失败!\n");
            return NULL;
        }
        node->data = generate_random_num(i);
        tail->next = node;
        node->next = NULL;
        tail = node;
    }
    return head;   
}

// 遍历离散列表
void list_range(Node *node)
{
    if (!node) {
        fprintf(stderr, "离散链表为空!\n");
        return;
    }
    Node *next = node->next;
    while (next) {
        fprintf(stderr, "%d\n", next->data);
        next = next->next;
    }
}

// 销毁离散列表
void list_destory(Node **head)
{
    Node *temp;
    Node *curt = *head;
    while (curt) {
        temp = curt->next; // 保存下一个节点的指针
        free(curt);        // 释放当前节点的内存
        curt = temp;       // 移动到下一个节点
    }
    *head = NULL; // 将头指针设为NULL
}

int main()
{
    Node *nodeList = list_init(5);
    list_range(nodeList);
    list_destory(&nodeList);

    return 0;
}
