# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

# Example 1:

# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
# Example 2:

# Input: n = 8
# Output: 0
# Explanation: 8 in binary is "1000".
# There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.
# Example 3:

# Input: n = 5
# Output: 2
# Explanation: 5 in binary is "101".
 

# Constraints:

# 1 <= n <= 109


def binaryGap(self, n: int) -> int:
    
    # Remove trailing zeros so the first bit is 1
    n //= n & -n

    if n == 1:
        return 0

    longest_distance = 0
    zeros_since_last_one = 0

    while n:
        if n & 1:  # Found a '1' bit
            longest_distance = max(longest_distance, zeros_since_last_one)
            zeros_since_last_one = 0
        else:  # Counting zeros between 1s
            zeros_since_last_one += 1

        n >>= 1

    # Distance = zeros between + 1
    return longest_distance + 1


# solution worked on top of bit manipulation and sequential state tracking, exploiting binary representation properties to compute distances between set bits efficiently. it has been taken into account three main principles of the problem:

# 1. trailing zeros are removed using n & -n so the iteration starts at the first significant '1', avoiding invalid initial gaps and reducing unnecessary computation.
# 2. the algorithm scans the binary representation from least significant bit to most significant bit, maintaining a running count of zeros since the last encountered '1'.
# 3. whenever a new '1' bit is found, the distance between consecutive set bits is computed implicitly by updating the maximum gap using the accumulated zero counter.

# [!] notice that the algorithm does not explicitly store bit positions; instead, distance is derived through incremental counting, achieving constant memory usage.
# [!] as the traversal is performed through bit shifting, each iteration strictly reduces the problem size by one bit, guaranteeing linear progress over the bit-length of the number.

# this leads to the computation of the maximum binary gap by iteratively evaluating transitions between consecutive set bits within the integer representation.


# time complexity: O(log n) -> one pass over the binary length of n
# space complexity: O(1) -> constant auxiliary variables only
