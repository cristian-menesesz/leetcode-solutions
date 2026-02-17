# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".


# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.

# For example, "10:2" is not valid. It should be "10:02".
 

# Example 1:

# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
# Example 2:

# Input: turnedOn = 9
# Output: []
 

# Constraints:

# 0 <= turnedOn <= 10


def readBinaryWatch(self, turnedOn: int) -> list[str]:
    
    if turnedOn == 0:
        return ["0:00"]

    MINUTE_MASK = (1 << 6) - 1  # lower 6 bits represent minutes
    combination = (1 << turnedOn) - 1  # smallest number with k bits set
    max_combination = combination << (10 - turnedOn)

    valid_times = []

    while combination <= max_combination:
        minutes = combination & MINUTE_MASK
        hours = combination >> 6

        if hours < 12 and minutes < 60:
            valid_times.append(f"{hours}:{minutes:02}")

        # Gosper's Hack — next k-bit combination
        lowest_set_bit = combination & -combination
        next_value = combination + lowest_set_bit
        combination = (((combination ^ next_value) // lowest_set_bit) >> 2) | next_value

    return valid_times


# solution worked on top of the bit manipulation combinatorial generation approach, it has been taken into account four main principles of the problem:

# 1. the binary watch can be modeled as a 10-bit number where the upper 4 bits represent hours (0–11) and the lower 6 bits represent minutes (0–59), allowing the problem to be reduced to generating fixed-size bit patterns
# 2. instead of iterating over all possible hour–minute pairs, the approach generates directly all integers with exactly turnedOn bits set among 10 positions, reducing unnecessary exploration
# 3. by masking the lower 6 bits (minute mask) and right-shifting the remaining bits (hours), each combination is decomposed into its hour and minute components in constant time
# 4. Gosper’s Hack is used to compute the next integer with the same number of set bits in lexicographical order, ensuring efficient traversal of all valid k-bit combinations without recomputation

# [!] notice that no explicit backtracking or nested iteration over hours and minutes is required, as the combinatorial generation guarantees coverage of all possible LED distributions
# [!] as the generation is constrained to exactly turnedOn active bits, the search space is pruned structurally rather than conditionally

# this leads to the computation of all valid time representations by iterating only over fixed-popcount 10-bit configurations, decomposing each into hours and minutes, and filtering invalid states


# time complexity: O(C(10, k)) → bounded by O(2^10) in the worst case, effectively constant
# space complexity: O(C(10, k)) → storage of valid combinations, auxiliary space O(1)
