# You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

# You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. Note that other bars are fixed and cannot be removed.

# Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

 

# Example 1:



# Input: n = 2, m = 1, hBars = [2,3], vBars = [2]

# Output: 4

# Explanation:

# The left image shows the initial grid formed by the bars. The horizontal bars are [1,2,3,4], and the vertical bars are [1,2,3].

# One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

# Example 2:



# Input: n = 1, m = 1, hBars = [2], vBars = [2]

# Output: 4

# Explanation:

# To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

# Example 3:



# Input: n = 2, m = 3, hBars = [2,3], vBars = [2,4]

# Output: 4

# Explanation:

# One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.

 

# Constraints:

# 1 <= n <= 109
# 1 <= m <= 109
# 1 <= hBars.length <= 100
# 2 <= hBars[i] <= n + 1
# 1 <= vBars.length <= 100
# 2 <= vBars[i] <= m + 1
# All values in hBars are distinct.
# All values in vBars are distinct.


def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:

    hBars.sort()
    vBars.sort()

    def longest_consecutive_run(bars: list[int]) -> int:
        
        max_run = 1
        current_run = 1

        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                current_run += 1
            else:
                max_run = max(max_run, current_run)
                current_run = 1

        return max(max_run, current_run)

    max_horizontal_run = longest_consecutive_run(hBars)
    max_vertical_run = longest_consecutive_run(vBars)

    max_square_side = min(max_horizontal_run, max_vertical_run) + 1
    return max_square_side * max_square_side


# solution worked on top of a greedy + ordering-based scanning approach, it has been taken into account the following main principles of the problem:

# 1. the relative order of removed bars is irrelevant; only their sorted positions matter to detect contiguous gaps
# 2. consecutive removed bars represent a continuous free span, which directly determines the maximum possible side length extension in that direction
# 3. the maximum square that can be formed is constrained by the smaller of the maximum horizontal span and the maximum vertical span

# [!] the computation of consecutive spans is independent for horizontal and vertical bars, allowing the same logic to be reused
# [!] the final square side length is one unit larger than the longest consecutive run, since bars define boundaries, not cells

# this leads to computing the longest consecutive sequences in both dimensions, selecting the limiting dimension, and squaring the resulting side length to obtain the maximum square area


# time complexity: O(n log n + m log m) -> sorting bars + linear scan for consecutive runs
# space complexity: O(1) -> constant extra space, aside from input storage
