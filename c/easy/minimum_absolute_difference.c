#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) {
    qsort(arr, arrSize, sizeof(int), cmp);

    int minDiff = __INT_MAX__;
    int** resultPairs = malloc(arrSize * sizeof(int*));
    *returnColumnSizes = malloc(arrSize * sizeof(int));
    *returnSize = 0;

    for(int i = 1; i < arrSize; i++) {
        int diff = arr[i] - arr[i - 1];
        if(diff < minDiff) {
            minDiff = diff;
            *returnSize = 0; // reset pairs
        }
        if(diff == minDiff) {
            resultPairs[*returnSize] = malloc(2 * sizeof(int));
            resultPairs[*returnSize][0] = arr[i - 1];
            resultPairs[*returnSize][1] = arr[i];
            (*returnColumnSizes)[*returnSize] = 2;
            (*returnSize)++;
        }
    }

    return resultPairs;
}
