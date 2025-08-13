# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?


def isPowerOfThree(n: int) -> bool:
    return n in {
        1, 3, 9, 27, 81, 243, 729, 2187, 6561,
        19683, 59049, 177147, 531441, 1594323,
        4782969, 14348907, 43046721, 129140163,
        387420489, 1162261467
    }

def main():
    print(isPowerOfThree(27))
    print(isPowerOfThree(0))

if __name__ == "__main__":
    main()


# solution works on top of precomputation advantages and set lookup efficiency, avoiding iterative or recursive processes
# it relies on the mathematical constraint that the maximum power of three fitting into a 32-bit signed integer is 3^19 = 1162261467

# 1. precompute all valid powers of three up to the maximum bound imposed by the integer constraint
# 2. store these values in a set to enable O(1) average time membership checks
# 3. return whether the given integer n exists in the set, ensuring immediate decision without further computation

# [!] the precomputation is static and independent from the input, meaning it does not grow with n and can be reused across multiple calls
# [!] the approach assumes the environment restricts n to the 32-bit signed integer range; for other ranges the precomputed set must be adjusted
# [!] this eliminates the need for loops, recursion, or floating-point calculations, making it safe for edge cases like n <= 0


# time complexity: O(1) -> constant-time membership check in a set
# space complexity: O(1) -> fixed-size set containing all valid powers of three within the constraint
