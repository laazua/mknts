// map

#ifndef _MPA_H_
#define _MAP_H_

#define MAX_SIZE 1024

typedef union {
    int i_value;
    double f_value;
    char *s_value;
    // other type
} Value;

typedef struct {
    char *key;
    Value value;
    int value_type;
} Kv;

typedef struct {
    int size;
    Kv pairs[MAX_SIZE];
} Map;

void map(Map *map);
void set_kv(Map *map, const char *key, const Value *value, int value_type);
Value get_kv(Map *map, const char *key);

#endif // _MAP_H_
