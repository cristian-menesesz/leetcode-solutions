#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp_desc(const void* a, const void* b) {
    return strcmp(*(const char**)b, *(const char**)a);
}

char* makeLargestSpecial(char* s) {
    int n = strlen(s);

    if (n <= 2) {
        return strdup(s);
    }

    char** blocks = malloc(n * sizeof(char*));
    int block_count = 0;

    int balance = 0;
    int start = 0;

    for (int i = 0; i < n; i++) {
        balance += (s[i] == '1') ? 1 : -1;

        if (balance == 0) {
            int inner_len = i - start - 1;

            char* inner = malloc(inner_len + 1);
            strncpy(inner, s + start + 1, inner_len);
            inner[inner_len] = '\0';

            char* optimized = makeLargestSpecial(inner);
            free(inner);

            int new_len = strlen(optimized) + 2;
            char* block = malloc(new_len + 1);
            sprintf(block, "1%s0", optimized);

            free(optimized);

            blocks[block_count++] = block;
            start = i + 1;
        }
    }

    qsort(blocks, block_count, sizeof(char*), cmp_desc);

    int total_len = 0;
    for (int i = 0; i < block_count; i++)
        total_len += strlen(blocks[i]);

    char* result = malloc(total_len + 1);
    result[0] = '\0';

    for (int i = 0; i < block_count; i++) {
        strcat(result, blocks[i]);
        free(blocks[i]);
    }

    free(blocks);

    return result;
}