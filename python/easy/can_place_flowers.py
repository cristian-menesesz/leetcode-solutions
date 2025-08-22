# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:

    plot_counter = 1
    flowers_placed = 0

    for plot in flowerbed:
        if plot == 0:
            plot_counter += 1
            if plot_counter == 3:
                flowers_placed += 1
                plot_counter = 1
        else:
            plot_counter = 0

    if plot_counter == 2:
        flowers_placed += 1

    return flowers_placed >= n

def main():
    print(canPlaceFlowers([1,0,0,0,1], 1))
    print(canPlaceFlowers([1,0,0,0,1], 2))

if __name__ == "__main__":
    main()


# solution worked on top of the greedy counting of consecutive empty plots, it has been taken into account three main principles of the problem:

# 1. each flower requires three consecutive states [0,0,0], where the middle one is planted and the sides guarantee the no-adjacent rule
# 2. by treating the boundaries as if they had one extra virtual empty plot, the same counting logic can be consistently applied at the start and end
# 3. whenever a valid position for planting is found, it is immediately taken (greedy), as it does not block other possible future placements

# [!] notice that the counting resets whenever a 1 (occupied plot) is found, since adjacency is broken
# [!] notice that at the very end, if the counter equals 2, it still allows one more planting, because the virtual empty boundary completes the three consecutive states


# time complexity: O(n) -> single pass through flowerbed
# space complexity: O(1) -> only counters and variables stored