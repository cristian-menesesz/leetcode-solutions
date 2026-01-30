# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string changed[i].

# You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy either of these two conditions:

# The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the indices picked in both operations are disjoint.
# The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the indices picked in both operations are identical.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

# Example 1:

# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert "abcd" to "acbe", do the following operations:
# - Change substring source[1..1] from "b" to "c" at a cost of 5.
# - Change substring source[2..2] from "c" to "e" at a cost of 1.
# - Change substring source[2..2] from "e" to "b" at a cost of 2.
# - Change substring source[3..3] from "d" to "e" at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28. 
# It can be shown that this is the minimum possible cost.
# Example 2:

# Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
# Output: 9
# Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
# - Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
# - Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
# - Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
# The total cost incurred is 1 + 3 + 5 = 9.
# It can be shown that this is the minimum possible cost.
# Example 3:

# Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
# Output: -1
# Explanation: It is impossible to convert "abcdefgh" to "addddddd".
# If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
# If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
 

# Constraints:

# 1 <= source.length == target.length <= 1000
# source, target consist only of lowercase English characters.
# 1 <= cost.length == original.length == changed.length <= 100
# 1 <= original[i].length == changed[i].length <= source.length
# original[i], changed[i] consist only of lowercase English characters.
# original[i] != changed[i]
# 1 <= cost[i] <= 106


def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        
    INF = 10**30
    n = len(source)
    m = len(original)

    string_to_id: dict[str, int] = {}
    valid_lengths: set[int] = set()
    next_id = 0

    # Distance matrix for Floyd–Warshall
    # Max possible unique strings = 2 * m
    max_nodes = 2 * m
    dist = [[INF] * max_nodes for _ in range(max_nodes)]

    # Assign IDs and initialize direct transformation costs
    for i in range(m):
        src = original[i]
        dst = changed[i]
        c = cost[i]

        if src not in string_to_id:
            string_to_id[src] = next_id
            valid_lengths.add(len(src))
            next_id += 1

        if dst not in string_to_id:
            string_to_id[dst] = next_id
            next_id += 1

        u = string_to_id[src]
        v = string_to_id[dst]
        dist[u][v] = min(dist[u][v], c)

    # Distance to self is zero
    for i in range(next_id):
        dist[i][i] = 0

    # Floyd–Warshall: all-pairs shortest paths
    for k in range(next_id):
        for i in range(next_id):
            if dist[i][k] == INF:
                continue
            ik = dist[i][k]
            row_k = dist[k]
            row_i = dist[i]
            for j in range(next_id):
                if row_k[j] != INF:
                    row_i[j] = min(row_i[j], ik + row_k[j])

    # DP over positions in source
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == INF:
            continue

        # Case 1: characters already match
        if source[i] == target[i]:
            dp[i + 1] = min(dp[i + 1], dp[i])

        # Case 2: try transforming substrings
        for length in valid_lengths:
            if i + length > n:
                continue

            src_sub = source[i : i + length]
            tgt_sub = target[i : i + length]

            if src_sub not in string_to_id or tgt_sub not in string_to_id:
                continue

            u = string_to_id[src_sub]
            v = string_to_id[tgt_sub]

            if dist[u][v] != INF:
                dp[i + length] = min(dp[i + length], dp[i] + dist[u][v])

    return -1 if dp[n] == INF else dp[n]


# solution is built on top of graph shortest-path precomputation combined with dynamic programming over string positions, it has been taken into account three main principles of the approach:

# 1. all substring transformations are modeled as a directed weighted graph, where nodes represent distinct substrings and edges represent direct transformations with an associated cost
# 2. since transformations can be chained, the minimum cost between any two substrings must be precomputed using an all-pairs shortest path strategy, ensuring that the dp stage always consumes optimal transformation costs
# 3. the string is processed left-to-right using dynamic programming, where each dp[i] represents the minimum cost to correctly transform the prefix source[0:i] into target[0:i], allowing independent local decisions to compose a global optimum

# [!] only substring lengths that appear in the transformation rules are considered, which prunes invalid states and bounds the dp transitions
# [!] character-level equality is treated as a zero-cost transition, avoiding unnecessary graph lookups and preserving optimal substructure

# this leads to a solution where the transformation graph resolves global substitution costs first, and a linear dp pass stitches these costs together to compute the minimum total transformation cost for the full string


# time complexity: O(K^3 + n * L) where K is the number of unique substrings involved in transformations (handled by Floyd–Warshall), n is the length of the source string, and L is the number of valid transformation lengths
# space complexity: O(K^2 + n) due to the all-pairs distance matrix and the dp memoization array
