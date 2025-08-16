# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
 

# Constraints:

# 1 <= num <= 104
# num consists of only 6 and 9 digits.


def maximum69Number (num: int) -> int:
    return int(str(num).replace('6', '9', 1))

def main():
    print(maximum69Number(9669))
    print(maximum69Number(9999))

if __name__ == "__main__":
    main()


# solution worked on top of a greedy transformation approach, it has been taken into account three main principles of the problem:

# 1. since the goal is to maximize the number, the optimal move is to change the most significant '6' into '9'
# 2. once the first replacement is done, no further changes can improve the number more, so at most one replacement is required
# 3. if no '6' exists in the number, the number is already maximized, so no changes are needed

# [!] notice that it is never beneficial to change a '9' into a '6' since that would decrease the number
# [!] as the digits are restricted to only '6' and '9', the first encountered '6' guarantees the optimal choice when replaced


# time complexity: O(d) -> d = number of digits in num, string conversion and single replacement
# space complexity: O(d) -> string representation of the number is stored temporarily
