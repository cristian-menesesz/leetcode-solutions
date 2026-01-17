# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

 

# Example 1:


# Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]

# Output: 1

# Explanation:

# A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

# Example 2:


# Input: bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]

# Output: 4

# Explanation:

# A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 2 * 2 = 4. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

# Example 3:

  
# Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]

# Output: 1

# Explanation:

# A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.

# Example 4:

  
# Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]

# Output: 0

# Explanation:

# No pair of rectangles intersect, hence, the answer is 0.

 

# Constraints:

# n == bottomLeft.length == topRight.length
# 2 <= n <= 103
# bottomLeft[i].length == topRight[i].length == 2
# 1 <= bottomLeft[i][0], bottomLeft[i][1] <= 107
# 1 <= topRight[i][0], topRight[i][1] <= 107
# bottomLeft[i][0] < topRight[i][0]
# bottomLeft[i][1] < topRight[i][1]


def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:

    rectangle_count = len(bottomLeft)
    max_square_side = 0

    for i in range(rectangle_count - 1):
        
        x1_i, y1_i = bottomLeft[i]
        x2_i, y2_i = topRight[i]

        for j in range(i + 1, rectangle_count):
            
            x1_j, y1_j = bottomLeft[j]
            x2_j, y2_j = topRight[j]
            intersection_width = min(x2_i, x2_j) - max(x1_i, x1_j)
            intersection_height = min(y2_i, y2_j) - max(y1_i, y1_j)

            if intersection_width <= 0 or intersection_height <= 0:
                continue

            square_side = min(intersection_width, intersection_height)
            max_square_side = max(max_square_side, square_side)

    return max_square_side * max_square_side


# solution worked on top of a brute-force geometric intersection analysis, where all meaningful pairs of rectangles are evaluated to determine the maximum square that can be formed from their overlapping area, it has been taken into account three main principles of the approach:

# 1. the solution iterates over every unique pair of rectangles, as a valid square can only emerge from the intersection of at least two rectangles
# 2. for each pair, the overlapping region is computed using coordinate-wise min/max operations, ensuring that only geometrically valid intersections are considered
# 3. from each valid intersection, the largest possible square is derived by taking the minimum between the intersection width and height, guaranteeing a square fits entirely inside the overlap

# [!] notice that rectangles with no positive intersection are immediately discarded, preventing invalid geometric regions from influencing the solution
# [!] the algorithm focuses on side length comparison only, deferring area computation to the final step, which simplifies intermediate reasoning and avoids unnecessary calculations

# this leads to the progressive evaluation of all rectangle intersections and the continuous update of the maximum square side that can be formed across the entire set


# time complexity: O(n^2) -> pairwise rectangle intersection checks
# space complexity: O(1) -> constant extra space, only scalar variables are used
