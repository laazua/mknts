#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 100
#define MAX_KEY_LENGTH 50
#define MAX_VALUE_LENGTH 50

char *get_value(const char *key) {
    char line[MAX_LINE_LENGTH];
    char cur_key[MAX_KEY_LENGTH];
    char value[MAX_VALUE_LENGTH];
    char *pos;
    FILE *file = fopen("config.txt", "r");

    if (file == NULL) {
        printf("Failed to open config file.\n");
        return NULL;
    }

    while (fgets(line, MAX_LINE_LENGTH, file)) {
        // Ignore comments and blank lines
        if (line[0] == '#' || line[0] == '\n') {
            continue;
        }

        // Split line into key and value
        pos = strchr(line, '=');
        if (pos == NULL) {
            printf("Invalid config line: %s", line);
            continue;
        }

        strncpy(cur_key, line, pos - line);
        cur_key[pos - line] = '\0';

        // If key matches, return value
        if (strcmp(key, cur_key) == 0) {
            strncpy(value, pos + 1, MAX_VALUE_LENGTH);
            value[strcspn(value, "\n")] = '\0';
            fclose(file);
            return strdup(value);
        }
    }

    fclose(file);
    printf("Key not found: %s\n", key);
    return NULL;
}

int main() {
    char *value = get_value("name");

    if (value != NULL) {
        printf("Value: %s\n", value);
        free(value);
    }

    return 0;
}

