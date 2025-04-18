#include <stdio.h>
#include <stdlib.h>

// 定义双链表节点
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

// 在链表末尾插入新节点
void insert(struct Node** head, int newData) {
    // 创建新节点
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = NULL;

    // 如果链表为空，将新节点设为头节点
    if (*head == NULL) {
        newNode->prev = NULL;
        *head = newNode;
        return;
    }

    // 遍历链表，找到最后一个节点
    struct Node* lastNode = *head;
    while (lastNode->next != NULL) {
        lastNode = lastNode->next;
    }
  
    // 连接新节点
    lastNode->next = newNode;
    newNode->prev = lastNode;
}

// 删除指定数据的节点
void delete(struct Node** head, int targetData) {
    // 如果链表为空，直接返回
    if (*head == NULL) {
        return;
    }

    // 如果头节点是要删除的节点
    if ((*head)->data == targetData) {
        struct Node* temp = *head;
        *head = (*head)->next;
        if (*head != NULL) {
          (*head)->prev = NULL;
        }
        free(temp);
        return;
    }

    // 遍历链表，找到要删除的节点
    struct Node* currentNode = *head;
    while (currentNode != NULL && currentNode->data != targetData) {
        currentNode = currentNode->next;
    }

    // 如果找到了要删除的节点
    if (currentNode != NULL) {
        currentNode->prev->next = currentNode->next;
        if (currentNode->next != NULL) {
          currentNode->next->prev = currentNode->prev;
        }
        free(currentNode);
    }
}

// 修改指定数据的节点
void modify(struct Node* head, int oldData, int newData) {
    struct Node* currentNode = head;

    // 遍历链表，找到要修改的节点
    while (currentNode != NULL) {
        if (currentNode->data == oldData) {
            currentNode->data = newData;
            break;
        }
        currentNode = currentNode->next;
    }
}

// 在双链表中查找指定数据的节点
struct Node* search(struct Node* head, int targetData) {
    struct Node* currentNode = head;

    // 遍历链表，找到目标节点
    while (currentNode != NULL) {
        if (currentNode->data == targetData) {
            return currentNode;
        }
        currentNode = currentNode->next;
    }

    // 如果没有找到，返回 NULL
    return NULL;
}

// 打印双链表中的所有节点（从头到尾）
void printList(struct Node* head) {
    struct Node* currentNode = head;

    printf("正向遍历：");
    while (currentNode != NULL) {
        printf("%d ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("\n");

    printf("反向遍历: ");
    while (currentNode != NULL) {
        printf("%d ", currentNode->data);
        currentNode = currentNode->prev;
    }
    printf("\n");
}

int main() {
    // 初始化双链表头节点
    struct Node* head = NULL;

    // 插入节点
    insert(&head, 1);
    insert(&head, 2);
    insert(&head, 3);
    insert(&head, 4);

    // 打印双链表
    printList(head);

    // 删除节点
    delete(&head, 3);

    // 打印双链表
    printList(head);

    // 修改节点
    modify(head, 2, 5);

    // 打印双链表
    printList(head);

    // 查找节点
    int targetData = 4;
    struct Node* targetNode = search(head, targetData);
    if (targetNode != NULL) {
        printf("找到了值为 %d 的节点。\n", targetData);
    } else {
        printf("未找到值为 %d 的节点。\n", targetData);    
    }

    return 0;
}
