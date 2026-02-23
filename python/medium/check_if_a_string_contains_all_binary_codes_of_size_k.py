# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s[i] is either '0' or '1'.
# 1 <= k <= 20


def hasAllCodes(self, s: str, k: int) -> bool:
    
    n = len(s)
    
    if n < k:
        return False

    total_codes = 1 << k  # number of possible k-length codes
    window_mask = 0  # rolling k-bit integer
    lower_bits_mask = (1 << (k - 1)) - 1

    # Faster than set() for dense integer domain
    seen = [False] * total_codes
    seen_count = 0

    # ---- build first window ----
    for i in range(k):
        window_mask = (window_mask << 1) | (s[i] == '1')

    seen[window_mask] = True
    seen_count = 1

    # ---- sliding window ----
    for right in range(k, n):
        # remove highest bit
        window_mask &= lower_bits_mask

        # shift + add new bit
        window_mask = (window_mask << 1) | (s[right] == '1')

        if not seen[window_mask]:
            seen[window_mask] = True
            seen_count += 1

            # early exit optimization
            if seen_count == total_codes:
                return True

    return seen_count == total_codes
    

# solution worked on top of a rolling bitmask + sliding window approach, leveraging fixed-size binary encoding and dense-state tracking to verify the existence of all k-length binary substrings.

# 1. every substring of length k is represented as a k-bit integer mask, allowing constant-time transitions between consecutive substrings instead of rebuilding substrings explicitly
# 2. a sliding window shifts one position at a time, removing the most significant bit and appending the incoming bit, preserving the k-length representation in O(1) time
# 3. as the domain of possible substrings is finite (2^k), a direct-indexed boolean array replaces hash structures, enabling dense memoization and constant-time presence checks
# 4. each newly generated mask corresponds to a unique binary code, and counting unseen masks incrementally determines whether the complete state space has been covered

# [!] substring construction is avoided entirely; computation operates only on integer bit transformations
# [!] early termination is possible once all 2^k codes are discovered, preventing unnecessary traversal of the remaining string

# this leads to scanning the string once while enumerating all reachable k-bit states through rolling transitions, validating coverage of the complete binary code space.


# time complexity: O(n) -> single pass sliding window
# space complexity: O(2^k) -> boolean memoization of all k-bit states
