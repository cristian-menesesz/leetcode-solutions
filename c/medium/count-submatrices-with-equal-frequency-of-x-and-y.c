#include <stdlib.h>

int numberOfSubmatrices(char** grid, int rows, int cols) {
    int* colX = calloc(cols, sizeof(int));
    int* colY = calloc(cols, sizeof(int));
    int result = 0;

    for (int r = 0; r < rows; r++) {
        int rowX = 0, rowY = 0;

        for (int c = 0; c < cols; c++) {
            char cell = grid[r][c];

            if (cell == 'X') {
                rowX++;
            } else if (cell == 'Y') {
                rowY++;
            }

            colX[c] += rowX;
            colY[c] += rowY;

            if (colX[c] > 0 && colX[c] == colY[c]) {
                result++;
            }
        }
    }

    free(colX);
    free(colY);
    return result;
}