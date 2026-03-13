#include <stdint.h>
#include <math.h>

static inline uint64_t isqrt_u64(uint64_t x) {
    uint64_t r = (uint64_t)sqrtl((long double)x);
    while (r * r > x) r--;
    while ((r + 1) * (r + 1) <= x) r++;
    return r;
}

static uint64_t max_height_in_time(uint64_t time, const uint64_t* worker_times, int n) {
    uint64_t total_height = 0;

    for (int i = 0; i < n; i++) {
        uint64_t worker_time = worker_times[i];

        uint64_t limit = (8 * time) / worker_time + 1;
        uint64_t k = (isqrt_u64(limit) - 1) / 2;

        total_height += k;
    }

    return total_height;
}

uint64_t min_number_of_seconds(uint64_t mountain_height,
                               const uint64_t* worker_times,
                               int n) {

    if (n == 1) {
        uint64_t w = worker_times[0];
        return w * mountain_height * (mountain_height + 1) / 2;
    }

    uint64_t left = 1;
    uint64_t right = (1000000000000ULL * mountain_height) / n;

    while (left < right) {
        uint64_t mid = left + (right - left) / 2;

        if (max_height_in_time(mid, worker_times, n) >= mountain_height)
            right = mid;
        else
            left = mid + 1;
    }

    return left;
}