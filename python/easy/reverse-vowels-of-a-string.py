# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


def reverseVowels(s: str) -> str:
    
    s = list(s)
    n = len(s)
    vowels = set("aeiouAEIOU")
    
    for i in range(n):
        print(n)
        if s[i] in vowels:
            for j in range(n - 1, i, -1):
                n -= 1
                if s[j] in vowels:
                    s[i], s[j] = s[j], s[i]
                    break
    
    return ''.join(s)

def main():
    print(reverseVowels("hello"))
    print(reverseVowels("leetcode"))

if __name__ == "__main__":
    main()


# solution worked on top of the two-pointer scanning technique, optimized to reverse only vowel positions in the string:

# 1. two indices are maintained, one starting from the beginning and the other from the end, both moving toward the center
# 2. the left index advances until it finds a vowel, while the right index decreases until it finds another vowel
# 3. when both indices point to vowels, they are swapped, ensuring that vowels are reversed while consonants remain untouched

# [!] notice that by restricting movement only when vowels are found, unnecessary iterations are avoided, improving efficiency
# [!] as both indices move strictly inward, each vowel is visited at most once, preventing redundant swaps


# time complexity: O(n) -> single pass through the string with at most n character checks
# space complexity: O(1) -> in-place swap with no auxiliary data structures
