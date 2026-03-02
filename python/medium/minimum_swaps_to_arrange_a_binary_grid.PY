# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

# A grid is said to be valid if all the cells above the main diagonal are zeros.

# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

# Example 1:


# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# Example 2:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# Example 3:


# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0
 

# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1


def minSwaps(self, grid: list[list[int]]) -> int:
    
    n = len(grid)

    # Count trailing zeros for each row
    trailing_zeros_per_row = [
        (row[::-1] + [1]).index(1)
        for row in grid
    ]

    swap_count = 0

    for target_row in range(n):
        min_required_zeros = n - 1 - target_row

        # Find closest row that can satisfy this position
        candidate_row = next(
            (
                idx
                for idx, zeros in enumerate(trailing_zeros_per_row)
                if zeros >= min_required_zeros
            ),
            -1
        )

        if candidate_row == -1:
            return -1

        swap_count += candidate_row
        trailing_zeros_per_row.pop(candidate_row)

    return swap_count


# solution worked on top of a greedy ordering strategy supported by structural constraints of the grid rows, where local optimal swaps guarantee the global minimum number of adjacent swaps required to satisfy the validity condition

# 1. each row is reduced to a single invariant: the number of trailing zeros, since only this property determines whether a row can occupy a specific position in the final grid configuration
# 2. the grid validity condition induces an ordering constraint where the i-th row must contain at least (n - 1 - i) trailing zeros, transforming the problem into progressively selecting feasible rows for each position
# 3. at every step, the closest row that satisfies the requirement is selected, because moving any farther valid row would introduce unnecessary swaps, therefore a greedy choice minimizes total adjacent swaps
# 4. once a row is placed, it is removed from further consideration, reducing the remaining problem into a smaller independent subproblem with the samestructure

# [!] the algorithm does not simulate swaps explicitly; instead, the index of the selected candidate represents the exact number of adjacent swapsneeded to bring that row into position
# [!] feasibility is checked incrementally; if no remaining row satisfies the required trailing-zero constraint at any step, the configuration is impossible and the algorithm terminates early

# this leads to iteratively constructing a valid row ordering while accumulating the minimum swap cost implied by each greedy selection


# time complexity: O(n^2) -> scanning remaining rows for each position
# space complexity: O(n) -> trailing zero representation of rows
