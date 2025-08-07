# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.

 

# Example 1:

# Input: fruits = [4,2,5], baskets = [3,5,4]

# Output: 1

# Explanation:

# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

# Example 2:

# Input: fruits = [3,6,1], baskets = [6,4,7]

# Output: 0

# Explanation:

# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# Since all fruits are successfully placed, we return 0.



# Constraints:

# n == fruits.length == baskets.length
# 1 <= n <= 100
# 1 <= fruits[i], baskets[i] <= 1000


def numOfUnplacedFruits(fruits: list[int], baskets: list[int]) -> int:
        
    n = len(baskets)
    placed = 0

    for fruit in fruits:
        for i in range(n):
            if fruit <= baskets[i]:
                placed += 1
                baskets[i] = 0
                break

    return n - placed

def main():
    print(numOfUnplacedFruits([4,2,5], [3,5,4]))
    print(numOfUnplacedFruits([3,6,1], [6,4,7]))

if __name__ == "__main__":
    main()


# solution worked on top of a greedy placement strategy to minimize unplaced fruits, utilizing a simple iterative selection mechanism

# 1. for each fruit, the algorithm attempts to place it in the first available basket that can hold it (i.e., basket capacity ≥ fruit size)
# 2. once a basket holds a fruit, its capacity is set to 0 to prevent reuse, effectively marking it as unavailable
# 3. the number of successfully placed fruits is tracked, and the final result is computed by subtracting it from the total number of baskets

# [!] notice that the order of the baskets remains unchanged, and no sorting or optimization of fruit-basket matching is applied
# [!] the algorithm uses a nested loop to ensure each fruit finds the earliest possible fitting basket, ensuring correctness but not optimal time efficiency


# time complexity: O(m * n) -> m = number of fruits, n = number of baskets
# space complexity: O(1) -> in-place operations without additional memory allocation
