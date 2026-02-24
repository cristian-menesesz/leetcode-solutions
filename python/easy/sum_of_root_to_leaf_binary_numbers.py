# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# The test cases are generated so that the answer fits in a 32-bits integer.

 

# Example 1:


# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

class Solution:
    def sumRootToLeaf(self, root: Optional["TreeNode"]) -> int:
        """
        Computes the sum of all binary numbers formed by
        root-to-leaf paths using DFS + bit accumulation.
        """

        def dfs(node: Optional["TreeNode"], current_value: int) -> int:
            
            if node is None:
                return 0

            # Shift previous bits and append current bit
            current_value = (current_value << 1) | node.val

            # Leaf node → complete binary number
            if node.left is None and node.right is None:
                return current_value

            # Recurse on children
            return (
                dfs(node.left, current_value) +
                dfs(node.right, current_value)
            )

        return dfs(root, 0)
    

# solution worked on top of the depth-first search (DFS) traversal combined with incremental bit manipulation accumulation, where each root-to-leaf path is interpreted as a binary number constructed during traversal.

# 1. the traversal follows a preorder DFS, propagating state through recursion, where the state represents the partial binary value formed from the root to the current node
# 2. at each step, the binary number is constructed incrementally by shifting the previously accumulated bits to the left and appending the current node value as the least significant bit
# 3. the recursion naturally models path independence, meaning each recursive branch represents a unique root-to-leaf path whose accumulated value does not interfere with other branches
# 4. leaf nodes define termination states of valid binary numbers, therefore computation is finalized only when a leaf is reached and its accumulated value is returned

# [!] notice that no explicit path storage is required, as the binary number is encoded directly in an integer through bitwise operations, reducing memory usage
# [!] the aggregation of results happens during recursion unwinding, allowing subtree results to be combined without auxiliary data structures

# this leads to a single-pass traversal of the tree where binary values are constructed on-the-fly and summed across all root-to-leaf paths


# time complexity: O(n) -> each node is visited exactly once
# space complexity: O(h) -> recursion stack proportional to tree height
