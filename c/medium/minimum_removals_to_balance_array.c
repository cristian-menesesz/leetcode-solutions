#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int min_removal(int *nums, int n, int k) {
    qsort(nums, n, sizeof(int), cmp);

    if ((long long)nums[0] * k >= nums[n - 1]) {
        return 0;
    }

    int min_removals = n;
    int left = 0;

    for (int right = 0; right < n; right++) {
        while (left < right && (long long)nums[left] * k < nums[right]) {
            left++;
        }

        int window_size = right - left + 1;
        int removals = n - window_size;
        if (removals < min_removals) {
            min_removals = removals;
        }
    }

    return min_removals;
}
