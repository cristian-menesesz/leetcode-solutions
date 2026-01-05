#include <stdlib.h>
#include <limits.h>

long long maxMatrixSum(int** matrix, int rows, int cols) {
    
    long long total_sum = 0;
    int min_abs = INT_MAX;
    int negative_count = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            int value = matrix[i][j];
            int abs_val = abs(value);

            total_sum += abs_val;

            if (abs_val < min_abs) {
                min_abs = abs_val;
            }

            if (value < 0) {
                negative_count++;
            }
        }
    }

    if (negative_count % 2 == 0) {
        return total_sum;
    } else {
        return total_sum - 2LL * min_abs;
    }
}
