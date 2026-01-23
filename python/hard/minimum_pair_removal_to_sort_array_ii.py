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

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


import heapq

def minimumPairRemoval(self, nums: list[int]) -> int:
    
    n = len(nums)

    if self.is_non_decreasing(nums):
        return 0

    removed = [False] * n
    prev_idx = [i - 1 for i in range(n)]
    next_idx = [i + 1 if i + 1 < n else -1 for i in range(n)]

    heap = [(nums[i] + nums[i + 1], i) for i in range(n - 1)]
    heapq.heapify(heap)

    violations = sum(nums[i] > nums[i + 1] for i in range(n - 1))

    operations = 0

    while violations > 0:
        
        pair_sum, left = heapq.heappop(heap)

        if removed[left] or next_idx[left] == -1:
            continue

        right = next_idx[left]

        if removed[right] or nums[left] + nums[right] != pair_sum:
            continue

        left_prev = prev_idx[left]
        right_next = next_idx[right]

        if left_prev != -1 and nums[left_prev] > nums[left]:
            violations -= 1
        if nums[left] > nums[right]:
            violations -= 1
        if right_next != -1 and nums[right] > nums[right_next]:
            violations -= 1

        nums[left] = pair_sum
        removed[right] = True

        next_idx[left] = right_next
        if right_next != -1:
            prev_idx[right_next] = left

        if left_prev != -1 and nums[left_prev] > nums[left]:
            violations += 1
        if right_next != -1 and nums[left] > nums[right_next]:
            violations += 1

        if left_prev != -1:
            heapq.heappush(heap, (nums[left_prev] + nums[left], left_prev))
        if right_next != -1:
            heapq.heappush(heap, (nums[left] + nums[right_next], left))

        operations += 1

    return operations

def is_non_decreasing(arr: list[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# solution worked on top of a greedy strategy combined with a priority queue and dynamic adjacency tracking, where the objective is to eliminate local order violations by always collapsing the most cost-effective adjacent pair first.

# 1. the approach models the array as a mutable linked structure, allowing constant-time removal and reconnection of elements while preserving neighbor relationships throughout the process.
# 2. all adjacent pairs are evaluated through a min-heap, which prioritizes the pair with the smallest combined value, enforcing a greedy choice that minimizes the impact of each merge.
# 3. instead of rechecking global order after each operation, the algorithm maintains a running count of local violations, updating only the affected neighbor comparisons after each merge.
# 4. stale heap entries are safely ignored using lazy deletion, ensuring correctness without the overhead of heap cleanup or rebuilds.

# [!] the heap may contain outdated pair sums due to prior merges; correctness is preserved by validating indices, removal state, and current values before applying an operation.
# [!] only local comparisons around the merged pair are adjusted, avoiding full array scans and guaranteeing efficiency.

# this leads to an iterative reduction of violations until the structure becomes non-decreasing, with each operation collapsing exactly one adjacent pair while preserving consistency of the remaining sequence.


# time complexity: O(n log n) -> each merge and heap operation costs O(log n), with at most n merges
# space complexity: O(n) -> auxiliary arrays for adjacency tracking and the priority queue
