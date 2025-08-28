# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?


def reverseWords(s: str) -> str:
    
    words = s.split()
    res = []

    for i in range(len(words) - 1, -1, -1):
        res.append(words[i])
        if i != 0:
            res.append(" ")

    return "".join(res)

def main():
    print(reverseWords("the sky is blue"))
    print(reverseWords("  hello world  "))

if __name__ == "__main__":
    main()


# solution worked on top of the string manipulation advantages, it has been taken into account three main principles of the problem:

# 1. the string can be normalized into words by splitting with default whitespace handling, which automatically removes leading, trailing, and multiple spaces
# 2. the reversed order of words can be achieved by iterating from the last index to the first index, ensuring the correct placement of words
# 3. words are concatenated back into a single string, using manual insertion of spaces to guarantee a single space separator between words

# [!] notice that splitting with default whitespace automatically handles extra spaces, which prevents the need for manual trimming or filtering
# [!] as the algorithm uses string splitting and list traversal, the operations are linear and do not require additional complex data structures


# time complexity: O(n) -> traversal and reconstruction are linear with respect to string length
# space complexity: O(n) -> auxiliary list of words and result construction
