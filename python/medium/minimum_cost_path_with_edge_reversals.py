# You are given a directed, weighted graph with n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

# Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch, you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

# The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

# Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.

 

# Example 1:

# Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

# Output: 5

# Explanation:



# Use the path 0 → 1 (cost 3).
# At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
# Total cost is 3 + 2 = 5.
# Example 2:

# Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

# Output: 3

# Explanation:

# No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
# Total cost is 1 + 1 + 1 = 3.
 

# Constraints:

# 2 <= n <= 5 * 104
# 1 <= edges.length <= 105
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 1000


import heapq
from numpy import inf

def minCost(self, n: int, edges: list[list[int]]) -> int:

    adjacency_list = [[] for _ in range(n)]
    min_distance = [0] + [inf] * (n - 1)
    min_heap = [(0, 0)]
    heapq.heapify(min_heap)

    for from_node, to_node, weight in edges:
        adjacency_list[from_node].append((weight, to_node))
        adjacency_list[to_node].append((weight << 1, from_node))

    while min_heap:
        
        current_cost, current_node = heapq.heappop(min_heap)

        if current_cost > min_distance[current_node]:
            continue

        if current_node == n - 1:
            return current_cost

        for edge_cost, next_node in adjacency_list[current_node]:
            
            new_cost = current_cost + edge_cost
            
            if new_cost < min_distance[next_node]:
                min_distance[next_node] = new_cost
                heapq.heappush(min_heap, (new_cost, next_node))

    return -1


# solution works on top of a graph shortest-path greedy strategy using priority queue optimization, leveraging asymmetric edge costs and early termination guarantees.

# 1. the problem space is modeled as a weighted graph using an adjacency list, allowing efficient exploration of reachable states while preserving directional cost differences.
# 2. a min-heap (priority queue) is used to always expand the currently cheapest known path, ensuring that once a node is finalized, its minimum cost is optimal.
# 3. asymmetric traversal costs are encoded directly during graph construction by assigning different weights depending on the traversal direction, avoiding post-processing or state duplication.
# 4. distance relaxation is applied greedily, updating only when a strictly better cost is found, which bounds unnecessary heap insertions.

# [!] notice that once the destination node is extracted from the heap, the algorithm can terminate immediately, as no cheaper path can exist beyond that point.
# [!] outdated heap entries are safely ignored by comparing against the stored minimum distance, preserving correctness without explicit heap cleanup.

# this leads to a single-source shortest path computation that efficiently propagates minimum costs until the destination is reached or all reachable states are exhausted.


# time complexity: O((n + e) log n) -> heap-based shortest path over adjacency list
# space complexity: O(n + e) -> adjacency list + distance memoization
