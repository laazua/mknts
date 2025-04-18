#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 定义链表节点结构体
struct Node {
    int data;
    struct Node* next;
};

// 创建新节点的函数
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// 初始化指定长度的链表并为每个节点随机赋值
struct Node* initializeRandomList(int length) {
    if (length <= 0) {
        return NULL;
    }

    // 设置随机种子
    srand(time(0));

    struct Node* head = createNode(rand() % 10);  // 生成 0 到 99 之间的随机数作为头节点的数据
    struct Node* current = head;

    for (int i = 1; i < length; i++) {
        current->next = createNode(rand() % 10);  // 生成 0 到 99 之间的随机数作为当前节点的数据
        current = current->next;
    }

    return head;
}

void destoryNode(struct Node* NodeList)
{
    // 释放内存
    while (NodeList != NULL) {
        struct Node* temp = NodeList;
        NodeList = NodeList->next;
        free(temp);
    } 
}

struct Node* addTwoNumbers(struct Node* l1, struct Node* l2)
{

}

int main()
{
    // 初始化l1,l2两条链表
    struct Node *l1 = initializeRandomList(3);
    struct Node *l2 = initializeRandomList(3);

    // 遍历链表并打印数据
    struct Node* current = l1;
    while (current != NULL) {
        printf("%d\n", current->data);
        current = current->next;
    }

    // 释放内存
    destoryNode(l1);
    destoryNode(l2);
   
    return 0;
}
