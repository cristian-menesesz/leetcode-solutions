#include <stdio.h>
#include <stdlib.h>

static int cups_until_half(int row) {
    return (row * row + 2 * row + (row % 2)) / 4;
}

static double overflow(double x) {
    return x > 1.0 ? x - 1.0 : 0.0;
}

double champagneTower(int poured, int query_row, int query_glass) {
    if (poured == 0) return 0.0;

    int col = query_glass < (query_row - query_glass) ?
              query_glass : (query_row - query_glass);

    int total_cups = cups_until_half(query_row) + col + 1;
    double *cups = calloc(total_cups, sizeof(double));

    cups[0] = (double)poured;
    int prev_row_start = 0;

    // build rows up to query_row - 1
    for (int r = 1; r < query_row; r++) {
        int row_start = cups_until_half(r);

        // left edge
        cups[row_start] = overflow(cups[prev_row_start]) / 2.0;

        // middle
        for (int j = 1; j < (r + 1) / 2; j++) {
            cups[row_start + j] =
                (overflow(cups[prev_row_start + j - 1]) +
                 overflow(cups[prev_row_start + j])) / 2.0;
        }

        // center when even width
        if (r % 2 == 0) {
            cups[row_start + r / 2] =
                overflow(cups[prev_row_start + r / 2 - 1]);
        }

        prev_row_start = row_start;
    }

    // final row partial
    int final_row_start = cups_until_half(query_row);

    if (query_row > 0) {
        cups[final_row_start] = overflow(cups[prev_row_start]) / 2.0;

        for (int j = 1; j < col; j++) {
            cups[final_row_start + j] =
                (overflow(cups[prev_row_start + j - 1]) +
                 overflow(cups[prev_row_start + j])) / 2.0;
        }
    }

    double result;

    if (col == 0)
        result = cups[final_row_start];
    else if (col * 2 == query_row)
        result = overflow(cups[prev_row_start + col - 1]);
    else
        result =
            (overflow(cups[prev_row_start + col - 1]) +
             overflow(cups[prev_row_start + col])) / 2.0;

    free(cups);
    return result > 1.0 ? 1.0 : result;
}


// beats 99.76%

#include <stdio.h>
#include <stdlib.h>

double champagneTower(int poured, int query_row, int query_glass) {

    int target_col = query_glass < (query_row - query_glass)
                     ? query_glass
                     : (query_row - query_glass);

    double *flow = (double*)calloc(target_col + 1, sizeof(double));
    flow[0] = (double)poured;

    int max_left_reach = query_row - target_col + 1;
    int dry_cutoff = -1;

    for (int row = 0; row < query_row; row++) {

        int center = row >> 1;
        int row_is_odd;

        if (center >= target_col) {
            center = target_col;
            row_is_odd = 0;
        } else {
            row_is_odd = row & 1;
        }

        double overflow = flow[center] - 1.0;
        if (overflow < 0.0) overflow = 0.0;

        if (overflow == 0.0) {
            free(flow);
            return 0.0;
        }

        if (row_is_odd)
            flow[center + 1] += overflow;

        flow[center] = overflow * 0.5;

        for (int col = center - 1; col > (row - max_left_reach) && col > dry_cutoff; col--) {

            double spill = flow[col] - 1.0;
            if (spill < 0.0) spill = 0.0;
            spill *= 0.5;

            if (spill == 0.0) {
                dry_cutoff = col;
                break;
            }

            flow[col + 1] += spill;
            flow[col] = spill;
        }
    }

    double result = flow[target_col] < 1.0 ? flow[target_col] : 1.0;
    free(flow);
    return result;
}
