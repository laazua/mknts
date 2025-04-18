#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLESIZE 100

struct Node {
    char *key;
    int value;
    struct Node *next;
};

struct HashTable {
    struct Node **array;
};

struct Node *new_node(const char *key, int value)
{
    struct Node *node = NULL;
    node = (struct Node *)malloc(sizeof(struct Node));
    if (node == NULL) return NULL;

    node->key = strdup(key);
    node->value = value;
    node->next = NULL;

    return node;
}

struct HashTable *new_hash_table()
{
    struct HashTable *hash_table = NULL;
    hash_table = (struct HashTable *)malloc(sizeof(struct HashTable));
    if (hash_table == NULL) return NULL;

    hash_table->array = NULL;
    hash_table->array = (struct Node **)malloc(sizeof(struct node*) * TABLESIZE);
    if (hash_table->array == NULL) return NULL;

    for (int idx=0; idx<TABLESIZE; idx++) hash_table->array[idx] = NULL;

    return hash_table;
}

int hash_func(const char *key)
{
    int hash = 0;
    for (int idx=0; key[idx]!='\0'; ++idx) hash = (hash * 31 + key[idx]) % TABLESIZE;

    return hash;
}

void insert_hash_table(struct HashTable *hash_table, const char *key, int value)
{
    int index = hash_func(key);
    if (hash_table == NULL) return;
    struct Node *node = new_node(key, value);
    if (node == NULL) return;

    if (hash_table->array[index] == NULL) {
        hash_table->array[index] = new_node(key, value);
    } else {
        struct Node *tmp = hash_table->array[index];
        while (tmp->next != NULL) tmp = tmp->next;
        tmp->next = node;
    }
}

int search_hash_table(struct HashTable *hash_table, const char *key)
{
    if (hash_table == NULL) return -1;
    int index = hash_func(key);
    struct Node *tmp = hash_table->array[index];
    while (tmp != NULL) {
        if (strcmp(tmp->key, key) == 0) return tmp->value;
        tmp = tmp->next;
    }

    return -2;  // 未找到对应键的值
}

void delete_hash_table(struct HashTable *hash_table)
{
    if (hash_table == NULL) return;
    
    free(hash_table);
    hash_table = NULL;
}

int main()
{
    struct HashTable *hash_table = new_hash_table();
    insert_hash_table(hash_table, "key1", 100);
    insert_hash_table(hash_table, "key2", 200);
    insert_hash_table(hash_table, "key3", 300);

    fprintf(stdout, "%d\n", search_hash_table(hash_table, "key1"));
    fprintf(stdout, "%d\n", search_hash_table(hash_table, "key2"));
    fprintf(stdout, "%d\n", search_hash_table(hash_table, "key3"));
    fprintf(stdout, "%d\n", search_hash_table(hash_table, "key4"));  // -2未找到对应键的值

    insert_hash_table(hash_table, "key1", 599);  // key1键已设置,这里不生效
    fprintf(stdout, "%d\n", search_hash_table(hash_table, "key1"));  // 100
   
    delete_hash_table(hash_table);

    return 0;
}
