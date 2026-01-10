#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int minimumDeleteSum(char* s1, char* s2) {
    int len_a = strlen(s1);
    int len_b = strlen(s2);

    // Ensure len_a >= len_b
    if (len_a < len_b) {
        return minimumDeleteSum(s2, s1);
    }

    int dp[2][1001] = {0}; // assuming max length <= 1000

    for (int i = 0; i < len_a; i++) {
        int curr = (i + 1) & 1;
        int prev = curr ^ 1;

        for (int j = 0; j < len_b; j++) {
            if (s1[i] == s2[j]) {
                dp[curr][j + 1] = (int)s1[i] + dp[prev][j];
            } else {
                dp[curr][j + 1] = max(dp[prev][j + 1], dp[curr][j]);
            }
        }
    }

    int total = 0;
    for (int i = 0; i < len_a; i++) total += (int)s1[i];
    for (int j = 0; j < len_b; j++) total += (int)s2[j];

    int max_common = dp[len_a & 1][len_b];
    return total - 2 * max_common;
}
