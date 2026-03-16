using System;
using System.Collections.Generic;

public class Solution
{
    const int OFFSET = 50;

    public IList<int> GetBiggestThree(int[][] grid)
    {
        int rows = grid.Length;
        int cols = grid[0].Length;

        int[][] diagPrefix = new int[100][];
        int[][] antiPrefix = new int[100][];

        for (int i = 0; i < 100; i++)
        {
            diagPrefix[i] = new int[cols + 1];
            antiPrefix[i] = new int[rows + 1];
        }

        // build diagonal prefix sums
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                int diagIdx = r - c + OFFSET;
                int antiIdx = r + c;
                int val = grid[r][c];

                diagPrefix[diagIdx][c + 1] = diagPrefix[diagIdx][c] + val;
                antiPrefix[antiIdx][r + 1] = antiPrefix[antiIdx][r] + val;
            }
        }

        int RhombusSum(int r, int c, int d)
        {
            if (d == 0)
                return grid[r][c];

            int left = c - d, right = c + d;
            int top = r - d, bottom = r + d;

            int diag0 = top - c + OFFSET;
            int diag1 = r - left + OFFSET;

            int total = diagPrefix[diag0][right + 1] - diagPrefix[diag0][c];
            total += diagPrefix[diag1][c + 1] - diagPrefix[diag1][left];

            int anti0 = top + c;
            int anti1 = bottom + c;

            total += antiPrefix[anti0][r] - antiPrefix[anti0][top + 1];
            total += antiPrefix[anti1][bottom] - antiPrefix[anti1][r + 1];

            return total;
        }

        int[] best = { -1, -1, -1 };
        int maxRadius = Math.Min(rows, cols) / 2;

        for (int d = 0; d <= maxRadius; d++)
        {
            for (int r = d; r < rows - d; r++)
            {
                for (int c = d; c < cols - d; c++)
                {
                    int val = RhombusSum(r, c, d);

                    if (val == best[0] || val == best[1] || val == best[2])
                        continue;

                    if (val > best[0])
                    {
                        best[2] = best[1];
                        best[1] = best[0];
                        best[0] = val;
                    }
                    else if (val > best[1])
                    {
                        best[2] = best[1];
                        best[1] = val;
                    }
                    else if (val > best[2])
                    {
                        best[2] = val;
                    }
                }
            }
        }

        List<int> result = new();
        foreach (int x in best)
            if (x != -1)
                result.Add(x);

        return result;
    }
}