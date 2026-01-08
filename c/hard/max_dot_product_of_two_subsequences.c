#include <limits.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int maxDotProduct(int* nums1, int len1, int* nums2, int len2) {
    
    if (len1 < len2) {
        return maxDotProduct(nums2, len2, nums1, len1);
    }

    const int NEG_INF = INT_MIN / 2;
    int dp[2][501];

    for (int r = 0; r < 2; r++) {
        for (int j = 0; j <= len2; j++) {
            dp[r][j] = NEG_INF;
        }
    }

    int max_result = NEG_INF;

    for (int i = len1 - 1; i >= 0; i--) {
        
        int curr = i & 1;
        int next = (i + 1) & 1;

        for (int j = len2 - 1; j >= 0; j--) {
            
            int product = nums1[i] * nums2[j];
            
            int best = product;

            best = max(best, product + dp[next][j + 1]);
            
            best = max(best, dp[curr][j + 1]);
            
            dp[curr][j] = max(best, dp[next][j]);

            max_result = max(max_result, dp[curr][j]);
        }
    }

    return max_result;
}
