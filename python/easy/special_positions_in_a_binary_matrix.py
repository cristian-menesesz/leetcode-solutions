# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

# Example 1:


# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
# Example 2:


# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] is either 0 or 1.


def _indices_of_ones(self, row: list[int]) -> list[int]:
    """Return indices where the row contains a 1."""
    
    return [index for index, value in enumerate(row) if value == 1]

def numSpecial(self, matrix: list[list[int]]) -> int:
    
    rows = len(matrix)
    cols = len(matrix[0])

    special_count = 0
    column_checked = [False] * cols  # marks columns already processed

    for row_index in range(rows):
        one_indices = self._indices_of_ones(matrix[row_index])

        # Case 1: exactly one '1' in the row
        if len(one_indices) == 1:
            col_index = one_indices[0]

            if not column_checked[col_index]:
                column_checked[col_index] = True

                # count how many 1s exist in this column
                column_sum = sum(matrix[r][col_index] for r in range(rows))

                if column_sum == 1:
                    special_count += 1

        # Case 2: multiple 1s → mark columns as unusable
        else:
            for col_index in one_indices:
                column_checked[col_index] = True

    return special_count


# solution worked on top of a greedy validation approach with column pruning, supported by localized counting and state marking to avoid redundant computation. it has been taken into account three main principles of the problem:

# 1. a row can only contribute to the solution if it contains exactly one '1', therefore rows are first reduced to the indices where valid candidates may exist
# 2. once a column is analyzed or invalidated, it is marked to prevent recomputation, ensuring each column is processed at most once
# 3. validation of a candidate position is performed by confirming column uniqueness, meaning the column must also contain exactly one '1' across all rows

# [!] rows containing multiple '1's immediately invalidate their corresponding columns, since no position within them can satisfy the uniqueness constraint
# [!] column marking acts as a pruning mechanism that converts repeated global checks into single-pass decisions

# this leads to iterating through rows to identify candidate columns, pruning invalid columns early, and validating remaining candidates through constrained column aggregation.


# time complexity: O(m * n) -> worst-case column summations across rows
# space complexity: O(n) -> column state tracking
