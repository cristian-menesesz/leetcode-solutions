const std = @import("std");

const OFFSET: i32 = 50;

fn rhombusSum(
    r: i32,
    c: i32,
    d: i32,
    grid: [][]i32,
    diag_prefix: [][]i32,
    anti_prefix: [][]i32,
) i32 {
    if (d == 0) return grid[@intCast(usize, r)][@intCast(usize, c)];

    const left = c - d;
    const right = c + d;
    const top = r - d;
    const bottom = r + d;

    const diag0 = top - c + OFFSET;
    const diag1 = r - left + OFFSET;

    var total: i32 = 0;

    total += diag_prefix[@intCast(usize, diag0)][@intCast(usize, right + 1)] -
             diag_prefix[@intCast(usize, diag0)][@intCast(usize, c)];

    total += diag_prefix[@intCast(usize, diag1)][@intCast(usize, c + 1)] -
             diag_prefix[@intCast(usize, diag1)][@intCast(usize, left)];

    const anti0 = top + c;
    const anti1 = bottom + c;

    total += anti_prefix[@intCast(usize, anti0)][@intCast(usize, r)] -
             anti_prefix[@intCast(usize, anti0)][@intCast(usize, top + 1)];

    total += anti_prefix[@intCast(usize, anti1)][@intCast(usize, bottom)] -
             anti_prefix[@intCast(usize, anti1)][@intCast(usize, r + 1)];

    return total;
}

pub fn getBiggestThree(grid: [][]i32) [3]i32 {
    const rows = grid.len;
    const cols = grid[0].len;

    var diag_prefix: [100][51]i32 = undefined;
    var anti_prefix: [100][51]i32 = undefined;

    std.mem.set(i32, &diag_prefix, 0);
    std.mem.set(i32, &anti_prefix, 0);

    for (grid, 0..) |row, r| {
        for (row, 0..) |val, c| {
            const diag_idx = @as(i32, @intCast(r)) - @as(i32, @intCast(c)) + OFFSET;
            const anti_idx = @as(i32, @intCast(r + c));

            diag_prefix[@intCast(usize, diag_idx)][c + 1] =
                diag_prefix[@intCast(usize, diag_idx)][c] + val;

            anti_prefix[@intCast(usize, anti_idx)][r + 1] =
                anti_prefix[@intCast(usize, anti_idx)][r] + val;
        }
    }

    var best = [_]i32{-1, -1, -1};
    const max_radius = @min(rows, cols) / 2;

    var d: usize = 0;
    while (d <= max_radius) : (d += 1) {
        var r: usize = d;
        while (r < rows - d) : (r += 1) {
            var c: usize = d;
            while (c < cols - d) : (c += 1) {

                const val = rhombusSum(
                    @intCast(i32, r),
                    @intCast(i32, c),
                    @intCast(i32, d),
                    grid,
                    diag_prefix[0..],
                    anti_prefix[0..],
                );

                if (val == best[0] or val == best[1] or val == best[2]) continue;

                if (val > best[0]) {
                    best[2] = best[1];
                    best[1] = best[0];
                    best[0] = val;
                } else if (val > best[1]) {
                    best[2] = best[1];
                    best[1] = val;
                } else if (val > best[2]) {
                    best[2] = val;
                }
            }
        }
    }

    return best;
}