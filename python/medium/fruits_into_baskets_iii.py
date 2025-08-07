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
# 1 <= n <= 105
# 1 <= fruits[i], baskets[i] <= 109


def numOfUnplacedFruits(fruits: list[int], baskets: list[int]) -> int:
    
    n = len(baskets)
    ans = 0
    
    power = 1
    while power < n:
        power *= 2
        
    segmented_tree = [0] * (power * 2)

    for i in range(n):
        segmented_tree[power + i] = baskets[i]
    
    for i in range(power - 1, 0, -1):
        segmented_tree[i] = max(segmented_tree[2 * i], segmented_tree[2 * i + 1])
    
    for fruit in fruits:
        if segmented_tree[1] < fruit:
            ans += 1
            continue
        
        i = 1
        while i < power:
            i *= 2
            if segmented_tree[i] < fruit:
                i += 1
        
        segmented_tree[i] = 0
        i //= 2
        while i > 0:
            segmented_tree[i] = max(segmented_tree[2 * i], segmented_tree[2 * i + 1])
            i //= 2
    
    return ans

def main():
    print(numOfUnplacedFruits([4,2,5], [3,5,4]))
    print(numOfUnplacedFruits([3,6,1], [6,4,7]))

if __name__ == "__main__":
    main()


# solution worked on top of a segment tree optimization to enable efficient greedy placement, leveraging range queries to identify the earliest valid basket for each fruit

# 1. a segment tree is constructed over the initial basket capacities to allow fast range maximum queries, enabling fruit-to-basket matching in logarithmic time
# 2. for each fruit, if the global maximum capacity is smaller than the fruit's requirement, the fruit is marked as unplaceable
# 3. otherwise, the segment tree is traversed top-down to locate the leftmost basket that satisfies the fruit's requirement, following the segment structure and updating the basket's value to 0 (indicating used), with upward propagation to maintain correct max values

# [!] notice that this tree-based structure transforms the brute-force O(n²) nested iteration into an O(n log n) efficient mechanism by preserving range max queries
# [!] the baskets are matched from left to right, as required, due to the structure of the segment tree traversal (always exploring left child first when possible)


# time complexity: O(n log n) -> build tree: O(n), n queries/updates: O(log n) each
# space complexity: O(n) -> segment tree requires approximately 2 * n space
