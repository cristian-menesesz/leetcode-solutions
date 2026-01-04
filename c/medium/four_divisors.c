#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    int sqrt_n = (int)sqrt(n);
    for (int i = 3; i <= sqrt_n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int sumFourDivisors(int nums[], int size) {
    int primes[] = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
        109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
        173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317
    };
    int primes_len = sizeof(primes) / sizeof(primes[0]);
    int total_sum = 0;

    for (int i = 0; i < size; i++) {
        int x = nums[i];
        if (x <= 1) continue;

        int sqrt_x = (int)sqrt(x);
        for (int j = 0; j < primes_len && primes[j] <= sqrt_x; j++) {
            int p = primes[j];
            if (x % p == 0) {
                int q = x / p;
                if (q != p && is_prime(q)) {
                    total_sum += 1 + p + q + x;
                    break;
                }
                if (q == p * p) {
                    total_sum += 1 + p + q + x;
                    break;
                }
            }
        }
    }
    return total_sum;
}
