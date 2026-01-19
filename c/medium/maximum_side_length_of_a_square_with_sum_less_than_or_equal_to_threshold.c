#include <stdlib.h>

int submatrix_sum(int r0, int r1, int c0, int c1, int **prefix) {
    int total = prefix[r1][c1];

    if (r0 > 0) total -= prefix[r0 - 1][c1];
    if (c0 > 0) total -= prefix[r1][c0 - 1];
    if (r0 > 0 && c0 > 0) total += prefix[r0 - 1][c0 - 1];

    return total;
}

int max_square_from_diagonal(
    int start_row, int start_col,
    int rows, int cols,
    int **prefix,
    int threshold
) {
    int max_possible = (rows - start_row < cols - start_col)
                        ? rows - start_row
                        : cols - start_col;

    int best_length = 0;
    int left = 0;

    for (int right = 0; right < max_possible; right++) {
        int r0 = start_row + left;
        int r1 = start_row + right;
        int c0 = start_col + left;
        int c1 = start_col + right;

        int current_sum = submatrix_sum(r0, r1, c0, c1, prefix);

        while (left < right && current_sum > threshold) {
            left++;
            r0++;
            c0++;
            current_sum = submatrix_sum(r0, r1, c0, c1, prefix);
        }

        if (current_sum <= threshold) {
            int len = right - left + 1;
            if (len > best_length) best_length = len;
        }
    }

    return best_length;
}

int maxSideLength(int **mat, int rows, int cols, int threshold) {
    for (int j = 1; j < cols; j++)
        mat[0][j] += mat[0][j - 1];

    for (int i = 1; i < rows; i++) {
        mat[i][0] += mat[i - 1][0];
        for (int j = 1; j < cols; j++)
            mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1];
    }

    int max_side = 0;

    for (int i = 0; i < rows; i++) {
        if (rows - i <= max_side) break;
        int v = max_square_from_diagonal(i, 0, rows, cols, mat, threshold);
        if (v > max_side) max_side = v;
    }

    for (int j = 1; j < cols; j++) {
        if (cols - j <= max_side) break;
        int v = max_square_from_diagonal(0, j, rows, cols, mat, threshold);
        if (v > max_side) max_side = v;
    }

    return max_side;
}
