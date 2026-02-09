# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

# Example 1:


# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
# Example 2:


# Input: root = [2,1,3]
# Output: [2,1,3]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    sorted_nodes: list[TreeNode] = []

    def inorder_traversal(node: Optional[TreeNode]) -> None:
        
        if not node:
            return
        
        inorder_traversal(node.left)
        sorted_nodes.append(node)
        inorder_traversal(node.right)

    def build_balanced_bst(left: int, right: int) -> Optional[TreeNode]:
        
        if left > right:
            return None

        mid = (left + right) // 2
        root = sorted_nodes[mid]
        root.left = build_balanced_bst(left, mid - 1)
        root.right = build_balanced_bst(mid + 1, right)

        return root

    inorder_traversal(root)
    return build_balanced_bst(0, len(sorted_nodes) - 1)


# solution worked on top of the inorder traversal properties of a Binary Search Tree combined with a divide-and-conquer reconstruction strategy:

# 1. the inorder traversal of a BST produces nodes in strictly sorted order, which allows transforming the tree structure problem into an ordered sequence problem
# 2. by storing references to the original nodes during traversal, the algorithm preserves node identity while decoupling structure from values
# 3. a balanced BST can be rebuilt by recursively selecting the middle element of the sorted sequence as the root, ensuring minimal height at every subtree
# 4. the left and right subtrees are constructed symmetrically from the left and right partitions of the sorted sequence, enforcing balance through divide-and-conquer

# [!] notice that no new nodes are created during reconstruction; the algorithm only rewires existing node pointers
# [!] notice that the balancing phase is independent from the traversal phase, which allows reasoning about correctness and complexity separately
# [!] because the reconstruction always selects the midpoint, the height difference between subtrees is guaranteed to be at most one

# this leads to a two-phase solution: first linearizing the BST through inorder traversal, and then rebuilding a height-balanced BST from the sorted nodes using recursive partitioning


# time complexity: O(n) -> inorder traversal = O(n), balanced reconstruction = O(n)
# space complexity: O(n) -> auxiliary storage for sorted nodes = O(n), recursion stack = O(n)
