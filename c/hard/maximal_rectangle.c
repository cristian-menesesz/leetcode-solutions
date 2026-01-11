#include <stdlib.h>
#include <string.h>

int find_max_rectangle_area(int* heights, int n) {
    if (n == 0) return 0;

    int* left = (int*)malloc(n * sizeof(int));
    int* right = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        left[i] = -1;
        right[i] = n;
    }

    for (int i = 1; i < n; i++) {
        int boundary = i - 1;
        while (boundary >= 0 && heights[boundary] >= heights[i]) {
            boundary = left[boundary];
        }
        left[i] = boundary;
    }

    int max_area = heights[n - 1] * (right[n - 1] - left[n - 1] - 1);

    for (int i = n - 2; i >= 0; i--) {
        int boundary = i + 1;
        while (boundary < n && heights[boundary] >= heights[i]) {
            boundary = right[boundary];
        }
        right[i] = boundary;

        int width = right[i] - left[i] - 1;
        int area = heights[i] * width;
        if (area > max_area) max_area = area;
    }

    free(left);
    free(right);
    return max_area;
}

int maximalRectangle(char*** matrix, int rows, int cols) {
    if (rows == 0 || cols == 0) return 0;

    int* heights = (int*)calloc(cols, sizeof(int));
    int max_area = 0;

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (matrix[r][c][0] == '0')
                heights[c] = 0;
            else
                heights[c]++;
        }

        int area = find_max_rectangle_area(heights, cols);
        if (area > max_area) max_area = area;
    }

    free(heights);
    return max_area;
}
