# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

 

# Example 1:

# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.


def countBinarySubstrings(self, s: str) -> int:
    
    total_substrings = 0
    previous_run_length = 0
    current_run_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_run_length += 1
        else:
            previous_run_length = current_run_length
            current_run_length = 1

        if current_run_length <= previous_run_length:
            total_substrings += 1

    return total_substrings


# solution worked on top of the greedy linear scan approach, it has been taken into account three main principles of the problem:

# 1. a valid binary substring with equal consecutive 0s and 1s is fully determined by two adjacent runs of different characters (e.g., "000111"), so the problem reduces to analyzing lengths of consecutive runs
# 2. for every transition between different characters, the number of valid substrings that can be formed is limited by the minimum length between the previous run and the current run
# 3. instead of storing all run lengths, it is sufficient to keep only the previous run length and the current run length, updating the result incrementally during a single left-to-right traversal

# [!] notice that the counting is performed greedily during traversal, avoiding any need for substring generation or post-processing
# [!] as only two scalar variables are required to represent the state between adjacent runs, the solution maintains constant space without auxiliary data structures

# this leads to the computation of the total valid binary substrings by accumulating, at each step, the number of balanced pairs allowed by the relationship between consecutive runs


# time complexity: O(n) -> single linear traversal of the string
# space complexity: O(1) -> constant extra space for run tracking