# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

# Example 1:


# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12
# Example 2:


# Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
# Output: 2
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 106


def largestMagicSquare(self, grid: list[list[int]]) -> int:
    
    rows, cols = len(grid), len(grid[0])
    row_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    col_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    diag_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    anti_diag_prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(rows):
        for j in range(cols):
            value = grid[i][j]
            row_prefix[i + 1][j + 1] = row_prefix[i + 1][j] + value
            col_prefix[i + 1][j + 1] = col_prefix[i][j + 1] + value
            diag_prefix[i + 1][j + 1] = diag_prefix[i][j] + value
            anti_diag_prefix[i + 1][j] = anti_diag_prefix[i][j + 1] + value

    def is_magic_square(size: int) -> bool:

        for top in range(rows - size + 1):
            for left in range(cols - size + 1):
                main_diag_sum = (
                    diag_prefix[top + size][left + size]
                    - diag_prefix[top][left]
                )
                anti_diag_sum = (
                    anti_diag_prefix[top + size][left]
                    - anti_diag_prefix[top][left + size]
                )

                if main_diag_sum != anti_diag_sum:
                    continue

                valid = True

                for offset in range(size):
                    row_sum = (
                        row_prefix[top + offset + 1][left + size]
                        - row_prefix[top + offset + 1][left]
                    )
                    col_sum = (
                        col_prefix[top + size][left + offset + 1]
                        - col_prefix[top][left + offset + 1]
                    )

                    if row_sum != main_diag_sum or col_sum != main_diag_sum:
                        valid = False
                        break

                if valid:
                    return True

        return False

    for size in range(min(rows, cols), 1, -1):
        if is_magic_square(size):
            return size

    return 1


# solution is based on a prefix-sum optimization approach combined with a decreasing-size validation strategy where constant-time range queries allow exhaustive verification of candidate squares efficiently

# 1. the grid is preprocessed into four independent prefix-sum structures (rows columns main diagonal and anti-diagonal) enabling O(1) computation of any row column or diagonal sum inside a sub-square
# 2. the validation of a square relies on fixing the diagonal sum as an invariant and checking all rows and columns against this invariant using prefix differences
# 3. candidate magic squares are explored in decreasing order of size ensuring that the first valid square found is the largest possible and allowing early termination of the search

# [!] diagonal sums are computed only once per candidate square and reused as the reference value
# [!] prefix sums transform repeated summations inside nested loops into constant-time operations
# [!] the algorithm prioritizes correctness over pruning heuristics relying on preprocessing to remain efficient

# this leads to a brute-force exploration over all square positions and sizes optimized by prefix sums where each candidate is validated in linear time with respect to its side length


# time complexity: O(n^3) -> size iteration O(n) * position scanning O(n^2) with O(1) range checks
# space complexity: O(n^2) -> prefix sum matrices storing cumulative grid information
