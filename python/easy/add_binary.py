# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


def addBinary(self, a: str, b: str) -> str:
    return bin(int(a,2)+int(b,2))[2:]


# solution worked on top of the built-in big integer arithmetic and base conversion utilities, it has been taken into account three main principles of the problem:

# 1. both binary strings can be interpreted as integers by explicitly specifying base 2, delegating the positional value computation to the language runtime
# 2. once converted to integers, the binary sum reduces to a single arithmetic addition, leveraging arbitrary-precision integer support to handle carries implicitly
# 3. the resulting integer can be transformed back into its binary string representation, and the prefix added by the conversion utility is removed to match the expected format

# [!] notice that this approach avoids manual bit-by-bit simulation and carry propagation, since all low-level binary operations are abstracted by the language
# [!] correctness relies on the language supporting arbitrary-precision integers; in environments with fixed-width integers, overflow could occur

# this leads to a direct transformation pipeline: binary string -> integer -> integer addition -> binary string


# time complexity: O(n) -> conversion of both strings and output generation = O(n)
# space complexity: O(n) -> storage of intermediate integer representation and result string = O(n)
