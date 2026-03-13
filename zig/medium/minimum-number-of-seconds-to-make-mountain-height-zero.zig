const std = @import("std");

fn maxHeightInTime(time: u64, worker_times: []const u64) u64 {
    var total_height: u64 = 0;

    for (worker_times) |worker_time| {
        // limit = floor(8*time/worker_time) + 1
        const limit: u64 = (8 * time) / worker_time + 1;

        const sqrt_val = std.math.sqrt(limit);
        const k: u64 = (sqrt_val - 1) / 2;

        total_height += k;
    }

    return total_height;
}

pub fn minNumberOfSeconds(mountainHeight: u64, workerTimes: []const u64) u64 {

    // fast path
    if (workerTimes.len == 1) {
        const w = workerTimes[0];
        return w * mountainHeight * (mountainHeight + 1) / 2;
    }

    var left: u64 = 1;
    var right: u64 = (1_000_000_000_000 * mountainHeight) / workerTimes.len;

    while (left < right) {
        const mid = (left + right) / 2;

        if (maxHeightInTime(mid, workerTimes) >= mountainHeight) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}