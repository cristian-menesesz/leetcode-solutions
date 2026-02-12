# You are given a string s consisting of lowercase English letters.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

 

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "zzabccy"

# Output: 4

# Explanation:

# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.


def longestBalanced(self, s: str) -> int:
    
    length = len(s)
    longest_length = 1

    for left in range(length):
        
        char_frequency = [0] * 26
        distinct_count = 0
        max_frequency = 0
        num_chars_with_max_frequency = 0

        for right in range(left, length):
            
            char_index = ord(s[right]) - ord('a')
            char_frequency[char_index] += 1
            current_frequency = char_frequency[char_index]

            if current_frequency == 1:
                distinct_count += 1

            if current_frequency > max_frequency:
                max_frequency = current_frequency
                num_chars_with_max_frequency = 1
            elif current_frequency == max_frequency:
                num_chars_with_max_frequency += 1

            if distinct_count == num_chars_with_max_frequency:
                longest_length = max(longest_length, right - left + 1)

    return longest_length


# Brute-Force Enumeration with Incremental Frequency Tracking (Optimized Counting Approach)

# 1. The solution enumerates every possible starting index and progressively expands the right boundary, transforming the problem into evaluating all substrings while avoiding recomputation of frequency data.
# 2. Instead of recomputing character frequencies from scratch for each substring, the approach incrementally updates a fixed-size frequency array (size 26), allowing constant-time updates per extension.
# 3. During expansion, the algorithm maintains three synchronized metrics:
# - distinct_count → number of distinct characters in the current substring.
# - max_frequency → highest frequency among all characters.
# - num_chars_with_max_frequency → number of characters that currently reach max_frequency.
# These metrics fully characterize the “balanced” condition without scanning the frequency array.
# 4. The substring satisfies the balanced property when: distinct_count == num_chars_with_max_frequency meaning all distinct characters appear the same number of times (each must have frequency = max_frequency).
# 5. By maintaining these invariants incrementally, the validity of each substring is checked in O(1), avoiding any secondary scans over the alphabet.

# [!] Notice that this is not a sliding window with shrinking behavior; it is a controlled quadratic expansion where each left index defines an independent frequency state.
# [!] The fixed alphabet size (26 lowercase letters) ensures constant auxiliary operations, preventing hidden linear factors inside the inner loop.

# This leads to a complete yet optimized enumeration of all substrings, where frequency statistics are updated incrementally and the balanced condition is validated in constant time.


# time complexity: O(n^2) -> nested substring expansion with O(1) frequency updates
# space complexity: O(1) -> fixed-size frequency array (26) and constant auxiliary variables
