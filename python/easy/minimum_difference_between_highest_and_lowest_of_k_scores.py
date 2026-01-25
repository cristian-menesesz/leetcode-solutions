# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

 

# Example 1:

# Input: nums = [90], k = 1
# Output: 0
# Explanation: There is one way to pick score(s) of one student:
# - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
# The minimum possible difference is 0.
# Example 2:

# Input: nums = [9,4,1,7], k = 2
# Output: 2
# Explanation: There are six ways to pick score(s) of two students:
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
# - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
# - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
# - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
# The minimum possible difference is 2.
 

# Constraints:

# 1 <= k <= nums.length <= 1000
# 0 <= nums[i] <= 105


def minimumDifference(nums: list[int], k: int) -> int:

    if k == 1:
        return 0

    nums.sort()
    min_difference = float("inf")

    for left in range(len(nums) - k + 1):
        right = left + k - 1
        current_difference = nums[right] - nums[left]
        min_difference = min(min_difference, current_difference)

    return min_difference


# solution works on top of sorting + sliding window optimization, reducing the problem to comparing fixed-size contiguous segments in a monotonically ordered domain.

# 1. by sorting the array, all candidate groups of size k that minimize the difference must appear as contiguous subarrays.
# 2. the difference within any group of k elements is fully determined by its minimum (left) and maximum (right) values.
# 3. iterating with a fixed-size window ensures all valid candidate groups are evaluated exactly once, without redundant comparisons.

# [!] no dynamic programming is required, as overlapping subproblems do not exist
# [!] expanding or shrinking the window is unnecessary because k is fixed
# [!] sorting transforms a combinatorial selection problem into a linear scan

# this leads to scanning all contiguous windows of size k and tracking the minimum difference between the window endpoints.


# time complexity: O(n log n) -> sorting + linear scan
# space complexity: O(1) -> constant extra space (ignoring sort internals)
