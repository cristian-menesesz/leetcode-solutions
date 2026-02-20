# Special binary strings are binary strings with the following two properties:

# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.

# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

# Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

 

# Example 1:

# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.
# Example 2:

# Input: s = "10"
# Output: "10"
 

# Constraints:

# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.


def makeLargestSpecial(self, s: str) -> str:
    """
    Recursively decomposes the special binary string into
    top-level special substrings, optimizes each one,
    then sorts them in descending lexicographic order.
    """

    # Base case: smallest possible special string
    if len(s) <= 2:
        return s

    special_blocks = []
    balance = 0
    block_start = 0

    # Split into top-level special substrings
    for i, char in enumerate(s):
        
        balance += 1 if char == '1' else -1

        # When balance returns to zero, we found a complete special substring
        if balance == 0:
            
            # Recursively optimize inner substring
            inner = s[block_start + 1 : i]
            optimized_inner = self.makeLargestSpecial(inner)

            special_blocks.append("1" + optimized_inner + "0")
            block_start = i + 1

    special_blocks.sort(reverse=True)

    return "".join(special_blocks)
    

# solution works under a recursive greedy decomposition approach over a hierarchical balanced structure

# 1. the string is interpreted as a hierarchy of top-level special substrings (identified by balance counting), allowing a structural decomposition similar to parsing well-formed parentheses
# 2. each time the balance returns to zero, a maximal top-level special block is isolated, guaranteeing independence between blocks at the same depth level
# 3. for each isolated block, the inner substring (excluding the outer '1' and '0')  is recursively optimized, ensuring optimality propagates bottom-up through the recursive structure
# 4. once all top-level blocks are recursively optimized, they are sorted in descending lexicographic order, applying a greedy ordering strategy that maximizes the global lexicographic result

# [!] notice that independence between top-level blocks allows reordering without breaking the special property, since each block is balanced and structurally closed
# [!] the recursion guarantees local optimality at each nested level before global reordering occurs, making the solution hierarchical rather than flat greedy

# this leads to decomposing the string into structurally independent balanced components, recursively optimizing each component, and greedily ordering them to construct the lexicographically largest valid special binary string


# time complexity: O(n^2) -> recursive decomposition and repeated sorting of substrings
# space complexity: O(n) -> recursion stack and substring storage
