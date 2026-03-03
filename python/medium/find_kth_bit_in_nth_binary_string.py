# Given two positive integers n and k, the binary string Sn is formed as follows:

# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first four strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

# Example 1:

# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1st bit is "0".
# Example 2:

# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11th bit is "1".
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= 2n - 1


def findKthBit(self, n: int, k: int) -> str:
    """
    Returns the k-th bit of S_n without constructing the string.

    Uses symmetry:
    - Middle element is always '1'
    - Right side is inverted mirror of the left side
    """

    # Base case: S1 = "0"
    if k == 1:
        return '0'

    bit_size = k.bit_length()

    # Mirror position across the nearest power-of-two boundary
    mirrored_index = (1 << bit_size) - k

    # If k is exactly the symmetry center
    if mirrored_index == k:
        return '1'

    # Recursive lookup + inversion
    mirrored_bit = self.findKthBit(n, mirrored_index)

    return '0' if mirrored_bit == '1' else '1'


# solution works on top of a recursive symmetry reduction approach, exploiting structural properties of the implicitly defined binary string

# 1. the constructed sequence S_n follows a self-similar structure where the right half is the inverted mirror of the left half, allowing any position to be mapped into an equivalent smaller subproblem
# 2. instead of constructing S_n explicitly, the algorithm reflects the queried index k across the nearest power-of-two boundary, reducing the problem size while preserving positional meaning
# 3. whenever the queried position corresponds to the symmetry center (middle element), the value is deterministically '1', acting as a termination condition independent of recursion depth
# 4. recursive calls progressively move the query toward the base case (k = 1), while tracking parity through inversion caused by mirror transitions

# [!] the parameter n is not required for computation because the position alone determines the recursive reduction through structural symmetry
# [!] no string construction or simulation is performed; the algorithm operates purely on index transformations

# this leads to computing the k-th bit by repeatedly reflecting the index into smaller symmetric subproblems and applying inversion rules until reaching the base configuration


# time complexity: O(log k) -> recursive reductions halve the problem scale
# space complexity: O(log k) -> recursion stack depth
