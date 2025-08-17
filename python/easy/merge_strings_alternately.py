# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


def mergeAlternately(word1: str, word2: str) -> str:
    
    result = []
    min_len = min(len(word1), len(word2))
    
    for i in range(min_len):
        result.append(word1[i])
        result.append(word2[i])
    
    if len(word1) > min_len:
        result.append(word1[min_len:])
    elif len(word2) > min_len:
        result.append(word2[min_len:])
    
    return ''.join(result)

def main():
    print(mergeAlternately("abc", "pqr"))
    print(mergeAlternately("ab", "pqrs"))

if __name__ == "__main__":
    main()


# solution worked on top of a direct iterative construction of the merged string, 
# it has been taken into account three main principles of the problem:

# 1. both strings contribute characters alternately, therefore iteration is only needed up to the length of the shorter string
# 2. at each iteration step, the character from word1 is appended first, immediately followed by the character from word2
# 3. once the shorter string is exhausted, the remaining substring of the longer word can be directly appended without further alternation

# [!] notice that this approach does not require any precomputation of the final size of the merged string, as characters are appended incrementally
# [!] the construction is performed in a list buffer to avoid costly string concatenations, which are inefficient in Python, and only joined into a final string at the end


# time complexity: O(n) -> iteration and concatenation of at most n = len(word1) + len(word2) characters
# space complexity: O(n) -> storage of the merged characters in the result buffer
