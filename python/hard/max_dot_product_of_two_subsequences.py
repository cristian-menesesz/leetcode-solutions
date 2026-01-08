# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

# Example 1:

# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
# Example 2:

# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
# Example 3:

# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 1000


def maxDotProduct(nums1: list[int], nums2: list[int]) -> int:

    if len(nums1) < len(nums2):
        return maxDotProduct(nums2, nums1)

    len1, len2 = len(nums1), len(nums2)
    NEG_INF = float('-inf')
    dp = [[NEG_INF] * (len2 + 1) for _ in range(2)]
    max_result = NEG_INF

    for i in range(len1 - 1, -1, -1):
        
        current_row = i & 1
        next_row = (i + 1) & 1

        for j in range(len2 - 1, -1, -1):
            
            product = nums1[i] * nums2[j]

            # Option 1: start a new subsequence with current pair
            best = product

            # Option 2: extend an existing subsequence
            if i + 1 < len1 and j + 1 < len2:
                best = max(best, product + dp[next_row][j + 1])

            # Option 3: skip element in nums2
            best = max(best, dp[current_row][j + 1])

            # Option 4: skip element in nums1
            dp[current_row][j] = max(best, dp[next_row][j])

            max_result = max(max_result, dp[current_row][j])

    return max_result


# solution worked on top of the dynamic programming with rolling memoization advantages, focusing on optimal subsequence alignment decisions.

# 1. the algorithm ensures nums1 is always the longer array, reducing the DP state space and simplifying transitions
# 2. each dp state represents the maximum dot product obtainable starting from indices (i, j), enforcing non-empty subsequences
# 3. at every state, the approach evaluates four strategic choices: start a new subsequence, extend an existing one, skip an element in nums2, or skip an element in nums1
# 4. iteration is performed bottom-up (from the end of both arrays) so all dependent states are already computed
# 5. rolling rows are used in the DP table, as each state depends only on the current and next row, enabling memory optimization

# [!] notice that initializing dp with negative infinity is critical to forbid empty subsequences from being considered valid solutions
# [!] notice that the “start new subsequence” option guarantees correctness even when all products are negative
# [!] the global maximum is tracked explicitly because the optimal subsequence may start at any (i, j), not necessarily (0, 0)

# this leads to the computation of the maximum dot product between any pair of non-empty subsequences by locally optimizing choices and globally preserving the best result across all states


# time complexity: O(n * m) -> full DP traversal of both arrays
# space complexity: O(m) -> rolling DP rows proportional to the smaller array
