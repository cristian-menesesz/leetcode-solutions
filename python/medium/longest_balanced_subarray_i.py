# You are given an integer array nums.

# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

# Return the length of the longest balanced subarray.

 

# Example 1:

# Input: nums = [2,5,4,3]

# Output: 4

# Explanation:

# The longest balanced subarray is [2, 5, 4, 3].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
# Example 2:

# Input: nums = [3,2,2,5,4]

# Output: 5

# Explanation:

# The longest balanced subarray is [3, 2, 2, 5, 4].
# It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
# Example 3:

# Input: nums = [1,2,3,2]

# Output: 3

# Explanation:

# The longest balanced subarray is [2, 3, 2].
# It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

# Constraints:

# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 105


def longestBalanced(self, nums: list[int]) -> int:
    
    array_length = len(nums)
    max_length = 0
    last_seen = [0] * (max(nums) + 1)

    for start in range(array_length):

        if array_length - start <= max_length:
            break

        distinct_counts = [0, 0]

        for end in range(start, array_length):
            value = nums[end]

            if last_seen[value] != start + 1:
                last_seen[value] = start + 1
                parity = value & 1
                distinct_counts[parity] += 1

            if distinct_counts[0] == distinct_counts[1]:
                max_length = max(max_length, end - start + 1)

    return max_length


# solution worked on top of a sliding window exploration combined with constant-time distinct tracking, it has been taken into account three main principles of the approach:

# 1. every possible subarray start is explored, but early termination is applied when it is impossible for the remaining elements to produce a better result than the current maximum
# 2. distinct values are tracked per window using a last-seen indexing strategy, avoiding re-counting the same value multiple times within the same starting position
# 3. the balance condition is evaluated incrementally by categorizing values by parity and updating counts only when a new distinct value appears in the current window

# [!] the last_seen array is reused across different window starts by encoding the window identity through start + 1, eliminating the need to reset auxiliary memory
# [!] the parity-based counting allows the balance condition to be checked in constant time at each step

# this leads to the computation of the maximum-length subarray where the number of distinct even
# values equals the number of distinct odd values


# time complexity: O(n^2) -> nested window expansion with constant-time updates
# space complexity: O(m) -> auxiliary arrays proportional to the maximum value in nums
