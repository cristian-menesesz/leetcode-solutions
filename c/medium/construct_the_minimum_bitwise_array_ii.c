#include <stdlib.h>

int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;

    for (int i = 0; i < numsSize; i++) {
        int target = nums[i];

        if ((target & 1) == 0) {
            result[i] = -1;
            continue;
        }

        int lowest_changed_bit = ((target + 1) & ~target) >> 1;
        int minimal_candidate = target & ~lowest_changed_bit;
        result[i] = minimal_candidate;
    }

    return result;
}
