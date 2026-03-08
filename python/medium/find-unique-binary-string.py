# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

# Constraints:

# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.


def findDifferentBinaryString(self, binary_strings: List[str]) -> str:
    
    # Build a string that differs from each input string at position i
    length = len(binary_strings[0])
    result_bits = ['0'] * length

    for index, binary_string in enumerate(binary_strings):
        # Flip the diagonal bit
        result_bits[index] = '1' if binary_string[index] == '0' else '0'

    return "".join(result_bits)


# solution worked on top of the diagonalization principle, constructing a binary string that is guaranteed to differ from every input string in at least one position

# 1. each binary string can be uniquely identified by at least one index position
# 2. by iterating through the list and inspecting the i-th bit of the i-th string, we obtain a position that characterizes that specific string
# 3. flipping that bit guarantees that the constructed string differs from that string at that position
# 4. repeating this process for every index constructs a string that differs from every string in the list at least in its diagonal position

# [!] the constructed string is guaranteed not to appear in the list because it differs from the i-th string exactly at position i
# [!] this works because the number of strings equals the length of each string, allowing a full diagonal traversal across all strings

# this leads to constructing a new binary string by flipping the diagonal bits of the
# matrix formed by the input strings


# time complexity: O(n) -> single traversal of n strings
# space complexity: O(n) -> storage of the resulting binary string
