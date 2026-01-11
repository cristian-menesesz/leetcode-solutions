# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= rows, cols <= 200
# matrix[i][j] is '0' or '1'.


def maximalRectangle(self, matrix: list[list[str]]) -> int:

    if not matrix or not matrix[0]:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    consecutive_ones_height = [0] * cols
    max_rectangle_area = 0
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '0':
                consecutive_ones_height[col] = 0
            else:
                consecutive_ones_height[col] += 1
        
        max_rectangle_area = max(
            max_rectangle_area, 
            self._find_max_rectangle_area(consecutive_ones_height)
        )
    
    return max_rectangle_area

def _find_max_rectangle_area(self, heights: list[int]) -> int:

    n = len(heights)
    if n == 0:
        return 0
    
    left_limit = [-1] * n
    right_limit = [n] * n
    
    for i in range(1, n):
        
        boundary = i - 1
        
        while boundary >= 0 and heights[boundary] >= heights[i]:
            boundary = left_limit[boundary]
        left_limit[i] = boundary
    
    max_area = heights[-1] * (right_limit[-1] - left_limit[-1] - 1)
    
    for i in range(n - 2, -1, -1):
        
        boundary = i + 1

        while boundary < n and heights[boundary] >= heights[i]:
            boundary = right_limit[boundary]
        
        right_limit[i] = boundary
        
        rectangle_width = right_limit[i] - left_limit[i] - 1
        area = heights[i] * rectangle_width
        max_area = max(max_area, area)
    
    return max_area


# solution works on top of dynamic programming with histogram compression, reducing a 2D maximal rectangle problem into a sequence of 1D maximal rectangle subproblems.

# 1. each row is treated as the base of a histogram, where the height of each column represents the number of consecutive '1's ending at the current row.
# 2. the histogram heights are updated incrementally row by row, allowing reuse of previously computed information instead of recomputing from scratch.
# 3. for each histogram, the largest rectangle is computed by determining, for every bar, the maximum horizontal span where that bar can act as the limiting height.
# 4. the horizontal span is obtained by precomputing the nearest smaller element to the left and to the right of each bar, effectively defining the maximal width for each possible rectangle height.
# 5. the global maximum rectangle area is updated by comparing the best rectangle found at each row.

# [!] the transformation from matrix rows to histograms is the key abstraction that enables a 2D problem to be solved using a well-known 1D strategy.
# [!] left and right boundaries skip over blocks of greater or equal height, ensuring amortized linear processing per histogram.
# [!] each histogram is independent once constructed, making the solution modular and easy to reason about.

# this leads to scanning the matrix row by row, accumulating vertical heights, and computing the maximal rectangle in each resulting histogram to obtain the global maximum area.


# time complexity: O(rows * cols) -> histogram construction = O(rows * cols), largest rectangle per row = O(cols)
# space complexity: O(cols) -> height array + left/right boundary memoization = O(cols)
