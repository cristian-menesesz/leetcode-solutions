class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int[] colX = new int[cols];
        int[] colY = new int[cols];

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

        return result;
    }
}