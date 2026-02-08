# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> Tuple[int, bool]:

        if node is None:
            return 0, True

        left_height, left_balanced = dfs(node.left)
        right_height, right_balanced = dfs(node.right)

        height = 1 + max(left_height, right_height)
        is_balanced = (
            left_balanced
            and right_balanced
            and abs(left_height - right_height) <= 1
        )

        return height, is_balanced

    _, is_balanced_tree = dfs(root)
    return is_balanced_tree


# solution follows a bottom-up depth-first traversal combined with implicit dynamic programming through memoized returns

# 1. each subtree computation returns a compound state that contains all the information required by its parent (height and balance status)
# 2. balance verification is deferred until both child subtrees have been fully evaluated, ensuring local correctness before propagation
# 3. subtree height is computed as a dependent value of its children, allowing balance constraints to be checked without revisiting nodes

# [!] notice that height and balance are computed simultaneously, avoiding separate traversals or recomputation
# [!] once an unbalanced subtree is detected, the imbalance is propagated upward without altering the traversal flow

# this leads to a single-pass post-order traversal where global balance is inferred from locally consistent subtree states


# time complexity: O(n) -> each node is visited exactly once during the dfs traversal
# space complexity: O(h) -> recursion stack proportional to the height of the tree (worst case O(n))
