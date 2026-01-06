# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105


from collections import deque
from typing import Optional

def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    queue = deque([root])
    
    max_sum = float("-inf")
    best_level = 0
    current_level = 1

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            best_level = current_level

        current_level += 1

    return best_level


# solution worked on top of a breadth-first traversal (level-order) strategy, leveraging a queue-based iterative approach

# 1. the tree is traversed level by level, ensuring that all nodes belonging to the same depth are processed together before moving to the next level
# 2. for each level, the number of nodes to be processed is fixed at the start of the iteration, allowing an exact aggregation of values belonging only to that level
# 3. as each level is independent from the others in terms of summation, the maximum level sum can be updated incrementally without revisiting previous nodes

# [!] notice that the queue always contains nodes from at most two consecutive levels, which guarantees controlled memory usage
# [!] notice that level indexing is handled explicitly, starting from level 1 at the root and increasing only after a full level has been processed

# this leads to a single-pass traversal of the tree where level sums are computed on the fly and the level with the maximum accumulated value is selected


# time complexity: O(n) -> each node in the tree is visited exactly once
# space complexity: O(w) -> queue storage proportional to the maximum width of the tree
