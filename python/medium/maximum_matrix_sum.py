# You are given an n x n integer matrix. You can do the following operation any number of times:

# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

# Example 1:


# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:


# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.
 

# Constraints:

# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105


def maxMatrixSum(self, matrix: list[list[int]]) -> int:

    total_sum = 0
    min_abs = float('inf')
    negative_count = 0

    for row in matrix:
        for value in row:
            abs_val = abs(value)
            total_sum += abs_val

            if abs_val < min_abs:
                min_abs = abs_val

            if value < 0:
                negative_count += 1

    if negative_count % 2 == 0:
        return total_sum
    else:
        return total_sum - 2 * min_abs


# solution worked on top of a greedy aggregation approach, it has been taken into account three main principles of the problem:

# 1. the absolute value of every element contributes positively to the maximum possible sum, regardless of its sign
# 2. the parity (even or odd) of the total number of negative elements determines whether all absolute values can be kept as-is
# 3. when the number of negative elements is odd, exactly one element must remain negative, and to minimize the penalty, it must be the one with the smallest absolute value

# [!] notice that the algorithm never modifies the matrix explicitly; it reasons purely on aggregated properties (sum of absolute values, minimum absolute value, and negative count)
# [!] notice that the decision logic is deferred until the full traversal is completed, ensuring correctness based on global parity rather than local choices

# this leads to the computation of the total absolute sum of the matrix, followed by a parity-based adjustment using the minimum absolute value when required


# time complexity: O(n^2) -> full traversal of the matrix
# space complexity: O(1) -> constant extra variables independent of input size