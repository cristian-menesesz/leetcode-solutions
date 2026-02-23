#include <stdio.h>

int binaryGap(int n) {

    // Remove trailing zeros so the first bit is 1
    n /= (n & -n);

    if (n == 1)
        return 0;

    int longest_distance = 0;
    int zeros_since_last_one = 0;

    while (n) {
        if (n & 1) {  // Found a '1' bit
            if (zeros_since_last_one > longest_distance)
                longest_distance = zeros_since_last_one;

            zeros_since_last_one = 0;
        } else {      // Counting zeros between 1s
            zeros_since_last_one++;
        }

        n >>= 1;
    }

    // Distance = zeros between + 1
    return longest_distance + 1;
}