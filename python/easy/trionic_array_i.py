# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.

 

# Example 1:

# Input: nums = [1,3,5,4,2,6]

# Output: true

# Explanation:

# Pick p = 2, q = 4:

# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).
# Example 2:

# Input: nums = [2,1,3]

# Output: false

# Explanation:

# There is no way to pick p and q to form the required three segments.

 

# Constraints:

# 3 <= n <= 100
# -1000 <= nums[i] <= 1000


def isTrionic(self, nums: list[int]) -> bool:
        
    n = len(nums)
    if n < 4:
        return False

    if nums[0] >= nums[1]:
        return False

    first_increase_finished = False
    decrease_finished = False

    direction = "increasing"

    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return False

        if direction == "increasing":
            if nums[i] < nums[i - 1]:
                if not first_increase_finished:
                    first_increase_finished = True
                    direction = "decreasing"
                else:
                    return False

        else:
            if nums[i] > nums[i - 1]:
                if not decrease_finished:
                    decrease_finished = True
                    direction = "increasing"
                else:
                    return False

    return first_increase_finished and decrease_finished


# solution works by modeling the array traversal as a finite-state directional scan, validating the existence of exactly three monotonic segments using a single pass and constant memory, it has been taken into account three main principles of the approach:

# 1. the array is traversed once while maintaining a current direction state ("increasing" or "decreasing"), ensuring local comparisons define global structure
# 2. a direction change is only allowed once per phase, enforcing exactly one transition from increasing → decreasing and one from decreasing → increasing
# 3. early termination is applied whenever a violation of strict monotonicity or an invalid extra transition is detected, preventing unnecessary computation

# [!] equality between consecutive elements is immediately rejected, as strict monotonicity is a core invariant of the approach
# [!] the first segment must start as increasing, otherwise the state machine would allow invalid configurations
# [!] flags are used to record completed phases, avoiding the need for auxiliary arrays or backtracking

# this leads to the validation of a trionic structure by confirming that both directional transitions occurred exactly once during the traversal


# time complexity: O(n) -> single linear pass through the array
# space complexity: O(1) -> constant extra space using directional state and boolean flags
