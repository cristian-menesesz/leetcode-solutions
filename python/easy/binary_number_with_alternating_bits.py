# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

# Example 1:

# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:

# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:

# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
 

# Constraints:

# 1 <= n <= 231 - 1


def hasAlternatingBits(self, n: int) -> bool:
    
    x = n ^ (n >> 1)
    
    return (x & (x + 1)) == 0


# solution worked on top of the dynamic programming memoization advantages, it has been taken into account three main principles of the problem:

# 1. the top left child only moves through the diagonal, as he cannot reach [n-1, n-1] in n-1 moves if he doesn't
# 2. with the top right child, he can only move in the upper triangle section of the grid until the diagonal, in case it passes the diagonal he wouldn't make it to [n-1, n-1] in n-1 moves
# 3. as the top right child and the bottom left child are symmetrical in their section of movement and in their possible movements, it can be computed the transpsose of the grid and reuse the same dp

# [!] notice thet for both upper and lower triangles sections it will be never taken into account a movement through the diagonal as the top left child is going to pass through it
# [!] as the problem is divided into independent sections it is possible to use two different dps, one for each section, in case the sections share dependency this is not possible

# this leads to the computation of the fruits collected in the diagonal, and both triangle sections (dp)


# time complexity: O(n^2) -> dp triangle section = O(n^2)
# space complexity: O(n) -> dp memoization = O(n).