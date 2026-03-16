from python import Python

OFFSET: Int = 50

@inline
fn rhombus_sum(
    r: Int,
    c: Int,
    d: Int,
    grid: List[List[Int]],
    diag_prefix: List[List[Int]],
    anti_prefix: List[List[Int]]
) -> Int:

    if d == 0:
        return grid[r][c]

    left = c - d
    right = c + d
    top = r - d
    bottom = r + d

    diag0 = top - c + OFFSET
    diag1 = r - left + OFFSET

    total = 0

    total += diag_prefix[diag0][right + 1] - diag_prefix[diag0][c]
    total += diag_prefix[diag1][c + 1] - diag_prefix[diag1][left]

    anti0 = top + c
    anti1 = bottom + c

    total += anti_prefix[anti0][r] - anti_prefix[anti0][top + 1]
    total += anti_prefix[anti1][bottom] - anti_prefix[anti1][r + 1]

    return total


fn get_biggest_three(grid: List[List[Int]]) -> List[Int]:

    rows = len(grid)
    cols = len(grid[0])

    diag_prefix = [[0]*(cols+1) for _ in range(100)]
    anti_prefix = [[0]*(rows+1) for _ in range(100)]

    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]

            diag_idx = r - c + OFFSET
            anti_idx = r + c

            diag_prefix[diag_idx][c+1] = diag_prefix[diag_idx][c] + val
            anti_prefix[anti_idx][r+1] = anti_prefix[anti_idx][r] + val

    best = [-1, -1, -1]
    max_radius = min(rows, cols) // 2

    for d in range(max_radius + 1):
        for r in range(d, rows - d):
            for c in range(d, cols - d):

                val = rhombus_sum(r, c, d, grid, diag_prefix, anti_prefix)

                if val in best:
                    continue

                if val > best[0]:
                    best[2] = best[1]
                    best[1] = best[0]
                    best[0] = val
                elif val > best[1]:
                    best[2] = best[1]
                    best[1] = val
                elif val > best[2]:
                    best[2] = val

    return [x for x in best if x != -1]