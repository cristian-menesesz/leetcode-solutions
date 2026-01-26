# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 

# Constraints:

# 2 <= arr.length <= 105
# -106 <= arr[i] <= 106


def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
    
    arr.sort()
    minimum_difference = float("inf")
    result_pairs = []

    for i in range(1, len(arr)):
        
        difference = arr[i] - arr[i - 1]

        if difference < minimum_difference:
            minimum_difference = difference
            result_pairs = [[arr[i - 1], arr[i]]]
        elif difference == minimum_difference:
            result_pairs.append([arr[i - 1], arr[i]])

    return result_pairs


# solution worked on top of a sorting + linear scan optimization approach, it has been taken into account two main principles of the problem:

# 1. by sorting the array, the minimum absolute difference between any two elements must occur between adjacent elements
# 2. a single linear pass after sorting is sufficient to evaluate all candidate pairs that could produce the minimum difference

# [!] notice that non-adjacent comparisons are intentionally ignored, as sorting guarantees they cannot produce a smaller difference
# [!] when a new smaller difference is found, previously stored pairs are discarded to preserve correctness

# this leads to a single pass accumulation of all pairs that achieve the global minimum absolute difference


# time complexity: O(n log n) -> sorting dominates the execution time
# space complexity: O(1) -> excluding output storage, only constant extra space is used