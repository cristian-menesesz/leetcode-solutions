# You are given an array happiness of length n, and a positive integer k.

# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

 

# Example 1:

# Input: happiness = [1,2,3], k = 2
# Output: 4
# Explanation: We can pick 2 children in the following way:
# - Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
# - Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
# The sum of the happiness values of the selected children is 3 + 1 = 4.
# Example 2:

# Input: happiness = [1,1,1,1], k = 2
# Output: 1
# Explanation: We can pick 2 children in the following way:
# - Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
# - Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
# The sum of the happiness values of the selected children is 1 + 0 = 1.
# Example 3:

# Input: happiness = [2,3,4,5], k = 1
# Output: 5
# Explanation: We can pick 1 child in the following way:
# - Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
# The sum of the happiness values of the selected children is 5.
 

# Constraints:

# 1 <= n == happiness.length <= 2 * 105
# 1 <= happiness[i] <= 108
# 1 <= k <= n


def maximumHappinessSum(happiness: list[int], k: int) -> int:

    happiness.sort(reverse=True)
    happiness_sum = 0
    decrement = 0

    for i in range(k):
        current_happiness = max(happiness[i] - decrement, 0)
        happiness_sum += current_happiness
        decrement += 1

    return happiness_sum

def main():
    print(maximumHappinessSum(happiness = [1,2,3], k = 2))
    print(maximumHappinessSum(happiness = [1,1,1,1], k = 2))

if __name__ == "__main__":
    main()


# solution worked on top of a greedy optimization approach, exploiting ordering and monotonic decay of contribution to maximize the accumulated value:

# 1. the array is sorted in descending order so that the elements with the highest initial contribution are considered first
# 2. a cumulative decrement is applied progressively, modeling the diminishing return imposed by the selection order
# 3. at each step, the effective contribution is clamped to zero to avoid negative impact on the total sum
# 4. only the first k elements are considered, as any element beyond this point cannot increase the result under the decrement rule

# [!] the decrement grows deterministically with each selection, so there is no need for backtracking or state comparison
# [!] once an element’s adjusted value reaches zero, further decrements would never improve the result, but iteration is bounded by k
# [!] no overlapping subproblems or state reuse exist, therefore dynamic programming is unnecessary

# this leads to a linear accumulation over the top k sorted elements, each adjusted by its selection order, directly constructing the maximum achievable happiness sum


# time complexity: O(n log n) -> sorting dominates, loop is O(k)
# space complexity: O(1) -> constant extra space (in-place sort aside)