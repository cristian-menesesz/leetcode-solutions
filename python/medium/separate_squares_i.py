# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted multiple times.

 

# Example 1:

# Input: squares = [[0,0,1],[2,2,1]]

# Output: 1.00000

# Explanation:



# Any horizontal line between y = 1 and y = 2 will have 1 square unit above it and 1 square unit below it. The lowest option is 1.

# Example 2:

# Input: squares = [[0,0,2],[1,1,1]]

# Output: 1.16667

# Explanation:



# The areas are:

# Below the line: 7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5.
# Above the line: 5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5.
# Since the areas above and below the line are equal, the output is 7/6 = 1.16667.

 

# Constraints:

# 1 <= squares.length <= 5 * 104
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 109
# 1 <= li <= 109
# The total area of all the squares will not exceed 1012.


def area_above_y(squares: list[list[int]], cut_y: float) -> float:

    total_area = 0.0

    for _, bottom_y, side in squares:
        
        top_y = bottom_y + side

        if cut_y >= top_y:
            continue

        visible_height = min(side, top_y - cut_y)
        total_area += side * visible_height

    return total_area

def separateSquares(self, squares: list[list[int]]) -> float:

    total_area = self.area_above_y(squares, -1e18)
    half_area = total_area / 2.0
    min_y = float("inf")
    max_y = float("-inf")

    for _, bottom_y, side in squares:
        min_y = min(min_y, bottom_y)
        max_y = max(max_y, bottom_y + side)

    left, right = min_y, max_y
    epsilon = 1e-5

    while right - left > epsilon:
        
        mid = (left + right) / 2.0
        area_above = self.area_above_y(squares, mid)

        if area_above > half_area:
            left = mid
        else:
            right = mid

    return left


# 1. the accumulated area above a horizontal cut y is a monotonically non-increasing function, meaning that as y increases, the visible area of all squares above that cut can only decrease
# 2. the area contributed by each square can be computed independently, since squares do not interact or overlap in the vertical aggregation logic, allowing a simple summation per evaluation
# 3. because the target is to split the total area into two equal halves, the problem reduces to finding a cut y such that the area above y equals half of the total area, which is a root-finding problem on a monotonic function

# [!] the area computation ignores squares fully below the cut, as they contribute zero area and do not affect the monotonic behavior
# [!] precision is controlled via an epsilon threshold, trading exactness for convergence guarantees in continuous space
# [!] the algorithm does not require sorting or modifying the input, preserving the original structure of the data

# this leads to a solution that repeatedly evaluates the area above a candidate cut using a linear pass, while narrowing the search interval through binary search until the cut that separates the total area into two equal parts is found


# time complexity: O(n log R) -> n per area evaluation, log R binary search iterations over the y-range
# space complexity: O(1) -> constant extra space, independent of input size
