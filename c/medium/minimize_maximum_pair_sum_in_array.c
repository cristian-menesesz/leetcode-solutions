#include <stdlib.h>

int minPairSum(int* nums, int numsSize) {
    const int MAX_VALUE = 100000;
    int* frequency = calloc(MAX_VALUE + 1, sizeof(int));

    int min_value = MAX_VALUE;
    int max_value = 0;

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        frequency[num]++;
        if (num < min_value) min_value = num;
        if (num > max_value) max_value = num;
    }

    int pairs_needed = numsSize / 2;
    int smallest_used = 0;
    int largest_used = 0;

    int left = min_value;
    int right = max_value;
    int worst_pair_sum = 0;

    for (int pair_number = 1; pair_number <= pairs_needed; pair_number++) {

        while (smallest_used < pair_number) {
            smallest_used += frequency[left];
            left++;
        }

        while (largest_used < pair_number) {
            largest_used += frequency[right];
            right--;
        }

        int sum = left + right;
        if (sum > worst_pair_sum) worst_pair_sum = sum;
    }

    free(frequency);
    return worst_pair_sum;
}
