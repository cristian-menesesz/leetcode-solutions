# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
# Example 2:

# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
# Example 3:

# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 

# Constraints:

# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
 

# Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/


import Optional

def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    self.global_max_depth = 0

    def dfs(node: Optional[TreeNode], current_depth: int) -> tuple[Optional[TreeNode], int]:

        if node is None:
            self.global_max_depth = max(self.global_max_depth, current_depth)
            return None, current_depth
        left_node, left_depth = dfs(node.left, current_depth + 1)
        right_node, right_depth = dfs(node.right, current_depth + 1)

        if (
            left_depth == right_depth
            and left_depth == self.global_max_depth
        ):
            return node, left_depth

        if left_depth > right_depth:
            return left_node, left_depth
        else:
            return right_node, right_depth

    result, _ = dfs(root, 0)

    return result


# solution worked on top of a depth-first search (DFS) with post-order traversal, combined with depth propagation to identify the lowest common ancestor (LCA) of all deepest nodes in the tree.

# 1. the traversal computes the depth of each subtree bottom-up, ensuring that every node knows the maximum depth reachable through its children
# 2. a global maximum depth is tracked to represent the deepest level reached anywhere in the tree
# 3. when both left and right subtrees reach the same maximum depth, the current node is identified as the root of the smallest subtree containing all deepest nodes
# 4. if only one subtree reaches a deeper level, the candidate subtree is propagated upward unchanged

# [!] the algorithm relies on post-order traversal so that child depths are fully computed before making decisions at the parent node
# [!] global state is used only to record the deepest level, while subtree selection remains purely local and deterministic

# this leads to a single-pass DFS that simultaneously computes depths and determines the subtree root that contains all deepest nodes


# time complexity: O(n) -> each node is visited exactly once
# space complexity: O(h) -> recursion stack, where h is the height of the tree
