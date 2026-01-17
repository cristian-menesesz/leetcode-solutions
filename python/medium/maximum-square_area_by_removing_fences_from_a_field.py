# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

# Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

# Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

# Since the answer may be large, return it modulo 109 + 7.

# Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

 

# Example 1:



# Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
# Output: 4
# Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
# Example 2:



# Input: m = 6, n = 7, hFences = [2], vFences = [4]
# Output: -1
# Explanation: It can be proved that there is no way to create a square field by removing fences.
 

# Constraints:

# 3 <= m, n <= 109
# 1 <= hFences.length, vFences.length <= 600
# 1 < hFences[i] < m
# 1 < vFences[i] < n
# hFences and vFences are unique.


def compute_gaps(self, fences: list[int], max_coordinate: int) -> set[int]:
    
    points = [1, max_coordinate]
    points.extend(fences)
    points.sort()

    gaps = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            gaps.add(points[j] - points[i])

    return gaps

def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
    
    MOD = 10**9 + 7

    horizontal_gaps = self.compute_gaps(hFences, m)
    vertical_gaps = self.compute_gaps(vFences, n)

    max_side = max(horizontal_gaps & vertical_gaps, default=0)
    
    return -1 if max_side == 0 else (max_side * max_side) % MOD


# solution worked on top of a combinatorial enumeration approach with set-based intersection, it has been taken into account three main principles of the problem:

# 1. the valid side length of a square is fully determined by the distance between any two horizontal fences and any two vertical fences, including the implicit borders of the grid
# 2. by enumerating all possible gaps between fence coordinates, the problem is reduced to comparing feasible horizontal and vertical side lengths independently
# 3. the largest possible square side is obtained by intersecting both sets of gaps and selecting the maximum common value

# [!] notice that the grid boundaries are explicitly included as fences to ensure that edge-aligned squares are considered
# [!] as horizontal and vertical dimensions are independent, gap computation can be reused symmetrically for both axes

# this leads to the computation of all feasible square side lengths via set intersection, and the selection of the maximum valid square whose area is then computed


# time complexity: O(k^2 + l^2) -> gap enumeration for horizontal and vertical fences
# space complexity: O(k^2 + l^2) -> storage of all possible gaps in sets
