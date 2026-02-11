#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int min_value;
    int max_value;
    int lazy;
} SegmentNode;

typedef struct {
    int n;
    SegmentNode *tree;
} SegmentTree;

/* ---------- Segment Tree Core ---------- */

void pull(SegmentTree *st, int idx) {
    SegmentNode *left = &st->tree[idx * 2];
    SegmentNode *right = &st->tree[idx * 2 + 1];

    st->tree[idx].min_value =
        left->min_value < right->min_value ? left->min_value : right->min_value;

    st->tree[idx].max_value =
        left->max_value > right->max_value ? left->max_value : right->max_value;
}

void push_lazy(SegmentTree *st, int idx, int left, int right) {
    SegmentNode *node = &st->tree[idx];

    if (node->lazy == 0) return;

    node->min_value += node->lazy;
    node->max_value += node->lazy;

    if (left < right) {
        st->tree[idx * 2].lazy += node->lazy;
        st->tree[idx * 2 + 1].lazy += node->lazy;
    }

    node->lazy = 0;
}

void build(SegmentTree *st, int idx, int left, int right, int *arr) {
    if (left == right) {
        st->tree[idx].min_value = arr[left];
        st->tree[idx].max_value = arr[left];
        st->tree[idx].lazy = 0;
        return;
    }

    int mid = (left + right) / 2;
    build(st, idx * 2, left, mid, arr);
    build(st, idx * 2 + 1, mid + 1, right, arr);
    pull(st, idx);
}

void range_add(SegmentTree *st, int ql, int qr,
               int idx, int left, int right, int value) {

    push_lazy(st, idx, left, right);

    if (right < ql || left > qr) return;

    if (ql <= left && right <= qr) {
        st->tree[idx].lazy += value;
        push_lazy(st, idx, left, right);
        return;
    }

    int mid = (left + right) / 2;
    range_add(st, ql, qr, idx * 2, left, mid, value);
    range_add(st, ql, qr, idx * 2 + 1, mid + 1, right, value);

    pull(st, idx);
}

int find_rightmost_zero(SegmentTree *st, int idx, int left, int right) {
    push_lazy(st, idx, left, right);

    if (st->tree[idx].min_value > 0 ||
        st->tree[idx].max_value < 0)
        return -1;

    if (left == right)
        return left;

    int mid = (left + right) / 2;

    int right_result =
        find_rightmost_zero(st, idx * 2 + 1, mid + 1, right);

    if (right_result != -1)
        return right_result;

    return find_rightmost_zero(st, idx * 2, left, mid);
}

/* ---------- Bruteforce ---------- */

int bruteforce_longest_balanced(int *nums, int n) {
    int best = 0;

    for (int start = 0; start < n; start++) {
        if (start > n - best) break;

        int *seen = calloc(100001, sizeof(int));
        int diff = 0;

        for (int end = start; end < n; end++) {
            int x = nums[end];

            if (!seen[x]) {
                seen[x] = 1;
                diff += (x % 2 == 0) ? 1 : -1;
            }

            if (diff == 0) {
                int length = end - start + 1;
                if (length > best)
                    best = length;
            }
        }

        free(seen);
    }

    return best;
}

/* ---------- Main Logic ---------- */

int longestBalanced(int *nums, int n) {

    if (n <= 2000)
        return bruteforce_longest_balanced(nums, n);

    int *last_occ = malloc(sizeof(int) * 100001);
    int *next_pos = malloc(sizeof(int) * n);

    for (int i = 0; i < 100001; i++)
        last_occ[i] = n;

    for (int i = n - 1; i >= 0; i--) {
        next_pos[i] = last_occ[nums[i]];
        last_occ[nums[i]] = i;
    }

    int *prefix = malloc(sizeof(int) * n);
    int *seen = calloc(100001, sizeof(int));

    int diff = 0;

    for (int i = 0; i < n; i++) {
        if (!seen[nums[i]]) {
            seen[nums[i]] = 1;
            diff += (nums[i] % 2) ? 1 : -1;
        }
        prefix[i] = diff;
    }

    SegmentTree st;
    st.n = n;
    st.tree = calloc(4 * n, sizeof(SegmentNode));

    build(&st, 1, 0, n - 1, prefix);

    int answer = find_rightmost_zero(&st, 1, 0, n - 1);
    answer = (answer != -1) ? answer + 1 : 0;

    for (int i = 0; i < n - 1; i++) {
        int right_limit = next_pos[i] - 1;

        if (i + 1 <= right_limit) {
            int adjustment = (nums[i] % 2) ? -1 : 1;
            range_add(&st, i + 1, right_limit,
                      1, 0, n - 1, adjustment);
        }

        int rightmost = find_rightmost_zero(&st, 1, 0, n - 1);
        if (rightmost != -1) {
            int length = rightmost - i;
            if (length > answer)
                answer = length;
        }
    }

    free(last_occ);
    free(next_pos);
    free(prefix);
    free(seen);
    free(st.tree);

    return answer;
}
