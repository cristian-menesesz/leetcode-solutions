# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100


def countNegatives(grid: list[list[int]]) -> int:
    
    m = len(grid)
    n = len(grid[0])
    i = m - 1
    j = 0
    negative_count = 0

    while i >= 0 and j < n:
        if grid[i][j] < 0:
            negative_count += n - j
            i -= 1
        else:
            j += 1

    return negative_count


# solution worked on top of a monotonic matrix traversal (greedy two-pointer scan),
# it leverages the sorted properties of the grid to eliminate unnecessary checks:

# 1. the grid is sorted in non-increasing order both row-wise and column-wise,
#    which guarantees that once a negative value is found, all elements to its right
#    in the same row are also negative
# 2. the traversal starts from the bottom-left corner, as this position allows
#    deciding in constant time whether to move upward (when a negative is found)
#    or rightward (when the value is non-negative)
# 3. when a negative element is encountered, the count of negatives in that row
#    can be computed in bulk (n - j), avoiding per-element iteration

# [!] once a negative is found at position (i, j), all cells (i, j+1 ... n-1)
#     are implicitly negative due to row ordering
# [!] each movement (up or right) strictly reduces the remaining search space,
#     ensuring no cell is visited more than once

# this leads to a linear traversal over the grid dimensions, accumulating the
# total number of negative elements efficiently without auxiliary data structures


# time complexity: O(m + n)
# space complexity: O(1)