#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define REMOVED INT_MAX

bool is_non_decreasing_ignoring_removed(int *arr, int n) {
    int prev = INT_MIN;

    for (int i = 0; i < n; i++) {
        if (arr[i] == REMOVED) continue;
        if (arr[i] < prev) return false;
        prev = arr[i];
    }
    return true;
}

int minimumPairRemoval(int *nums, int n) {
    int operations = 0;

    while (!is_non_decreasing_ignoring_removed(nums, n)) {
        int min_pair_sum = INT_MAX;
        int left = -1, right = -1;

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == REMOVED) continue;

            int j = i + 1;
            while (j < n && nums[j] == REMOVED) j++;

            if (j < n) {
                int sum = nums[i] + nums[j];
                if (sum < min_pair_sum) {
                    min_pair_sum = sum;
                    left = i;
                    right = j;
                }
            }
        }

        if (left == -1) break;

        nums[left] += nums[right];
        nums[right] = REMOVED;
        operations++;
    }

    return operations;
}
