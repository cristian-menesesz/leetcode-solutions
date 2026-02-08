#include <stdbool.h>
#include <stdlib.h>

typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

typedef struct {
    int height;
    bool balanced;
} Result;

Result dfs(TreeNode* node) {
    if (node == NULL) {
        Result r = {0, true};
        return r;
    }

    Result left = dfs(node->left);
    Result right = dfs(node->right);

    Result r;
    r.height = 1 + (left.height > right.height ? left.height : right.height);
    r.balanced =
        left.balanced &&
        right.balanced &&
        abs(left.height - right.height) <= 1;

    return r;
}

bool isBalanced(TreeNode* root) {
    Result r = dfs(root);
    return r.balanced;
}
