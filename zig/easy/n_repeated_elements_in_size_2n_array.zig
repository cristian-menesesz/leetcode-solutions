const std = @import("std");

pub fn repeatedNTimes(allocator: std.mem.Allocator, nums: []const i32) !i32 {
    var seen = std.AutoHashMap(i32, void).init(allocator);
    defer seen.deinit();

    for (nums) |number| {
        if (seen.contains(number)) {
            return number;
        }
        try seen.put(number, {});
    }

    return -1;
}
