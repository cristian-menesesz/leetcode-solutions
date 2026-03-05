# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

 

# Example 1:

# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:

# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:

# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
 

# Constraints:

# 1 <= s.length <= 104
# s[i] is either '0' or '1'.


def minOperations(self, s: str) -> int:
    
    mismatches_starting_with_zero = 0
    length = len(s)

    for index in range(length):
        # Count mismatches with pattern "010101..."
        mismatches_starting_with_zero += (ord(s[index]) ^ index) & 1

    # Alternative pattern "101010..."
    mismatches_starting_with_one = length - mismatches_starting_with_zero

    return min(mismatches_starting_with_zero, mismatches_starting_with_one)


# solution worked on top of a parity-based pattern comparison approach, it leverages the binary representation of characters and index parity to evaluate mismatches against an alternating binary pattern in a single pass

# 1. the expected value of each position in the pattern "010101..." can be determined directly from the parity of the index (even -> '0', odd -> '1')
# 2. by XORing the ASCII code of the current character with the index and masking the least significant bit, it is possible to detect whether the character matches the expected alternating value
# 3. counting mismatches against the pattern "010101..." automatically determines the mismatches for the complementary pattern "101010..." since both patterns are perfect inverses of each other

# [!] the XOR operation combined with a bitmask allows the comparison to be reduced to a constant-time bitwise operation without constructing the expected pattern
# [!] since both valid alternating patterns are complements, computing one mismatch count is sufficient to derive the other

# this leads to a single linear traversal of the string that counts mismatches with one alternating pattern and derives the other through complementarity, returning the minimal number of flips required


# time complexity: O(n) -> single pass through the string
# space complexity: O(1) -> constant auxiliary memory
