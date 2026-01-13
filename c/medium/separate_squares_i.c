#include <math.h>
#include <float.h>

double area_above_y(int squares[][3], int n, double cut_y) {
    double total_area = 0.0;

    for (int i = 0; i < n; i++) {
        double bottom_y = squares[i][1];
        double side = squares[i][2];
        double top_y = bottom_y + side;

        if (cut_y >= top_y)
            continue;

        double visible_height = fmin(side, top_y - cut_y);
        total_area += side * visible_height;
    }

    return total_area;
}

double separateSquares(int squares[][3], int n) {
    double total_area = area_above_y(squares, n, -1e18);
    double half_area = total_area / 2.0;

    double min_y = DBL_MAX;
    double max_y = -DBL_MAX;

    for (int i = 0; i < n; i++) {
        double bottom_y = squares[i][1];
        double side = squares[i][2];
        if (bottom_y < min_y) min_y = bottom_y;
        if (bottom_y + side > max_y) max_y = bottom_y + side;
    }

    double left = min_y, right = max_y;
    double epsilon = 1e-5;

    while (right - left > epsilon) {
        double mid = (left + right) / 2.0;
        double area_above = area_above_y(squares, n, mid);

        if (area_above > half_area)
            left = mid;
        else
            right = mid;
    }

    return left;
}
