# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

# Example 1:


# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:

# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105


def submatrix_sum(
    self, r0: int, r1: int, c0: int, c1: int, prefix: list[list[int]]
) -> int:

    total = prefix[r1][c1]

    if r0 > 0:
        total -= prefix[r0 - 1][c1]
    if c0 > 0:
        total -= prefix[r1][c0 - 1]
    if r0 > 0 and c0 > 0:
        total += prefix[r0 - 1][c0 - 1]

    return total

def max_square_from_diagonal(
    self,
    start_row: int,
    start_col: int,
    rows: int,
    cols: int,
    prefix: list[list[int]],
    threshold: int,
) -> int:

    max_possible = min(rows - start_row, cols - start_col)
    best_length = 0

    left = 0
    for right in range(max_possible):
        r0 = start_row + left
        r1 = start_row + right
        c0 = start_col + left
        c1 = start_col + right

        current_sum = self.submatrix_sum(r0, r1, c0, c1, prefix)

        while left < right and current_sum > threshold:
            left += 1
            r0 += 1
            c0 += 1
            current_sum = self.submatrix_sum(r0, r1, c0, c1, prefix)

        if current_sum <= threshold:
            best_length = max(best_length, right - left + 1)

    return best_length

def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:

    rows, cols = len(mat), len(mat[0])

    for j in range(1, cols):
        mat[0][j] += mat[0][j - 1]

    for i in range(1, rows):
        mat[i][0] += mat[i - 1][0]
        for j in range(1, cols):
            mat[i][j] += (
                mat[i - 1][j]
                + mat[i][j - 1]
                - mat[i - 1][j - 1]
            )

    max_side = 0

    for i in range(rows):
        if rows - i <= max_side:
            break
        max_side = max(
            max_side,
            self.max_square_from_diagonal(i, 0, rows, cols, mat, threshold),
        )

    for j in range(1, cols):
        if cols - j <= max_side:
            break
        max_side = max(
            max_side,
            self.max_square_from_diagonal(0, j, rows, cols, mat, threshold),
        )

    return max_side


# solution works on top of 2D prefix sums combined with a diagonal-based sliding window strategy, exploiting monotonicity of square growth and threshold constraints to efficiently search valid squares

# 1. the matrix is first transformed into a 2D prefix sum grid, enabling O(1) submatrix sum queries
# 2. every possible square is uniquely identified by its top-left corner lying on either the first row or first column, which allows iterating only over diagonals instead of all (i, j) starting points
# 3. for each diagonal, a two-pointer (sliding window) technique is applied where the right pointer expands the square size along the diagonal and the left pointer shrinks the square whenever the threshold constraint is violated
# 4. the prefix sum inclusion–exclusion principle is used to compute square sums efficiently, ensuring that each diagonal is processed in linear time

# [!] the sliding window relies on the fact that increasing the square size monotonically increases its sum
# [!] each diagonal is independent, so no cross-diagonal state or shared DP is required
# [!] prefix sums overwrite the input matrix to achieve O(1) extra space usage

# this leads to scanning all candidate square sizes by diagonals in O(n^2) time, while validating each square sum in constant time using prefix sums


# time complexity: O(rows * cols) -> building prefix sums + diagonal scans
# space complexity: O(1) extra space -> prefix sums stored in-place
