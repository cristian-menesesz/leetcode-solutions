#include <stdlib.h>

int* constructTransformedArray(int* nums, int n) {
    int* result = (int*)malloc(n * sizeof(int));
    if (!result) return NULL;

    for (int i = 0; i < n; i++) {
        int j = (i + nums[i]) % n;
        result[i] = nums[j];
    }

    return result;
}
