# You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

# The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

# You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

# Return the minimum possible sum of the cost of these subarrays.

 

# Example 1:

# Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
# Output: 5
# Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
# Example 2:

# Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
# Output: 15
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
# The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
# Example 3:

# Input: nums = [10,8,18,9], k = 3, dist = 1
# Output: 36
# Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
# The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
 

# Constraints:

# 3 <= n <= 105
# 1 <= nums[i] <= 109
# 3 <= k <= n
# k - 2 <= dist <= n - 2


import bisect
from bisect import insort, bisect_left

def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
    n = len(nums)

    required_picks = k - 1
    chosen = []
    overflow = []
    chosen_sum = 0

    def add_value(x: int):
        nonlocal chosen_sum

        insort(chosen, x)
        chosen_sum += x

        if len(chosen) > required_picks:
            largest = chosen.pop()
            chosen_sum -= largest
            insort(overflow, largest)

    def remove_value(x: int):
        nonlocal chosen_sum

        idx = bisect_left(chosen, x)
        if idx < len(chosen) and chosen[idx] == x:
            chosen.pop(idx)
            chosen_sum -= x

            if overflow:
                smallest_overflow = overflow.pop(0)
                insort(chosen, smallest_overflow)
                chosen_sum += smallest_overflow
        else:
            idx = bisect_left(overflow, x)
            overflow.pop(idx)

    window_end = dist + 2
    initial_window = nums[1:window_end]

    initial_window.sort()
    chosen = initial_window[:required_picks]
    overflow = initial_window[required_picks:]
    chosen_sum = sum(chosen)

    min_cost = nums[0] + chosen_sum

    left = 1
    for right in range(window_end, n):
        remove_value(nums[left])
        add_value(nums[right])
        left += 1

        min_cost = min(min_cost, nums[0] + chosen_sum)

    return min_cost


# solution worked on top of an ordered sliding window optimization combined with greedy selection, it has been taken into account four main principles of the approach:

# 1. the first element is always part of the solution, therefore the problem is reduced to selecting k-1 optimal elements from a constrained window to minimize the total cost
# 2. the window of candidates is bounded by the distance constraint, so the solution is explored by sliding a fixed-size window over the array
# 3. within each window, the k-1 smallest values must be dynamically maintained to guarantee minimal contribution, which is achieved by splitting the window into a chosen set and an overflow set
# 4. insertion and removal operations preserve order and balance between sets, ensuring that the chosen set always contains the k-1 smallest valid elements

# [!] the chosen and overflow sets are kept sorted at all times to allow logarithmic-time insertions and removals
# [!] the chosen set size is strictly limited to k-1, enforcing the greedy invariant throughout the window transitions
# [!] each window update is independent, allowing the minimum cost to be evaluated incrementally without recomputation

# this leads to the computation of the minimum possible cost by iterating over all valid windows and combining the fixed first element with the dynamically maintained minimal subset


# time complexity: O(n log k) -> sliding window with ordered insertions and removals
# space complexity: O(k) -> storage of chosen and overflow elements
