#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool hasAllCodes(const char* s, int k) {
    int n = strlen(s);

    if (n < k)
        return false;

    int total_codes = 1 << k;
    int window_mask = 0;
    int lower_bits_mask = (1 << (k - 1)) - 1;

    // boolean array instead of set
    bool* seen = (bool*)calloc(total_codes, sizeof(bool));
    int seen_count = 0;

    // ---- build first window ----
    for (int i = 0; i < k; i++) {
        window_mask = (window_mask << 1) | (s[i] == '1');
    }

    seen[window_mask] = true;
    seen_count = 1;

    // ---- sliding window ----
    for (int right = k; right < n; right++) {
        // remove highest bit
        window_mask &= lower_bits_mask;

        // shift + add new bit
        window_mask = (window_mask << 1) | (s[right] == '1');

        if (!seen[window_mask]) {
            seen[window_mask] = true;
            seen_count++;

            if (seen_count == total_codes) {
                free(seen);
                return true;
            }
        }
    }

    bool result = (seen_count == total_codes);
    free(seen);
    return result;
}