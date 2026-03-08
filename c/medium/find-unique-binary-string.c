#include <stdlib.h>

char* findDifferentBinaryString(char** binary_strings, int n) {
    char* result = (char*)malloc((n + 1) * sizeof(char));

    for (int i = 0; i < n; i++) {
        result[i] = (binary_strings[i][i] == '0') ? '1' : '0';
    }

    result[n] = '\0';
    return result;
}
