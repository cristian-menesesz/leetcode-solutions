#include <stdio.h>
#include <stdlib.h>

int cmp_int(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

/*
 * Computes all pairwise gaps and stores them in a boolean array.
 * gaps[d] = 1 means distance d exists.
 */
void compute_gaps(
    int *fences, int fences_len,
    int max_coordinate,
    char *gaps
) {
    int size = fences_len + 2;
    int *points = malloc(size * sizeof(int));

    points[0] = 1;
    points[1] = max_coordinate;
    for (int i = 0; i < fences_len; i++) {
        points[i + 2] = fences[i];
    }

    qsort(points, size, sizeof(int), cmp_int);

    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            gaps[points[j] - points[i]] = 1;
        }
    }

    free(points);
}

int maximizeSquareArea(
    int m, int n,
    int *hFences, int hLen,
    int *vFences, int vLen
) {
    const int MOD = 1000000007;

    char *hGaps = calloc(m + 1, sizeof(char));
    char *vGaps = calloc(n + 1, sizeof(char));

    compute_gaps(hFences, hLen, m, hGaps);
    compute_gaps(vFences, vLen, n, vGaps);

    int max_side = 0;
    int limit = m < n ? m : n;

    for (int d = 1; d <= limit; d++) {
        if (hGaps[d] && vGaps[d]) {
            if (d > max_side) max_side = d;
        }
    }

    free(hGaps);
    free(vGaps);

    if (max_side == 0) return -1;
    return (int)((1LL * max_side * max_side) % MOD);
}
