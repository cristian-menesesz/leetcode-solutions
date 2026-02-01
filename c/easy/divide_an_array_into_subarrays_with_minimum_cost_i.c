#include <limits.h>

int minimumCost(int* nums, int size) {
    int first = nums[0];
    int min1 = INT_MAX;
    int min2 = INT_MAX;

    for (int i = 1; i < size; i++) {
        int x = nums[i];
        if (x < min1) {
            min2 = min1;
            min1 = x;
        } else if (x < min2) {
            min2 = x;
        }
    }

    return first + min1 + min2;
}
