class Solution {

    private static final int OFFSET = 50;

    public int[] getBiggestThree(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;

        int[][] diag = new int[100][cols + 1];
        int[][] anti = new int[100][rows + 1];

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {

                int val = grid[r][c];
                int diagIdx = r - c + OFFSET;
                int antiIdx = r + c;

                diag[diagIdx][c + 1] = diag[diagIdx][c] + val;
                anti[antiIdx][r + 1] = anti[antiIdx][r] + val;
            }
        }

        int[] best = {-1, -1, -1};
        int maxRadius = Math.min(rows, cols) / 2;

        for (int d = 0; d <= maxRadius; d++) {
            for (int r = d; r < rows - d; r++) {
                for (int c = d; c < cols - d; c++) {

                    int val = rhombusSum(r, c, d, grid, diag, anti);

                    if (val == best[0] || val == best[1] || val == best[2])
                        continue;

                    if (val > best[0]) {
                        best[2] = best[1];
                        best[1] = best[0];
                        best[0] = val;
                    } else if (val > best[1]) {
                        best[2] = best[1];
                        best[1] = val;
                    } else if (val > best[2]) {
                        best[2] = val;
                    }
                }
            }
        }

        return java.util.Arrays.stream(best).filter(x -> x != -1).toArray();
    }

    private int rhombusSum(int r, int c, int d, int[][] grid, int[][] diag, int[][] anti) {

        if (d == 0)
            return grid[r][c];

        int left = c - d, right = c + d;
        int top = r - d, bottom = r + d;

        int diag0 = top - c + OFFSET;
        int diag1 = r - left + OFFSET;

        int total = diag[diag0][right + 1] - diag[diag0][c];
        total += diag[diag1][c + 1] - diag[diag1][left];

        int anti0 = top + c;
        int anti1 = bottom + c;

        total += anti[anti0][r] - anti[anti0][top + 1];
        total += anti[anti1][bottom] - anti[anti1][r + 1];

        return total;
    }
}