#include <stdbool.h>

#define MAX 51

int largestMagicSquare(int grid[MAX][MAX], int rows, int cols) {
    int row_prefix[MAX+1][MAX+1] = {0};
    int col_prefix[MAX+1][MAX+1] = {0};
    int diag_prefix[MAX+1][MAX+1] = {0};
    int anti_diag_prefix[MAX+1][MAX+1] = {0};

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            int v = grid[i][j];
            row_prefix[i+1][j+1] = row_prefix[i+1][j] + v;
            col_prefix[i+1][j+1] = col_prefix[i][j+1] + v;
            diag_prefix[i+1][j+1] = diag_prefix[i][j] + v;
            anti_diag_prefix[i+1][j] = anti_diag_prefix[i][j+1] + v;
        }
    }

    for (int size = rows < cols ? rows : cols; size > 1; size--) {
        for (int top = 0; top <= rows - size; top++) {
            for (int left = 0; left <= cols - size; left++) {
                int main_diag =
                    diag_prefix[top+size][left+size] - diag_prefix[top][left];
                int anti_diag =
                    anti_diag_prefix[top+size][left] - anti_diag_prefix[top][left+size];

                if (main_diag != anti_diag) continue;

                bool valid = true;
                for (int k = 0; k < size; k++) {
                    int row_sum =
                        row_prefix[top+k+1][left+size] - row_prefix[top+k+1][left];
                    int col_sum =
                        col_prefix[top+size][left+k+1] - col_prefix[top][left+k+1];

                    if (row_sum != main_diag || col_sum != main_diag) {
                        valid = false;
                        break;
                    }
                }

                if (valid) return size;
            }
        }
    }
    return 1;
}
