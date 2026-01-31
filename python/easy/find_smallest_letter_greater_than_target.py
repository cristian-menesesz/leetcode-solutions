# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
# Example 3:

# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 

# Constraints:

# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.


from bisect import bisect_right

def nextGreatestLetter(self, letters: list[str], target: str) -> str:
    return letters[i] if (i:=bisect_right(letters, target))<len(letters) else letters[0]


# solution is based on binary search over a sorted domain, exploiting order and wrap-around behavior

# 1. the letters array is treated as a cyclically ordered sequence, meaning that exceeding its bounds naturally maps back to the first valid candidate
# 2. the search is reduced to finding the first element strictly greater than the target, which allows the use of an upper-bound binary search strategy
# 3. index validation is used as a decision point: if the computed position exceeds the array length, the solution resolves by wrapping to the initial element

# [!] the algorithm does not scan or compare elements linearly; ordering is assumed and leveraged
# [!] the wrap-around case is not handled as a special branch but as a consequence of index bounds checking

# this leads to a constant-time resolution after a logarithmic search, directly selecting the next valid character or wrapping to the start when no greater element exists


# time complexity: O(log n) -> single binary search
# space complexity: O(1) -> no additional data structures used
