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

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105


class SegmentNode:
    __slots__ = ("min_value", "max_value", "lazy")

    def __init__(self, value: int = None):
        if value is None:
            self.min_value = float("inf")
            self.max_value = float("-inf")
        else:
            self.min_value = value
            self.max_value = value
        self.lazy = 0


class LazyMinMaxSegmentTree:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [SegmentNode() for _ in range(self.n * 4)]
        self._build(1, 0, self.n - 1, arr)

    def _build(self, idx: int, left: int, right: int, arr: list[int]):
        if left == right:
            self.tree[idx] = SegmentNode(arr[left])
            return

        mid = (left + right) // 2
        self._build(idx * 2, left, mid, arr)
        self._build(idx * 2 + 1, mid + 1, right, arr)
        self._pull(idx)

    def _pull(self, idx: int):
        left_node = self.tree[idx * 2]
        right_node = self.tree[idx * 2 + 1]

        self.tree[idx].min_value = min(left_node.min_value, right_node.min_value)
        self.tree[idx].max_value = max(left_node.max_value, right_node.max_value)

    def _push_lazy(self, idx: int, left: int, right: int):
        node = self.tree[idx]
        if node.lazy == 0:
            return

        node.min_value += node.lazy
        node.max_value += node.lazy

        if left < right:
            self.tree[idx * 2].lazy += node.lazy
            self.tree[idx * 2 + 1].lazy += node.lazy

        node.lazy = 0

    def range_add(self, ql: int, qr: int, idx: int, left: int, right: int, value: int):
        self._push_lazy(idx, left, right)

        if right < ql or left > qr:
            return

        if ql <= left and right <= qr:
            self.tree[idx].lazy += value
            self._push_lazy(idx, left, right)
            return

        mid = (left + right) // 2
        self.range_add(ql, qr, idx * 2, left, mid, value)
        self.range_add(ql, qr, idx * 2 + 1, mid + 1, right, value)
        self._pull(idx)

    def find_rightmost_zero_prefix(self, idx: int, left: int, right: int) -> int:
        self._push_lazy(idx, left, right)

        node = self.tree[idx]

        if node.min_value > 0 or node.max_value < 0:
            return -1

        if left == right:
            return left

        mid = (left + right) // 2

        right_result = self.find_rightmost_zero_prefix(idx * 2 + 1, mid + 1, right)
        if right_result != -1:
            return right_result

        return self.find_rightmost_zero_prefix(idx * 2, left, mid)

class Solution:
    def _bruteforce_longest_balanced(self, nums: list[int]) -> int:
        n = len(nums)
        best = 0

        for start in range(n):
            if start > n - best:
                break

            seen = set()
            diff = 0  # distinct_even - distinct_odd

            for end in range(start, n):
                x = nums[end]
                if x not in seen:
                    seen.add(x)
                    diff += -1 if x % 2 else 1

                if diff == 0:
                    best = max(best, end - start + 1)

        return best

    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)

        # Small input optimization
        if n <= 2000:
            return self._bruteforce_longest_balanced(nums)

        # Precompute next occurrences
        max_value = max(nums)
        last_occurrence = [n] * (max_value + 1)
        next_position = [n] * n

        for i in range(n - 1, -1, -1):
            value = nums[i]
            next_position[i] = last_occurrence[value]
            last_occurrence[value] = i

        # Build prefix difference array
        seen = set()
        prefix = []
        diff = 0

        for x in nums:
            if x not in seen:
                seen.add(x)
                diff += 1 if x % 2 else -1
            prefix.append(diff)

        seg_tree = LazyMinMaxSegmentTree(prefix)

        answer = seg_tree.find_rightmost_zero_prefix(1, 0, n - 1)
        answer = answer + 1 if answer != -1 else 0

        for i in range(n - 1):
            right_limit = next_position[i] - 1

            if i + 1 <= right_limit:
                adjustment = -1 if nums[i] % 2 else 1
                seg_tree.range_add(i + 1, right_limit, 1, 0, n - 1, adjustment)

            if i + answer + 1 < n:
                rightmost = seg_tree.find_rightmost_zero_prefix(1, 0, n - 1)
                if rightmost != -1:
                    answer = max(answer, rightmost - i)

        return answer
    

# solution is built on top of a segment tree with lazy propagation, transforming the distinct-even vs distinct-odd balance condition into a dynamic prefix-difference maintenance problem under range updates, it has been taken into account the following main principles of the approach:

# 1. a subarray is balanced if the difference between distinct even and distinct odd elements inside it is zero; this can be represented as a prefix-difference array, reducing the problem to finding equal prefix states
# 2. when shifting the left boundary of the subarray, only the first occurrence of that value affects the balance; therefore, its removal can be modeled as a range adjustment over future prefix positions until its next occurrence
# 3. range adjustments over the prefix array can be performed efficiently using a segment tree with lazy propagation, maintaining both minimum and maximum values to detect whether zero exists in a range
# 4. instead of checking every possible right boundary, the tree supports querying the rightmost index where the prefix-difference equals zero, ensuring maximal length selection at each stage

# [!] notice that the segment tree maintains both min and max in each node; this guarantees that zero exists in a segment iff min_value ≤ 0 ≤ max_value
# [!] the lazy propagation ensures that multiple overlapping left-boundary shifts remain amortized O(log n), avoiding recomputation of the full prefix array
# [!] a brute-force solution is used for small inputs to avoid unnecessary overhead, as the segment tree only becomes asymptotically advantageous for large n

# this leads to dynamically simulating all valid starting points while maintaining a globally updated prefix-difference structure, allowing efficient extraction of the longest balanced subarray


# time complexity: O(n log n) -> building prefix + next occurrences = O(n), each range update and query = O(log n), performed O(n) times
# space complexity: O(n) -> segment tree storage + auxiliary arrays
