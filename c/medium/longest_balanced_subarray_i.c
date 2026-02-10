#include <stdlib.h>

int longestBalanced(int* nums, int numsSize) {
    int maxVal = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    int* last_seen = calloc(maxVal + 1, sizeof(int));
    int max_length = 0;

    for (int start = 0; start < numsSize; start++) {
        if (numsSize - start <= max_length) break;

        int distinct_counts[2] = {0, 0};

        for (int end = start; end < numsSize; end++) {
            int value = nums[end];

            if (last_seen[value] != start + 1) {
                last_seen[value] = start + 1;
                int parity = value & 1;
                distinct_counts[parity]++;
            }

            if (distinct_counts[0] == distinct_counts[1]) {
                int length = end - start + 1;
                if (length > max_length) {
                    max_length = length;
                }
            }
        }
    }

    free(last_seen);
    return max_length;
}
