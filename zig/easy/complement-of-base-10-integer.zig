const std = @import("std");

pub fn bitwiseComplement(n: u64) u64 {
    if (n == 0) return 1;

    const bit_len = std.math.log2_int(u64, n) + 1;
    const mask: u64 = (@as(u64, 1) << bit_len) - 1;

    return (~n) & mask;
}