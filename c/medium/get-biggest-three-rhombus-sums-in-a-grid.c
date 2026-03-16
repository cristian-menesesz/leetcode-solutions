#include <stdio.h>

#define OFFSET 50
#define MAXN 50
#define MAXD 100

static int diag_prefix[MAXD][MAXN + 1];
static int anti_prefix[MAXD][MAXN + 1];

static inline int rhombus_sum(
    int r, int c, int d,
    int grid[MAXN][MAXN]
) {
    if (d == 0)
        return grid[r][c];

    int left = c - d;
    int right = c + d;
    int top = r - d;
    int bottom = r + d;

    int total = 0;

    int diag0 = top - c + OFFSET;
    int diag1 = r - left + OFFSET;

    total += diag_prefix[diag0][right + 1] - diag_prefix[diag0][c];
    total += diag_prefix[diag1][c + 1] - diag_prefix[diag1][left];

    int anti0 = top + c;
    int anti1 = bottom + c;

    total += anti_prefix[anti0][r] - anti_prefix[anti0][top + 1];
    total += anti_prefix[anti1][bottom] - anti_prefix[anti1][r + 1];

    return total;
}

int getBiggestThree(
    int grid[MAXN][MAXN],
    int rows,
    int cols,
    int result[3]
) {

    for (int i = 0; i < MAXD; i++)
        for (int j = 0; j <= MAXN; j++)
            diag_prefix[i][j] = anti_prefix[i][j] = 0;

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {

            int val = grid[r][c];

            int diag_idx = r - c + OFFSET;
            int anti_idx = r + c;

            diag_prefix[diag_idx][c + 1] =
                diag_prefix[diag_idx][c] + val;

            anti_prefix[anti_idx][r + 1] =
                anti_prefix[anti_idx][r] + val;
        }
    }

    int best[3] = {-1, -1, -1};
    int max_radius = (rows < cols ? rows : cols) / 2;

    for (int d = 0; d <= max_radius; d++) {
        for (int r = d; r < rows - d; r++) {
            for (int c = d; c < cols - d; c++) {

                int val = rhombus_sum(r, c, d, grid);

                if (val == best[0] || val == best[1] || val == best[2])
                    continue;

                if (val > best[0]) {
                    best[2] = best[1];
                    best[1] = best[0];
                    best[0] = val;
                }
                else if (val > best[1]) {
                    best[2] = best[1];
                    best[1] = val;
                }
                else if (val > best[2]) {
                    best[2] = val;
                }
            }
        }
    }

    int k = 0;
    for (int i = 0; i < 3; i++)
        if (best[i] != -1)
            result[k++] = best[i];

    return k;
}