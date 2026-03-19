const std = @import("std");

pub fn numberOfSubmatrices(grid: [][]const u8) usize {
    const rows = grid.len;
    const cols = grid[0].len;

    var allocator = std.heap.page_allocator;

    var col_x = allocator.alloc(usize, cols) catch unreachable;
    var col_y = allocator.alloc(usize, cols) catch unreachable;

    defer allocator.free(col_x);
    defer allocator.free(col_y);

    std.mem.set(usize, col_x, 0);
    std.mem.set(usize, col_y, 0);

    var result: usize = 0;

    for (grid) |row| {
        var row_x: usize = 0;
        var row_y: usize = 0;

        for (row, 0..) |cell, c| {
            if (cell == 'X') {
                row_x += 1;
            } else if (cell == 'Y') {
                row_y += 1;
            }

            col_x[c] += row_x;
            col_y[c] += row_y;

            if (col_x[c] != 0 and col_x[c] == col_y[c]) {
                result += 1;
            }
        }
    }

    return result;
}