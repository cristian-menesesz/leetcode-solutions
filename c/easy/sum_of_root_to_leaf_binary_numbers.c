#include <stdio.h>
#include <stdlib.h>

/* Tree node definition */
typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;


/* DFS helper */
int dfs(TreeNode* node, int current_value) {
    if (node == NULL)
        return 0;

    /* Shift bits and append current bit */
    current_value = (current_value << 1) | node->val;

    /* Leaf node */
    if (node->left == NULL && node->right == NULL)
        return current_value;

    return dfs(node->left, current_value)
         + dfs(node->right, current_value);
}


/* Main function */
int sumRootToLeaf(TreeNode* root) {
    return dfs(root, 0);
}