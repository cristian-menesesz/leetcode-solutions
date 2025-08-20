# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


from math import gcd

def gcdOfStrings(str1: str, str2: str) -> str:
    
    max_length = gcd(len(str1), len(str2))

    if str1 + str2 != str2 + str1:
        return ""

    return str1[:max_length]

def main():
    print(gcdOfStrings("ABCABC", "ABC"))
    print(gcdOfStrings("ABABAB", "ABAB"))

if __name__ == "__main__":
    main()


# solution worked on top of the mathematical properties of string concatenation and the greatest common divisor (GCD), it has been taken into account three main principles of the problem:

# 1. for two strings to have a common divisor string, their concatenation order must be commutative, i.e., str1 + str2 must equal str2 + str1, otherwise no divisor string can exist
# 2. the largest divisor string that divides both str1 and str2 must have a length equal to the GCD of their lengths, since any common repeating substring must repeat in cycles compatible with both strings
# 3. extracting the prefix of str1 with length equal to gcd(len(str1), len(str2)) guarantees the maximal possible divisor string, as any longer prefix would exceed the valid repetition structure of one of the strings

# [!] notice that if the concatenation commutativity check fails, the solution can immediately return an empty string without further computation
# [!] the use of gcd(len(str1), len(str2)) ensures that the algorithm only needs one prefix extraction instead of testing multiple candidates


# time complexity: O(n) → dominated by string concatenation comparisons (n = len(str1) + len(str2))
# space complexity: O(1) → only constant extra memory is used outside the input strings
