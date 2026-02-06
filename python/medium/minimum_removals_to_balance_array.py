# You are given an integer array nums and an integer k.

# An array is considered balanced if the value of its maximum element is at most k times the minimum element.

# You may remove any number of elements from nums​​​​​​​ without making it empty.

# Return the minimum number of elements to remove so that the remaining array is balanced.

# Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

 

# Example 1:

# Input: nums = [2,1,5], k = 2

# Output: 1

# Explanation:

# Remove nums[2] = 5 to get nums = [2, 1].
# Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
# Example 2:

# Input: nums = [1,6,2,9], k = 3

# Output: 2

# Explanation:

# Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
# Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
# Example 3:

# Input: nums = [4,6], k = 2

# Output: 0

# Explanation:

# Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 105


def min_removal(nums: list[int], k: int) -> int:
    
    nums.sort()
    n = len(nums)
    min_removals = n

    if nums[0] * k >= nums[-1]:
        return 0

    left = 0
    for right in range(n):

        while left < right and nums[left] * k < nums[right]:
            left += 1

        window_size = right - left + 1
        removals_needed = n - window_size
        min_removals = min(min_removals, removals_needed)

    return min_removals


# solution works on top of sorting and the sliding window technique, leveraging the monotonic properties induced by ordering the input array:

# 1. by sorting the array, any valid subset that satisfies the constraint nums[i] * k >= nums[j] must form a contiguous segment in the sorted order
# 2. a two-pointer window is expanded greedily to the right while maintaining the constraint, ensuring the widest possible valid window for each right boundary
# 3. when the constraint is violated, the left pointer is advanced to restore validity, preserving optimality without re-evaluating past states

# [!] notice that the sliding window never moves backward, which guarantees linear traversal after sorting
# [!] the problem is transformed from selecting elements to removing the minimum complement of a maximal valid window

# this leads to computing the maximum size window that satisfies the condition and deriving the minimum removals as the complement of that window


# time complexity: O(n log n) -> sorting dominates, sliding window traversal is O(n)
# space complexity: O(1) -> in-place sorting and constant extra variables
