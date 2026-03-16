# You are given an m x n integer matrix grid​​​.

# A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


# Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

# Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

# Example 1:


# Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211
# Example 2:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [20,9,8]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
# - Blue: 4 + 2 + 6 + 8 = 20
# - Red: 9 (area 0 rhombus in the bottom right corner)
# - Green: 8 (area 0 rhombus in the bottom middle)
# Example 3:

# Input: grid = [[7,7,7]]
# Output: [7]
# Explanation: All three possible rhombus sums are the same, so return [7].
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 105


OFFSET = 50

def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
    rows, cols = len(grid), len(grid[0])

    diag_prefix = [[0] * (cols + 1) for _ in range(100)]
    anti_prefix = [[0] * (rows + 1) for _ in range(100)]

    # build diagonal prefix sums
    for r in range(rows):
        for c in range(cols):
            diag_idx = r - c + OFFSET
            anti_idx = r + c
            val = grid[r][c]

            diag_prefix[diag_idx][c + 1] = diag_prefix[diag_idx][c] + val
            anti_prefix[anti_idx][r + 1] = anti_prefix[anti_idx][r] + val

    def rhombus_sum(r: int, c: int, d: int) -> int:
        if d == 0:
            return grid[r][c]

        left, right = c - d, c + d
        top, bottom = r - d, r + d

        # "\" diagonals
        diag0 = top - c + OFFSET
        diag1 = r - left + OFFSET

        total = diag_prefix[diag0][right + 1] - diag_prefix[diag0][c]
        total += diag_prefix[diag1][c + 1] - diag_prefix[diag1][left]

        # "/" diagonals (without corners)
        anti0 = top + c
        anti1 = bottom + c

        total += anti_prefix[anti0][r] - anti_prefix[anti0][top + 1]
        total += anti_prefix[anti1][bottom] - anti_prefix[anti1][r + 1]

        return total

    best = [-1, -1, -1]
    max_radius = min(rows, cols) // 2

    for d in range(max_radius + 1):
        for r in range(d, rows - d):
            for c in range(d, cols - d):
                val = rhombus_sum(r, c, d)

                if val in best:
                    continue

                if val > best[0]:
                    best[2] = best[1]
                    best[1] = best[0]
                    best[0] = val
                elif val > best[1]:
                    best[2] = best[1]
                    best[1] = val
                elif val > best[2]:
                    best[2] = val

    return [x for x in best if x != -1]


# solution worked on top of the prefix sums advantages applied over diagonal directions,
# it has been taken into account four main principles of the problem:

# 1. the perimeter of any rhombus in the grid is composed of four diagonal segments,
#    two belonging to "\" diagonals and two belonging to "/" diagonals
# 2. as every cell belongs to a unique "\" diagonal (r - c) and a unique "/" diagonal (r + c),
#    it is possible to group cells by those diagonals and build prefix sums for each of them
# 3. once diagonal prefix sums are built, any rhombus perimeter can be decomposed into four
#    contiguous diagonal ranges whose sums can be obtained in constant time
# 4. by enumerating every valid center (r, c) and radius d, all rhombus perimeters can be
#    evaluated while maintaining the three largest distinct values

# [!] an offset is required to normalize (r - c) indices so they can be used safely as array indices
# [!] the rhombus perimeter excludes duplicated corner contributions by separating "\" edges
#     from "/" edges and adjusting the queried prefix ranges
# [!] only the three largest distinct sums are tracked, avoiding the need to store all candidates

# this leads to the computation of rhombus perimeter sums in O(1) using diagonal prefix sums,
# while scanning all valid centers and radii and maintaining the three largest unique values


# time complexity: O(n^3) -> enumeration of centers and radii with O(1) rhombus sum computation
# space complexity: O(n^2) -> storage of diagonal prefix sums
