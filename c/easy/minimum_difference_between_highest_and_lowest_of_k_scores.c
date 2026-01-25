#include <stdlib.h>
#include <limits.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int minimumDifference(int* nums, int numsSize, int k) {
    if (k == 1) return 0;

    qsort(nums, numsSize, sizeof(int), compare);

    int min_difference = INT_MAX;

    for (int left = 0; left <= numsSize - k; left++) {
        int right = left + k - 1;
        int current_difference = nums[right] - nums[left];
        if (current_difference < min_difference) {
            min_difference = current_difference;
        }
    }

    return min_difference;
}
