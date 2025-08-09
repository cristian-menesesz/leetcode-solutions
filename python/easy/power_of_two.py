# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

def main():
    print(isPowerOfTwo(1))
    print(isPowerOfTwo(3))

if __name__ == "__main__":
    main()


# solution worked on top of the bit manipulation advantages, it has been taken into account two main principles of the problem:

# 1. a number that is a power of two has exactly one bit set in its binary representation, and all other bits are zero
# 2. subtracting 1 from such a number flips that single 1 bit to 0 and turns all less significant bits into 1, ensuring that the bitwise AND between the number and its predecessor will always be zero

# [!] this approach avoids loops and recursion entirely, relying purely on constant-time bitwise operations
# [!] the method handles negative and zero values early, as they cannot be powers of two

# this leads to the computation of a single bitwise check (n & (n - 1)) == 0 after validating that n is positive, determining the result in O(1) time

# time complexity: O(1) -> single bitwise check
# space complexity: O(1) -> constant memory usage
