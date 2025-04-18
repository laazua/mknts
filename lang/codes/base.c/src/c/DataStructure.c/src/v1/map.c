#include <stdio.h>
#include <string.h>

#include "map.h"


void map(Map *map)
{
    map->size = 0;
}


void set_kv(Map *map, const char *key, const Value *value, int value_type)
{
    if (map->size < MAX_SIZE) {
        strcpy(map->pairs[map->size].key, key);
        map->pairs[map->size].value = *value;
        map->pairs[map->size].value_type = value_type;
        map->size++;
    } else {
        printf("Dictionary is full. Cannot add more key-value pairs.\n");
    }
}


Value get_kv(Map *map, const char *key)
{
    Value valueNull;
    valueNull.s_value = "\0";
    for (int i=0; i<map->size; i++) {
        if (strcmp(map->pairs[i].key, key) == 0)
	    return map->pairs[i].value;
    }
    return valueNull;
}
