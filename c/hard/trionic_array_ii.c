#include <limits.h>

long long maxTrionicSubarraySum(int* nums, int n) {
    const long long NEG_INF = -(1LL << 50);

    long long inc1 = NEG_INF;
    long long dec  = NEG_INF;
    long long inc2 = NEG_INF;
    long long best = NEG_INF;

    int prev = nums[0];

    for (int i = 1; i < n; i++) {
        int curr = nums[i];

        long long next_inc1 = NEG_INF;
        long long next_dec  = NEG_INF;
        long long next_inc2 = NEG_INF;

        if (curr > prev) {
            long long m1 = inc1 > prev ? inc1 : prev;
            next_inc1 = m1 + curr;

            long long m2 = dec > inc2 ? dec : inc2;
            next_inc2 = m2 + curr;
        } else if (curr < prev) {
            long long m = inc1 > dec ? inc1 : dec;
            next_dec = m + curr;
        }

        inc1 = next_inc1;
        dec  = next_dec;
        inc2 = next_inc2;

        if (inc2 > best) best = inc2;
        prev = curr;
    }

    return best;
}
