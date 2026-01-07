# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104


from typing import Optional

def maxProduct(self, root: Optional[TreeNode]) -> int:

    MOD = 10**9 + 7
    max_product = 0
    total_tree_sum = 0

    def compute_subtree_sum(node: Optional[TreeNode]) -> int:
        
        nonlocal max_product, total_tree_sum

        if node is None:
            return 0

        subtree_sum = (
            node.val
            + compute_subtree_sum(node.left)
            + compute_subtree_sum(node.right)
        )
        max_product = max(
            max_product,
            subtree_sum * (total_tree_sum - subtree_sum)
        )

        return subtree_sum

    total_tree_sum = compute_subtree_sum(root)
    compute_subtree_sum(root)

    return max_product % MOD


# solution worked on top of a tree-based depth-first traversal combined with global aggregation, it has been taken into account three main principles of the problem:

# 1. the total sum of the tree must be known in advance, as every valid split of the tree depends on partitioning this total into two complementary subtree sums
# 2. every possible split of the tree can be represented by cutting exactly one edge, which is equivalent to considering each subtree sum as a candidate partition
# 3. during a post-order traversal, the subtree sum is fully determined at each node, making it possible to evaluate the product of the two resulting parts locally while propagating information upward

# [!] notice that subtree sums must be computed bottom-up (post-order), otherwise the contribution of child subtrees would be incomplete
# [!] the maximum product is updated independently of the traversal order once the total tree sum is fixed, allowing reuse of the same traversal logic

# this leads to a two-pass depth-first strategy: the first pass computes the total sum of the tree, and the second pass evaluates all valid subtree partitions to maximize the product


# time complexity: O(n) -> each node is visited a constant number of times
# space complexity: O(h) -> recursion stack, where h is the height of the tree
