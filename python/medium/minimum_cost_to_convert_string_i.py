# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

# Example 1:

# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.
# Example 2:

# Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
# Output: 12
# Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
# Example 3:

# Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
# Output: -1
# Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
 

# Constraints:

# 1 <= source.length == target.length <= 105
# source, target consist of lowercase English letters.
# 1 <= cost.length == original.length == changed.length <= 2000
# original[i], changed[i] are lowercase English letters.
# 1 <= cost[i] <= 106
# original[i] != changed[i]


def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    
    ALPHABET_SIZE = 26
    INF = 10**18
    distance = [[INF] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
    total_cost = 0

    for src_char, dst_char, c in zip(original, changed, cost):
        
        src = ord(src_char) - ord('a')
        dst = ord(dst_char) - ord('a')
        distance[src][dst] = min(distance[src][dst], c)

    for i in range(ALPHABET_SIZE):
        distance[i][i] = 0

    for mid in range(ALPHABET_SIZE):
        for start in range(ALPHABET_SIZE):
            if distance[start][mid] == INF:
                continue
            for end in range(ALPHABET_SIZE):
                
                new_cost = distance[start][mid] + distance[mid][end]
                
                if new_cost < distance[start][end]:
                    distance[start][end] = new_cost

    for s_char, t_char in zip(source, target):
        
        s = ord(s_char) - ord('a')
        t = ord(t_char) - ord('a')
        
        if distance[s][t] == INF:
            return -1
        
        total_cost += distance[s][t]

    return total_cost


# solution is built on top of an all-pairs shortest path dynamic programming approach, where character transformations are modeled as a weighted directed graph over a fixed alphabet:

# 1. each character in the alphabet is treated as a node, and every allowed transformation defines a directed edge with an associated cost
# 2. the problem is reduced to computing the minimum cost to transform any character into any other character, independently of their positions in the strings
# 3. dynamic programming is applied over an intermediate character dimension to progressively relax transformation paths, ensuring that indirect transformations are considered optimally
# 4. once the global minimum transformation costs are computed, the total cost is obtained by aggregating the per-position transformation costs from source to target

# [!] the alphabet size is fixed and small, which makes an O(k³) dynamic programming solution feasible and efficient in practice
# [!] direct transformations are initialized with their minimum cost, allowing multiple edges between the same characters to be safely consolidated
# [!] if at any position no valid transformation path exists, the solution terminates early since the overall transformation is impossible

# this leads to a two-phase solution: first computing the minimum transformation cost between all pairs of characters, and then summing the costs required to transform the source string into the target string


# time complexity: O(k³ + n) -> all-pairs shortest path over the alphabet plus linear scan of the strings
# space complexity: O(k²) -> distance matrix storing minimum transformation costs
