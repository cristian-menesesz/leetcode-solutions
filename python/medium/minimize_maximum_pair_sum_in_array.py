def minPairSum(self, nums: list[int]) -> int:
    
    MAX_VALUE = 100_000
    frequency = [0] * (MAX_VALUE + 1)

    min_value = MAX_VALUE
    max_value = 0

    for num in nums:
        frequency[num] += 1
        min_value = min(min_value, num)
        max_value = max(max_value, num)

    pairs_needed = len(nums) // 2
    smallest_used = 0
    largest_used = 0

    left = min_value
    right = max_value

    worst_pair_sum = 0

    for pair_number in range(1, pairs_needed + 1):

        while smallest_used < pair_number:
            smallest_used += frequency[left]
            left += 1

        while largest_used < pair_number:
            largest_used += frequency[right]
            right -= 1

        worst_pair_sum = max(worst_pair_sum, left + right)

    return worst_pair_sum
