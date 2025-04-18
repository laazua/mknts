#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glib.h>

int main() {
    GHashTable *config = g_hash_table_new(g_str_hash, g_str_equal);

    FILE *file = fopen("config.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    char line[100];
    while (fgets(line, sizeof(line), file)) {
        if (line[0] == '#') {
            continue; // 忽略注释行
        }
        
        char key[50], value[50];
        sscanf(line, "%[^=]=%[^\n]", key, value);
        g_hash_table_insert(config, g_strdup(key), g_strdup(value));
    }

    fclose(file);

    // 获取配置项的值
    const gchar *name = g_hash_table_lookup(config, "Name");
    const gchar *age_str = g_hash_table_lookup(config, "Age");
    int age = atoi(age_str);
    const gchar *city = g_hash_table_lookup(config, "City");

    // 输出配置项的值
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    printf("City: %s\n", city);

    // 清理内存
    g_hash_table_destroy(config);

    return 0;
}
// 安装glib库: sudo apt install libglib2.0-dev
// 编译: gcc -o main config.c `pkg-config --cflags --libs glib-2.0`
