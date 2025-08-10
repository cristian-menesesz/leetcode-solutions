# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false
 

# Constraints:

# 1 <= n <= 109


def reorderedPowerOf2(n: int) -> bool:

    def digit_freq(x: int) -> tuple:
        freq = [0] * 10
        while x > 0:
            freq[x % 10] += 1
            x //= 10
        return tuple(freq)

    if not hasattr(reorderedPowerOf2, "_signatures"):
        reorderedPowerOf2._signatures = {
            digit_freq(1 << i) for i in range(31)
        }

    return digit_freq(n) in reorderedPowerOf2._signatures

def main():
    print(reorderedPowerOf2(10))
    print(reorderedPowerOf2(1))

if __name__ == "__main__":
    main()


# solution based on digit frequency matching against precomputed powers of two, it has been taken into account three main principles of the problem:

# 1. digit frequencies uniquely identify the multiset of digits, allowing direct comparison for permutation checks without generating all permutations
# 2. the range of possible powers of two is limited to 2^0 through 2^30, enabling exhaustive precomputation in constant time
# 3. storing frequencies as immutable tuples allows efficient hashing and lookup in a set for quick membership testing

# [!] the precomputation is performed lazily and cached as a function attribute to optimize for multiple invocations without redundant calculations


# time complexity: O(1) -> precomputation over fixed 31 powers = O(1), frequency calculation = O(log n) but bounded by digit count
# space complexity: O(1) -> fixed-size set of tuples = O(1)
