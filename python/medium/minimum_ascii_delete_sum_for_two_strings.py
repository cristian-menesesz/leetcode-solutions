# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

# Example 1:

# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:

# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

# Constraints:

# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.


def minimumDeleteSum(self, s1: str, s2: str) -> int:

    if len(s1) < len(s2):
        return self.minimumDeleteSum(s2, s1)

    len_a, len_b = len(s1), len(s2)
    lcs_ascii_dp = [[0] * (len_b + 1) for _ in range(2)]

    for i in range(len_a):
        
        curr_row = (i + 1) & 1
        prev_row = curr_row ^ 1

        for j in range(len_b):
            if s1[i] == s2[j]:
                lcs_ascii_dp[curr_row][j + 1] = (
                    ord(s1[i]) + lcs_ascii_dp[prev_row][j]
                )
            else:
                lcs_ascii_dp[curr_row][j + 1] = max(
                    lcs_ascii_dp[prev_row][j + 1],
                    lcs_ascii_dp[curr_row][j]
                )

    total_ascii_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
    max_common_ascii_sum = lcs_ascii_dp[len_a & 1][len_b]

    return total_ascii_sum - 2 * max_common_ascii_sum


# solution worked on top of a dynamic programming optimization of the classic LCS (Longest Common Subsequence) problem, adapted to maximize ASCII value instead of length, while minimizing space usage through row compression, it has been taken into account four main principles of the approach:

# 1. the problem can be reduced to finding a common subsequence between both strings whose total ASCII value is maximal, since deleting all other characters minimizes the total deletion cost.
# 2. instead of computing a standard LCS by length, the DP state accumulates ASCII sums, transforming the objective from “longest” to “most valuable” common subsequence.
# 3. as each DP state dp[i][j] depends only on dp[i-1][j], dp[i][j-1], and dp[i-1][j-1], it is sufficient to keep only two rows in memory, enabling space optimization through rolling arrays.
# 4. by enforcing that the first string is always the longer one, the DP table width is minimized, ensuring the rolling-array optimization yields O(n) auxiliary space.

# [!] notice that the DP transition preserves optimal substructure: at every character comparison, the solution locally decides whether to extend a common subsequence or propagate the best previous result.
# [!] notice that the ASCII accumulation guarantees correctness because deletions are symmetric on both strings, and any common character kept contributes twice its ASCII value to the total sum saved.

# this leads to the computation of the maximum ASCII sum of a common subsequence, which is then subtracted (twice) from the total ASCII sum of both strings to obtain the minimum delete sum.


# time complexity: O(n * m) -> full DP traversal over both strings
# space complexity: O(m) -> rolling DP rows, where m = length of the shorter string
