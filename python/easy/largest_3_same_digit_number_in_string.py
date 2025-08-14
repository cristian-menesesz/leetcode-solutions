# # You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# # It is a substring of num with length 3.
# # It consists of only one unique digit.
# # Return the maximum good integer as a string or an empty string "" if no such integer exists.

# # Note:

# # A substring is a contiguous sequence of characters within a string.
# # There may be leading zeroes in num or a good integer.
 

# # Example 1:

# # Input: num = "6777133339"
# # Output: "777"
# # Explanation: There are two distinct good integers: "777" and "333".
# # "777" is the largest, so we return "777".
# # Example 2:

# # Input: num = "2300019"
# # Output: "000"
# # Explanation: "000" is the only good integer.
# # Example 3:

# # Input: num = "42352338"
# # Output: ""
# # Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
 

# # Constraints:

# # 3 <= num.length <= 1000
# # num only consists of digits.


def largestGoodInteger(num: str) -> str:

    count = 1
    ans = -1
    
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            count += 1
            if count == 3:
                ans = max(ans, int(num[i]))
        else:
            count = 1

    return str(ans) * 3 if ans != -1 else ""

def main():
    print(largestGoodInteger("6777133339"))
    print(largestGoodInteger("42352338"))

if __name__ == "__main__":
    main()


# solution worked on top of sequential scanning and local state tracking advantages, it has been taken into account three main principles of the problem:

# 1. iterate through the string while keeping a counter of consecutive identical digits to identify possible "good integers" in a single pass
# 2. whenever a streak of three identical digits is found, update the maximum candidate by comparing its numeric value with the best found so far
# 3. reset the streak counter whenever the digit sequence is interrupted, ensuring only contiguous segments are evaluated

# [!] as soon as a sequence reaches length three, its value is considered without extending the count further, since only substrings of length exactly three matter
# [!] numeric comparison is used rather than string comparison to ensure correct ordering when dealing with digits, even with leading zeroes


# time complexity: O(n) → single pass over the string
# space complexity: O(1) → only a few integer variables are stored
