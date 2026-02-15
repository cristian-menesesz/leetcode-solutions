#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* addBinary(const char* a, const char* b) {
    int lenA = strlen(a);
    int lenB = strlen(b);
    int maxLen = lenA > lenB ? lenA : lenB;

    char* result = malloc(maxLen + 2);  // +1 for possible carry, +1 for '\0'
    result[maxLen + 1] = '\0';

    int carry = 0;
    int i = lenA - 1, j = lenB - 1, k = maxLen;

    while (k >= 0) {
        int sum = carry;

        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';

        result[k--] = (sum % 2) + '0';
        carry = sum / 2;
    }

    if (result[0] == '0') {
        memmove(result, result + 1, maxLen + 1);
    }

    return result;
}
