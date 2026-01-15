#include <stdlib.h>

int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int longest_consecutive_run(int *bars, int size) {
    if (size == 0) return 0;

    int max_run = 1;
    int current_run = 1;

    for (int i = 1; i < size; i++) {
        if (bars[i] == bars[i - 1] + 1) {
            current_run++;
        } else {
            if (current_run > max_run)
                max_run = current_run;
            current_run = 1;
        }
    }

    return current_run > max_run ? current_run : max_run;
}

int maximizeSquareHoleArea(int n, int m, int *hBars, int hSize, int *vBars, int vSize) {
    qsort(hBars, hSize, sizeof(int), cmp_int);
    qsort(vBars, vSize, sizeof(int), cmp_int);

    int max_horizontal_run = longest_consecutive_run(hBars, hSize);
    int max_vertical_run = longest_consecutive_run(vBars, vSize);

    int max_square_side = (max_horizontal_run < max_vertical_run
                           ? max_horizontal_run
                           : max_vertical_run) + 1;

    return max_square_side * max_square_side;
}
