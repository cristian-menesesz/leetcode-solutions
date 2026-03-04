#include <stdbool.h>

int numSpecial(int** matrix, int rows, int cols) {
    int special_count = 0;

    // marks columns already processed
    bool* column_checked = (bool*)calloc(cols, sizeof(bool));

    for (int r = 0; r < rows; r++) {
        int one_count = 0;
        int col_index = -1;

        // count ones in row
        for (int c = 0; c < cols; c++) {
            if (matrix[r][c] == 1) {
                one_count++;
                col_index = c;
            }
        }

        // Case 1: exactly one '1'
        if (one_count == 1) {
            if (!column_checked[col_index]) {
                column_checked[col_index] = true;

                int column_sum = 0;
                for (int rr = 0; rr < rows; rr++) {
                    column_sum += matrix[rr][col_index];
                }

                if (column_sum == 1)
                    special_count++;
            }
        }
        // Case 2: multiple ones → invalidate columns
        else if (one_count > 1) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == 1)
                    column_checked[c] = true;
            }
        }
    }

    free(column_checked);
    return special_count;
}