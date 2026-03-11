# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement.

 

# Example 1:

# Input: n = 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
# Example 2:

# Input: n = 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
# Example 3:

# Input: n = 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

# Constraints:

# 0 <= n < 109


def bitwiseComplement(self, n: int) -> int:
    
    if n == 0: return 1

    return ~n & (1 << n.bit_length()) - 1


# solution works on top of bitwise masking principles, it has been taken into account two main principles of the problem:

# 1. the complement of a number must only affect the bits that belong to the binary representation of n, therefore a mask of 1s with the same bit length of n is required
# 2. the bitwise NOT (~n) inverts all bits of the machine representation, so it must be restricted using the mask in order to remove the higher unwanted bits

# [!] notice that the mask is constructed by shifting 1 left by the bit length of n and subtracting 1, producing a sequence of 1s exactly covering the bits of n
# [!] notice that the case n == 0 must be handled separately, as its complement is defined as 1

# this leads to computing the unrestricted bitwise complement and applying a mask that preserves only the relevant bits of the number

# time complexity: O(1)
# space complexity: O(1)
