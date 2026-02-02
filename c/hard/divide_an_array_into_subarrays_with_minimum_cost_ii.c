#include <stdlib.h>
#include <limits.h>

void insert_sorted(int *arr, int *size, int value) {
    int i = *size - 1;
    while (i >= 0 && arr[i] > value) {
        arr[i + 1] = arr[i];
        i--;
    }
    arr[i + 1] = value;
    (*size)++;
}

void remove_sorted(int *arr, int *size, int value) {
    int i = 0;
    while (i < *size && arr[i] != value) i++;
    for (; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
}

int minimumCost(int *nums, int n, int k, int dist) {
    int required = k - 1;
    int chosen[1000], overflow[1000];
    int chosen_size = 0, overflow_size = 0;
    int chosen_sum = 0;

    for (int i = 1; i <= dist + 1; i++) {
        insert_sorted(chosen, &chosen_size, nums[i]);
        chosen_sum += nums[i];
        if (chosen_size > required) {
            int largest = chosen[chosen_size - 1];
            chosen_sum -= largest;
            chosen_size--;
            insert_sorted(overflow, &overflow_size, largest);
        }
    }

    int min_cost = nums[0] + chosen_sum;
    int left = 1;

    for (int right = dist + 2; right < n; right++) {
        int x = nums[left++];
        int found = 0;

        for (int i = 0; i < chosen_size; i++) {
            if (chosen[i] == x) {
                remove_sorted(chosen, &chosen_size, x);
                chosen_sum -= x;
                found = 1;
                if (overflow_size > 0) {
                    int y = overflow[0];
                    remove_sorted(overflow, &overflow_size, y);
                    insert_sorted(chosen, &chosen_size, y);
                    chosen_sum += y;
                }
                break;
            }
        }
        if (!found) {
            remove_sorted(overflow, &overflow_size, x);
        }

        insert_sorted(chosen, &chosen_size, nums[right]);
        chosen_sum += nums[right];
        if (chosen_size > required) {
            int largest = chosen[chosen_size - 1];
            chosen_sum -= largest;
            chosen_size--;
            insert_sorted(overflow, &overflow_size, largest);
        }

        int cost = nums[0] + chosen_sum;
        if (cost < min_cost) min_cost = cost;
    }

    return min_cost;
}
