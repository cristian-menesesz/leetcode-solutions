#include <stdlib.h>
#include <limits.h>

typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

typedef struct {
    TreeNode** data;
    int front, rear, size, capacity;
} Queue;

Queue* createQueue(int capacity) {
    Queue* q = malloc(sizeof(Queue));
    q->capacity = capacity;
    q->front = q->size = 0;
    q->rear = capacity - 1;
    q->data = malloc(capacity * sizeof(TreeNode*));
    return q;
}

int isEmpty(Queue* q) {
    return q->size == 0;
}

void enqueue(Queue* q, TreeNode* node) {
    q->rear = (q->rear + 1) % q->capacity;
    q->data[q->rear] = node;
    q->size++;
}

TreeNode* dequeue(Queue* q) {
    TreeNode* node = q->data[q->front];
    q->front = (q->front + 1) % q->capacity;
    q->size--;
    return node;
}

int maxLevelSum(TreeNode* root) {
    if (!root) return 0;

    Queue* q = createQueue(10000);
    enqueue(q, root);
    
    int max_sum = INT_MIN;
    int best_level = 0;
    int current_level = 1;

    while (!isEmpty(q)) {
        
        int level_size = q->size;
        int level_sum = 0;

        for (int i = 0; i < level_size; i++) {
            TreeNode* node = dequeue(q);
            level_sum += node->val;

            if (node->left) enqueue(q, node->left);
            if (node->right) enqueue(q, node->right);
        }

        if (level_sum > max_sum) {
            max_sum = level_sum;
            best_level = current_level;
        }

        current_level++;
    }

    return best_level;
}
