# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

 

# Example 1:

# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:

# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.


def minimumDeletions(self, s: str) -> int:
        
    min_deletions = 0
    b_before_a = 0

    for character in s:
        if character == 'b':
            b_before_a += 1
        elif b_before_a > 0:
            min_deletions += 1
            b_before_a -= 1

    return min_deletions


# solution worked on top of a greedy invariant-based approach, where local optimal decisions are taken while maintaining a global consistency condition across the iteration:

# 1. the algorithm maintains the invariant that all kept 'b' characters must appear after all kept 'a' characters
# 2. the counter b_before_a represents the number of conflicting 'b's that would violate the invariant if an 'a' is kept
# 3. when an 'a' is encountered after one or more 'b's, the algorithm resolves the conflict by deleting the minimal-cost option (either the current 'a' or one of the previous 'b's), which is achieved greedily by removing a prior 'b'
# 4. each deletion immediately restores the invariant, allowing the algorithm to proceed without backtracking

# [!] the algorithm never revisits past decisions; once a character is processed, its contribution is permanently resolved
# [!] the invariant guarantees that all remaining characters form a valid configuration at every step

# this leads to a single left-to-right pass where conflicts are resolved optimally as they appear, yielding the minimum number of deletions required to enforce the ordering constraint

# time complexity: O(n) -> single linear scan of the string
# space complexity: O(1) -> constant auxiliary state
