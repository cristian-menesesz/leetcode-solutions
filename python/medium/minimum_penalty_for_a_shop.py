# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.

# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

 

# Example 1:

# Input: customers = "YYNY"
# Output: 2
# Explanation: 
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
# Example 2:

# Input: customers = "NNNNN"
# Output: 0
# Explanation: It is best to close the shop at the 0th hour as no customers arrive.
# Example 3:

# Input: customers = "YYYY"
# Output: 4
# Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
 

# Constraints:

# 1 <= customers.length <= 105
# customers consists only of characters 'Y' and 'N'.


def bestClosingTime(customers: str) -> int:
    
    penalty = customers.count('Y')
    min_penalty = penalty
    best_hour = 0

    for i, c in enumerate(customers):
        if c == 'Y':
            penalty -= 1
        else:
            penalty += 1

        if penalty < min_penalty:
            min_penalty = penalty
            best_hour = i + 1

    return best_hour


# solution worked on top of a greedy incremental cost optimization approach, where the total penalty is updated in-place while traversing the input once:

# 1. the initial penalty is computed assuming the shop is closed for the entire timeline, counting all future dissatisfied customers ('Y')
# 2. as the closing time advances hour by hour, the penalty is updated incrementally: encountering a 'Y' reduces the penalty (customer is now served), while encountering an 'N' increases it (unnecessary open hour)
# 3. at each step, the current penalty represents the total cost of closing at that exact hour, so the minimum can be tracked without recomputation
# 4. the optimal closing time is the first hour at which the minimum penalty is achieved, ensuring correctness under ties

# [!] the algorithm never recomputes penalties from scratch; all updates are local and derived from the previous state
# [!] the problem is reduced to a single linear pass by transforming future penalties into a running balance
# [!] the solution relies on the fact that penalties are additive and independent per hour

# this leads to maintaining a rolling penalty score, selecting the hour that minimizes customer dissatisfaction with a single traversal


# time complexity: O(n) -> single pass over customers
# space complexity: O(1) -> constant extra variables only