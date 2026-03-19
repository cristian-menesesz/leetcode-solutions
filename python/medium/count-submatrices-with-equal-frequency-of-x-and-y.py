# Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

# grid[0][0]
# an equal frequency of 'X' and 'Y'.
# at least one 'X'.
 

# Example 1:

# Input: grid = [["X","Y","."],["Y",".","."]]

# Output: 3

# Explanation:



# Example 2:

# Input: grid = [["X","X"],["X","Y"]]

# Output: 0

# Explanation:

# No submatrix has an equal frequency of 'X' and 'Y'.

# Example 3:

# Input: grid = [[".","."],[".","."]]

# Output: 0

# Explanation:

# No submatrix has at least one 'X'.

 

# Constraints:

# 1 <= grid.length, grid[i].length <= 1000
# grid[i][j] is either 'X', 'Y', or '.'.


def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    
    col_x_counts = [0] * cols
    col_y_counts = [0] * cols
    
    result = 0

    for r in range(rows):
        row_x = row_y = 0  # prefix counts for current row

        for c in range(cols):
            cell = grid[r][c]

            if cell == 'X':
                row_x += 1
            elif cell == 'Y':
                row_y += 1

            # accumulate vertical prefix sums
            col_x_counts[c] += row_x
            col_y_counts[c] += row_y

            # valid if equal X and Y and at least one X
            if col_x_counts[c] > 0 and col_x_counts[c] == col_y_counts[c]:
                result += 1

    return result


# solution works on top of a prefix-sum dynamic counting approach, it leverages cumulative state reuse across rows and columns to efficiently evaluate submatrices:

# 1. the algorithm maintains running prefix counts of 'X' and 'Y' per row, allowing each cell to represent the total contribution of its row segment up to that column
# 2. these row-wise contributions are accumulated vertically into column prefix arrays, effectively encoding the total count of 'X' and 'Y' for all submatrices ending at the current cell
# 3. each position (r, c) implicitly represents a family of submatrices with bottom-right corner at (r, c), and the prefix structure allows constant-time validation of their aggregated properties
# 4. the condition of validity (equal number of 'X' and 'Y' with at least one 'X') is checked directly using the synchronized prefix sums without reconstructing submatrices

# [!] notice that the algorithm does not explicitly enumerate submatrices; instead, it compresses the state space through cumulative counting, avoiding higher-order complexity
# [!] the reuse of column accumulators transforms a 2D counting problem into an incremental 1D update per row, enabling efficient state propagation

# this leads to a linear scan over the grid where each cell aggregates and validates prefix information, resulting in the total number of valid submatrices


# time complexity: O(rows * cols) -> single pass over the grid with constant-time updates
# space complexity: O(cols) -> column-wise prefix accumulators
