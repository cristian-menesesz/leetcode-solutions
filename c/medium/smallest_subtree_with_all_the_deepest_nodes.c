#include <stdlib.h>

typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

int global_max_depth = 0;

typedef struct {
    TreeNode* node;
    int depth;
} Result;

Result dfs(TreeNode* node, int current_depth) {
    if (node == NULL) {
        if (current_depth > global_max_depth)
            global_max_depth = current_depth;
        Result r = { NULL, current_depth };
        return r;
    }

    Result left = dfs(node->left, current_depth + 1);
    Result right = dfs(node->right, current_depth + 1);

    if (left.depth == right.depth && left.depth == global_max_depth) {
        Result r = { node, left.depth };
        return r;
    }

    return (left.depth > right.depth) ? left : right;
}

TreeNode* subtreeWithAllDeepest(TreeNode* root) {
    global_max_depth = 0;
    Result r = dfs(root, 0);
    return r.node;
}
