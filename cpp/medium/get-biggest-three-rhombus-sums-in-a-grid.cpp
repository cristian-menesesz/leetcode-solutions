#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    static const int OFFSET = 50;

public:
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        vector<vector<int>> diagPrefix(100, vector<int>(cols + 1));
        vector<vector<int>> antiPrefix(100, vector<int>(rows + 1));

        // build diagonal prefix sums
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int diagIdx = r - c + OFFSET;
                int antiIdx = r + c;
                int val = grid[r][c];

                diagPrefix[diagIdx][c + 1] = diagPrefix[diagIdx][c] + val;
                antiPrefix[antiIdx][r + 1] = antiPrefix[antiIdx][r] + val;
            }
        }

        auto rhombusSum = [&](int r, int c, int d) {
            if (d == 0) return grid[r][c];

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
        };

        int best[3] = {-1, -1, -1};
        int maxRadius = min(rows, cols) / 2;

        for (int d = 0; d <= maxRadius; d++) {
            for (int r = d; r < rows - d; r++) {
                for (int c = d; c < cols - d; c++) {
                    int val = rhombusSum(r, c, d);

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

        vector<int> result;
        for (int x : best)
            if (x != -1) result.push_back(x);

        return result;
    }
};