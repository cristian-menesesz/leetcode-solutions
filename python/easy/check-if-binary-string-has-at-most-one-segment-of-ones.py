# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

# Example 1:

# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
# Example 2:

# Input: s = "110"
# Output: true
 

# Constraints:

# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.


def checkOnesSegment(self, s: str) -> bool:
    # a second '1' segment implies the pattern "01"
    return "01" not in s


# solution worked on top of the pattern detection advantages of string searching, it has been taken into account one main principle of the problem:

# 1. if the binary string contains more than one segment of '1's, there must exist a transition from '0' to '1' after the first segment, which necessarily forms the substring "01"

# [!] the existence of the substring "01" indicates that after a block of '1's a new block of '1's starts again, meaning there are at least two segments of '1's
# [!] if the substring "01" does not appear in the string, then all '1's must appear in a single contiguous segment

# this leads to verifying whether the substring "01" exists in the string, where its absence guarantees that there is only one segment of '1's


# time complexity: O(n) -> substring search over the string
# space complexity: O(1) -> constant auxiliary space
