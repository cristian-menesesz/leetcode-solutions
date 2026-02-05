# You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

# For each index i (where 0 <= i < nums.length), perform the following independent actions:
# If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.

# Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

 

# Example 1:

# Input: nums = [3,-2,1,1]

# Output: [1,1,1,3]

# Explanation:

# For nums[0] that is equal to 3, If we move 3 steps to right, we reach nums[3]. So result[0] should be 1.
# For nums[1] that is equal to -2, If we move 2 steps to left, we reach nums[3]. So result[1] should be 1.
# For nums[2] that is equal to 1, If we move 1 step to right, we reach nums[3]. So result[2] should be 1.
# For nums[3] that is equal to 1, If we move 1 step to right, we reach nums[0]. So result[3] should be 3.
# Example 2:

# Input: nums = [-1,4,-1]

# Output: [-1,-1,4]

# Explanation:

# For nums[0] that is equal to -1, If we move 1 step to left, we reach nums[2]. So result[0] should be -1.
# For nums[1] that is equal to 4, If we move 4 steps to right, we reach nums[2]. So result[1] should be -1.
# For nums[2] that is equal to -1, If we move 1 step to left, we reach nums[1]. So result[2] should be 4.
 

# Constraints:

# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100


def constructTransformedArray(self, nums: list[int]) -> list[int]:
        
    return [nums[(i+nums[i])%len(nums)] for i  in range(len(nums))]


# solution works on top of index transformation and modular arithmetic composition, where the resulting array is constructed by re-mapping each position based on a value-dependent offset within circular bounds.

# 1. each position i is treated as an independent transformation unit, meaning the resulting value at index i depends solely on nums[i] and its relative displacement from i
# 2. circular behavior is enforced through modulo arithmetic, guaranteeing that alltransformed indices remain within valid array bounds without conditional checks
# 3. since the transformation of each index does not depend on the transformation of any other index the operation can be expressed as a direct mapping rather than, an iterative or accumulative process

# [!] notice that no intermediate state or auxiliary structure is required, as the mapping is purely functional and stateless
# [!] the original array remains unchanged during the transformation, ensuring that index lookups are always consistent and deterministic

# this leads to the construction of a new array where each element is selected by applying a value-driven circular shift over the original array


# time complexity: O(n) -> single pass transformation over the input array
# space complexity: O(n) -> output array allocation
