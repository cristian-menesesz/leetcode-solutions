#include <stdlib.h>
#include <stdint.h>

#define MOD 1000000007

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

long long max_product = 0;
long long total_tree_sum = 0;

long long compute_subtree_sum(struct TreeNode* node) {
    
    if (node == NULL) return 0;

    long long left = compute_subtree_sum(node->left);
    long long right = compute_subtree_sum(node->right);
    long long subtree_sum = node->val + left + right;
    long long product = subtree_sum * (total_tree_sum - subtree_sum);

    if (product > max_product) {
        max_product = product;
    }

    return subtree_sum;
}

int maxProduct(struct TreeNode* root) {
    
    max_product = 0;
    total_tree_sum = 0;

    total_tree_sum = compute_subtree_sum(root);
    compute_subtree_sum(root);

    return (int)(max_product % MOD);
}
