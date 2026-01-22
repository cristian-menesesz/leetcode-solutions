# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

# Example 1:

# Input: nums = [5,2,3,1]

# Output: 2

# Explanation:

# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.

# Example 2:

# Input: nums = [1,2,2]

# Output: 0

# Explanation:

# The array nums is already sorted.

 

# Constraints:

# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000


def minimumPairRemoval(self, nums: list[int]) -> int:

    REMOVED = float("inf")

    def is_non_decreasing_ignoring_removed(arr: list[int]) -> bool:

        prev_value = float("-inf")

        for value in arr:
            if value == REMOVED:
                continue

            if value < prev_value:
                return False

            prev_value = value

        return True
    
    operations = 0
    n = len(nums)

    while not is_non_decreasing_ignoring_removed(nums):
        
        min_pair_sum = float("inf")
        left_idx = right_idx = -1

        i = 0
        while i < n - 1:
            if nums[i] == REMOVED:
                i += 1
                continue

            j = i + 1
            while j < n and nums[j] == REMOVED:
                j += 1

            if j < n:
                pair_sum = nums[i] + nums[j]
                if pair_sum < min_pair_sum:
                    min_pair_sum = pair_sum
                    left_idx, right_idx = i, j

            i += 1

        if left_idx != -1:
            nums[left_idx] += nums[right_idx]
            nums[right_idx] = REMOVED
            operations += 1
        else:
            break

    return operations


# solution is based on a greedy iterative reduction strategy, combined with state masking to simulate removals, taking into account three main principles of the approach:

# 1. the array is progressively transformed by merging exactly one adjacent valid pair per iteration, ensuring that each operation strictly reduces the number of active (non-removed) elements
# 2. at each step, the locally optimal decision is to merge the adjacent pair with the minimum possible sum, as this minimizes the risk of creating future decreasing violations in the remaining sequence
# 3. removed elements are not physically deleted but logically ignored using a sentinel value, allowing index stability while preserving the relative order of remaining elements

# [!] the non-decreasing check is performed ignoring removed elements, effectively treating the array as a compressed sequence without rebuilding it
# [!] adjacency is defined relative to the current valid elements, not raw indices, which requires skipping removed positions during pair selection

# this leads to an iterative process where the array monotonically approaches a non-decreasing state through greedy pair merging, counting the number of such operations required


# time complexity: O(n^2) -> each iteration scans the array to check order and find the minimum-sum valid pair
# space complexity: O(1) -> all transformations are performed in-place using a constant sentinel value
