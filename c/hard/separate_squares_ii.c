#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *x_coords;
    int segment_count;
    int *coverage_count;
    int *covered_length;
} SegmentTree;

SegmentTree *segment_tree_create(int *x_coords, int n) {
    SegmentTree *st = malloc(sizeof(SegmentTree));
    st->x_coords = x_coords;
    st->segment_count = n - 1;
    st->coverage_count = calloc(4 * st->segment_count, sizeof(int));
    st->covered_length = calloc(4 * st->segment_count, sizeof(int));
    return st;
}

void segment_tree_update(
    SegmentTree *st,
    int x_left,
    int x_right,
    int delta,
    int left,
    int right,
    int node
) {
    if (st->x_coords[right + 1] <= x_left ||
        st->x_coords[left] >= x_right) {
        return;
    }

    if (x_left <= st->x_coords[left] &&
        st->x_coords[right + 1] <= x_right) {
        st->coverage_count[node] += delta;
    } else {
        int mid = (left + right) / 2;
        segment_tree_update(st, x_left, x_right, delta, left, mid, node * 2 + 1);
        segment_tree_update(st, x_left, x_right, delta, mid + 1, right, node * 2 + 2);
    }

    if (st->coverage_count[node] > 0) {
        st->covered_length[node] =
            st->x_coords[right + 1] - st->x_coords[left];
    } else {
        if (left == right) {
            st->covered_length[node] = 0;
        } else {
            st->covered_length[node] =
                st->covered_length[node * 2 + 1] +
                st->covered_length[node * 2 + 2];
        }
    }
}

int segment_tree_query(SegmentTree *st) {
    return st->covered_length[0];
}
