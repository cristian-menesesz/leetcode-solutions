# You are given an integer array nums of length n.

# A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

# nums[l...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...r] is strictly increasing.
# Return the maximum sum of any trionic subarray in nums.

 

# Example 1:

# Input: nums = [0,-2,-1,-3,0,2,-1]

# Output: -4

# Explanation:

# Pick l = 1, p = 2, q = 3, r = 5:

# nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
# nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
# nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
# Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.
# Example 2:

# Input: nums = [1,4,2,7]

# Output: 14

# Explanation:

# Pick l = 0, p = 1, q = 2, r = 3:

# nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
# nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
# nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
# Sum = 1 + 4 + 2 + 7 = 14.
 

# Constraints:

# 4 <= n = nums.length <= 105
# -109 <= nums[i] <= 109
# It is guaranteed that at least one trionic subarray exists.


def maxTrionicSubarraySum(self, nums: list[int]) -> int:
    
    NEG_INF = -(1 << 50)
    inc1 = dec = inc2 = NEG_INF
    best = NEG_INF
    prev = nums[0]

    for i in range(1, len(nums)):
        
        curr = nums[i]
        next_inc1 = next_dec = next_inc2 = NEG_INF

        if curr > prev:
            next_inc1 = max(inc1, prev) + curr
            next_inc2 = max(dec, inc2) + curr

        elif curr < prev:
            next_dec = max(inc1, dec) + curr

        inc1, dec, inc2 = next_inc1, next_dec, next_inc2
        best = max(best, inc2)
        prev = curr

    return best


# solution worked on top of a dynamic programming state-machine approach with constant-space memoization, modeling directional transitions between consecutive elements to capture a trionic subarray pattern

# 1. the algorithm models three ordered states: first increasing phase (inc1), decreasing phase (dec), second increasing phase (inc2). each state represents the best achievable subarray sum ending at the current position while respecting the phase constraints up to that point

# 2. transitions between states are driven exclusively by the comparison of consecutive elements (curr vs prev), ensuring that the subarray respects the required directional pattern without explicitly storing indices or subarrays

# 3. each state is updated independently using the previous iteration’s values, allowing invalid transitions to be discarded naturally by initializing unreachable states with negative infinity

# [!] only valid directional transitions are allowed: increasing → decreasing → increasing, and any violation automatically invalidates the corresponding state without special-case handling

# [!] the use of rolling variables replaces a full DP table, guaranteeing constant space usage while preserving correctness

# this leads to the incremental construction of the maximum trionic subarray sum, where the final answer is the maximum value reached in the second increasing state


# time complexity: O(n) -> single pass with constant-time state transitions
# space complexity: O(1) -> constant number of DP states
