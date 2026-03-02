#include <stdio.h>
#include <stdlib.h>

int minSwaps(int** grid, int n) {
    int* trailingZeros = (int*)malloc(sizeof(int) * n);

    // Count trailing zeros per row
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (grid[i][j] == 0)
                count++;
            else
                break;
        }
        trailingZeros[i] = count;
    }

    int swapCount = 0;
    int currentSize = n;

    for (int targetRow = 0; targetRow < n; targetRow++) {
        int minRequiredZeros = n - 1 - targetRow;
        int candidateRow = -1;

        // find first valid row
        for (int i = 0; i < currentSize; i++) {
            if (trailingZeros[i] >= minRequiredZeros) {
                candidateRow = i;
                break;
            }
        }

        if (candidateRow == -1) {
            free(trailingZeros);
            return -1;
        }

        swapCount += candidateRow;

        // remove element (shift left)
        for (int i = candidateRow; i < currentSize - 1; i++) {
            trailingZeros[i] = trailingZeros[i + 1];
        }

        currentSize--;
    }

    free(trailingZeros);
    return swapCount;
}