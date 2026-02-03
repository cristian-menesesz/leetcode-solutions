#include <stdbool.h>

bool isTrionic(int* nums, int n) {
    if (n < 4) return false;
    if (nums[0] >= nums[1]) return false;

    bool first_increase_finished = false;
    bool decrease_finished = false;
    bool increasing = true;

    for (int i = 1; i < n; i++) {
        if (nums[i] == nums[i - 1]) return false;

        if (increasing) {
            if (nums[i] < nums[i - 1]) {
                if (!first_increase_finished) {
                    first_increase_finished = true;
                    increasing = false;
                } else {
                    return false;
                }
            }
        } else {
            if (nums[i] > nums[i - 1]) {
                if (!decrease_finished) {
                    decrease_finished = true;
                    increasing = true;
                } else {
                    return false;
                }
            }
        }
    }

    return first_increase_finished && decrease_finished;
}
