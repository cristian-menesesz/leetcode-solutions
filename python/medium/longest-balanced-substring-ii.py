# You are given a string s consisting only of the characters 'a', 'b', and 'c'.

# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

# Return the length of the longest balanced substring of s.

 

# Example 1:

# Input: s = "abbac"

# Output: 4

# Explanation:

# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:

# Input: s = "aabcc"

# Output: 3

# Explanation:

# The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

# Example 3:

# Input: s = "aba"

# Output: 2

# Explanation:

# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

 

# Constraints:

# 1 <= s.length <= 105
# s contains only the characters 'a', 'b', and 'c'.


class Solution:
    def _longest_single_char_run(self, s: str) -> int:

        max_run = 1
        current_run = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_run += 1
            else:
                max_run = max(max_run, current_run)
                current_run = 1
        
        return max(max_run, current_run)

    def longestBalanced(self, s: str) -> int:
        
        n = len(s)
        
        # Case: only one distinct character
        max_length = self._longest_single_char_run(s)
        
        # Maps to track earliest index of prefix states
        seen_abc = {(0, 0): -1}  # (B-A, C-A)
        seen_ab  = {(0, 0): -1}  # (A-B, C)
        seen_bc  = {(0, 0): -1}  # (B-C, A)
        seen_ca  = {(0, 0): -1}  # (C-A, B)
        
        count_a = count_b = count_c = 0
        
        for index, char in enumerate(s):
            if char == 'a':
                count_a += 1
            elif char == 'b':
                count_b += 1
            else:  # 'c'
                count_c += 1
            
            A, B, C = count_a, count_b, count_c
            
            # --- 3-letter balance: A = B = C ---
            key = (B - A, C - A)
            if key in seen_abc:
                max_length = max(max_length, index - seen_abc[key])
            else:
                seen_abc[key] = index
            
            # --- 2-letter balance: A = B and no C ---
            key = (A - B, C)
            if key in seen_ab:
                max_length = max(max_length, index - seen_ab[key])
            else:
                seen_ab[key] = index
            
            # --- 2-letter balance: B = C and no A ---
            key = (B - C, A)
            if key in seen_bc:
                max_length = max(max_length, index - seen_bc[key])
            else:
                seen_bc[key] = index
            
            # --- 2-letter balance: C = A and no B ---
            key = (C - A, B)
            if key in seen_ca:
                max_length = max(max_length, index - seen_ca[key])
            else:
                seen_ca[key] = index
        
        return max_length


# solution worked on top of the prefix state compression + hash-based memoization approach, it has been taken into account five main principles of the problem:

# 1. any balanced substring can be characterized by invariant relations between prefix frequency differences (e.g., A = B = C ⇔ (B − A, C − A) remains constant between two indices)
# 2. instead of recomputing frequencies for every substring, cumulative counts (prefix sums) are maintained, allowing any substring balance condition to be reduced to equality between two prefix states
# 3. each balance configuration (three-letter balance and each two-letter balance excluding the third) is represented as a compressed state key stored in a hash map that records the earliest occurrence of that state
# 4. when the same prefix state reappears at a later index, the substring between the two indices satisfies the corresponding balance condition, and its length can be computed in O(1)
# 5. the single-distinct-character case is treated independently by computing the longest contiguous run, since pure repetition is a degenerate balanced case not captured by inter-letter difference states

# [!] notice that each balance condition is isolated in its own hash structure because their state definitions are not interchangeable; merging them would mix invariants and invalidate correctness
# [!] as only the earliest occurrence of each prefix state is stored, this guarantees maximum substring length while preserving O(1) lookup and update

# this leads to a single linear traversal of the string where prefix frequencies define invariant states, and repeated states directly yield maximal balanced substrings through constant-time hash lookups


# time complexity: O(n) -> single pass with constant-time hash operations
# space complexity: O(n) -> hash maps storing prefix states


# beats 96% - 796ms

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # --- 1) Longest single-character run ---
        max_run = 1
        current_run = 1
        
        for i in range(1, n):
            if s[i] == s[i - 1]:
                current_run += 1
            else:
                max_run = max(max_run, current_run)
                current_run = 1
        
        max_run = max(max_run, current_run)

        result = max_run

        # --- 2) Two-character balanced substrings ---
        result = max(result, self._longest_two_balanced(s, 'a', 'b'))
        result = max(result, self._longest_two_balanced(s, 'a', 'c'))
        result = max(result, self._longest_two_balanced(s, 'b', 'c'))

        # --- 3) Three-character balanced substrings ---
        result = max(result, self._longest_three_balanced(s))

        return result


    def _longest_two_balanced(self, s: str, char1: str, char2: str) -> int:
        """
        Longest substring containing only char1 and char2
        where count(char1) == count(char2).
        """
        first_occurrence = {0: -1}
        balance = 0
        last_invalid_index = -1
        max_length = 0

        for i, ch in enumerate(s):
            if ch != char1 and ch != char2:
                # Reset when third character appears
                balance = 0
                first_occurrence = {0: i}
                last_invalid_index = i
                continue

            if ch == char1:
                balance += 1
            else:
                balance -= 1

            if balance in first_occurrence:
                max_length = max(max_length, i - first_occurrence[balance])
            else:
                first_occurrence[balance] = i

        return max_length


    def _longest_three_balanced(self, s: str) -> int:
        """
        Longest substring where count(a) == count(b) == count(c).
        """
        # Track differences relative to 'a'
        first_occurrence = {(0, 0): -1}
        
        count_a = count_b = count_c = 0
        max_length = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                count_a += 1
            elif ch == 'b':
                count_b += 1
            else:
                count_c += 1

            # State defined by two independent differences
            state = (count_b - count_a, count_c - count_a)

            if state in first_occurrence:
                max_length = max(max_length, i - first_occurrence[state])
            else:
                first_occurrence[state] = i

        return max_length


# solution worked on top of prefix-state hashing and balance invariants, it decomposes the problem into independent balance configurations (1-character, 2-character, and 3-character cases) and computes the maximum valid substring in each scenario.

# 1. the single-character case is treated as a maximal consecutive run, since equal frequency is trivially satisfied when only one symbol exists; this establishes a lower bound for the answer.
# 2. for the two-character case, the approach models the substring as a prefix-balance problem where balance = count(char1) - count(char2); whenever the same balance value reappears, the substring between the two indices has equal frequency of both characters.
# 3. as soon as a third character appears in the two-character analysis, the balance state becomes invalid and the prefix structure must be reset, effectively partitioning the string into independent valid segments.
# 4. for the three-character case, the approach reduces the equality condition count(a) == count(b) == count(c) into two independent linear invariants: (count_b - count_a) and (count_c - count_a); these two differences uniquely define a state in a 2D prefix space.
# 5. if the same 2D state reappears at two indices, the substring between them preserves zero net change in both differences, which implies equal counts of all three characters.

# [!] notice that equality constraints are transformed into prefix-state reoccurrence detection rather than brute-force frequency comparison.
# [!] the algorithm avoids O(n^2) substring enumeration by leveraging hash maps that store the first occurrence of each balance state.

# this leads to evaluating three independent balance models (run-based, 1D prefix-difference, and 2D prefix-difference), and selecting the maximum valid substring length among them.


# time complexity: O(n) -> single pass per balance configuration
# space complexity: O(n) -> hash maps storing prefix states
