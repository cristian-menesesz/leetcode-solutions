#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* Dynamic array to store nodes */
struct TreeNode **nodes;
int size = 0;
int capacity = 0;

void push(struct TreeNode *node) {
    if (size == capacity) {
        capacity = capacity == 0 ? 8 : capacity * 2;
        nodes = realloc(nodes, capacity * sizeof(struct TreeNode *));
    }
    nodes[size++] = node;
}

void inorder(struct TreeNode *root) {
    if (!root) return;
    inorder(root->left);
    push(root);
    inorder(root->right);
}

struct TreeNode *build(int left, int right) {
    if (left > right) return NULL;
    int mid = (left + right) / 2;
    struct TreeNode *root = nodes[mid];
    root->left = build(left, mid - 1);
    root->right = build(mid + 1, right);
    return root;
}

struct TreeNode *balanceBST(struct TreeNode *root) {
    inorder(root);
    return build(0, size - 1);
}
