# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1


def isPowerOfFour(n: int) -> bool:
    return (n & (n - 1)) == 0 and n % 3 == 1

def main():
    print(isPowerOfFour(16))
    print(isPowerOfFour(5))

if __name__ == "__main__":
    main()


# solution worked on top of the bit manipulation and modular arithmetic advantages, it has been taken into account two main principles of the problem:

# 1. a power of four is also a power of two, meaning its binary representation contains exactly one set bit; this can be checked with the condition (n & (n - 1)) == 0
# 2. powers of four have a specific property when divided by 3: they leave a remainder of 1; this allows distinguishing them from other powers of two (like powers of two that are not powers of four)

# [!] the check (n & (n - 1)) == 0 ensures n is a power of two, but does not confirm it's a power of four; the modulo 3 check filters the correct subset
# [!] negative numbers, zero, and non-power-of-two numbers are automatically filtered by the first condition, making the approach robust

# time complexity: O(1) -> both bitwise and modulo operations are constant time
# space complexity: O(1) -> no additional memory is used apart from a few variables
