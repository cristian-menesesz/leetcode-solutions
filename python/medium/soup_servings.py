# You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:

# pour 100 mL from type A and 0 mL from type B
# pour 75 mL from type A and 25 mL from type B
# pour 50 mL from type A and 50 mL from type B
# pour 25 mL from type A and 75 mL from type B
# Note:

# There is no operation that pours 0 mL from A and 100 mL from B.
# The amounts from A and B are poured simultaneously during the turn.
# If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
# The process stops immediately after any turn in which one of the soups is used up.

# Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: n = 50
# Output: 0.62500
# Explanation: 
# If we perform either of the first two serving operations, soup A will become empty first.
# If we perform the third operation, A and B will become empty at the same time.
# If we perform the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
# Example 2:

# Input: n = 100
# Output: 0.71875
# Explanation: 
# If we perform the first serving operation, soup A will become empty first.
# If we perform the second serving operations, A will become empty on performing operation [1, 2, 3], and both A and B become empty on performing operation 4.
# If we perform the third operation, A will become empty on performing operation [1, 2], and both A and B become empty on performing operation 3.
# If we perform the fourth operation, A will become empty on performing operation 1, and both A and B become empty on performing operation 2.
# So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.71875.
 

# Constraints:

# 0 <= n <= 109


import collections
from math import ceil


def soupServings(n: int) -> float:
    
    m = ceil(n / 25)
    dp = collections.defaultdict(dict)

    def calculate_dp(i: int, j: int) -> float:
        if i <= 0 and j <= 0:
            return 0.5
        if i <= 0:
            return 1.0
        if j <= 0:
            return 0.0
        if i in dp and j in dp[i]:
            return dp[i][j]

        dp[i][j] = (
            calculate_dp(i - 4, j)
            + calculate_dp(i - 3, j - 1)
            + calculate_dp(i - 2, j - 2)
            + calculate_dp(i - 1, j - 3)
        ) / 4.0

        return dp[i][j]

    for k in range(1, m + 1):
        if calculate_dp(k, k) > 1 - 1e-5:
            return 1.0
        
    return calculate_dp(m, m)

def main():
    print(soupServings(50))
    print(soupServings(100))

if __name__ == "__main__":
    main()


# solution worked on top of the dynamic programming memoization advantages, it has been taken into account three main principles of the problem:

# 1. the pourings are probabilistic and symmetric, so we can model the expected outcomes with recursive states defined by remaining A and B values
# 2. the problem allows the assumption that when n becomes large, the probability of A finishing first converges to 1, so we can optimize by bounding the state space
# 3. because pour amounts are always multiples of 25, the problem can be scaled down to a granularity of 25 mL units, reducing the DP state space significantly

# [!] notice that when n > 4800, the answer converges fast enough to 1 with tolerance 1e-5, allowing an early return and avoiding deep recursion
# [!] the 4 recursive branches represent the 4 equiprobable operations; each reduces the state space in a fixed way, allowing for straightforward memoization
# [!] the recursion stops at the base cases: A empty first → 1.0, B empty first → 0.0, both empty together → 0.5


# time complexity: O(1) → dp memoization explores at most (n/25)^2 states, the computation of the algorithm is only made when n < 4800 which can be seem as constant
# space complexity: O(1) → dp memoization stores at most (n/25)^2 states, n < 4800
