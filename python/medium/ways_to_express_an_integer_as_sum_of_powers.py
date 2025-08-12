# Given two positive integers n and x.

# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

# Since the result can be very large, return it modulo 109 + 7.

# For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

# Example 1:

# Input: n = 10, x = 2
# Output: 1
# Explanation: We can express n as the following: n = 32 + 12 = 10.
# It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
# Example 2:

# Input: n = 4, x = 1
# Output: 2
# Explanation: We can express n in the following ways:
# - n = 41 = 4.
# - n = 31 + 11 = 4.
 

# Constraints:

# 1 <= n <= 300
# 1 <= x <= 5


def numberOfWays(n: int, x: int) -> int:
    
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        val = i**x
        if val > n:
            break
        for j in range(n, val - 1, -1):
            dp[j] = (dp[j] + dp[j - val]) % MOD

    return dp[n]

def main():
    print(numberOfWays(10, 2))
    print(numberOfWays(4, 1))

if __name__ == "__main__":
    main()


# solution worked on top of the dynamic programming memoization advantages for subset sum–style problems, leveraging iterative state updates to count valid combinations without recomputation

# 1. each number from 1 to n is raised to the power x, forming the set of candidate values to be used in combinations
# 2. the dp array stores, for every sum from 0 to n, the number of ways it can be formed using the candidates considered so far
# 3. iteration proceeds in reverse over the sums to ensure that each candidate is used at most once in each combination

# [!] only powers i**x ≤ n are considered, as larger values cannot contribute to any valid sum
# [!] reverse iteration on dp is crucial to avoid overcounting combinations where the same candidate is reused in the same step

# by iteratively updating dp with valid candidates, the final result is dp[n], representing the total count of unique combinations that sum exactly to n


# time complexity: O(n * m) -> m = number of valid powers ≤ n
# space complexity: O(n) -> dp memoization array of size n+1
