#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int numberOfSubmatrices(const vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        vector<int> colX(cols, 0);
        vector<int> colY(cols, 0);

        int result = 0;

        for (int r = 0; r < rows; ++r) {
            int rowX = 0, rowY = 0;

            for (int c = 0; c < cols; ++c) {
                char cell = grid[r][c];

                if (cell == 'X') ++rowX;
                else if (cell == 'Y') ++rowY;

                colX[c] += rowX;
                colY[c] += rowY;

                if (colX[c] > 0 && colX[c] == colY[c]) {
                    ++result;
                }
            }
        }

        return result;
    }
};