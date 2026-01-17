#include <stdio.h>

int largestSquareArea(
    int bottomLeft[][2],
    int topRight[][2],
    int rectangle_count
) {
    int max_square_side = 0;

    for (int i = 0; i < rectangle_count - 1; i++) {
        int x1_i = bottomLeft[i][0];
        int y1_i = bottomLeft[i][1];
        int x2_i = topRight[i][0];
        int y2_i = topRight[i][1];

        for (int j = i + 1; j < rectangle_count; j++) {
            int x1_j = bottomLeft[j][0];
            int y1_j = bottomLeft[j][1];
            int x2_j = topRight[j][0];
            int y2_j = topRight[j][1];

            int intersection_width =
                (x2_i < x2_j ? x2_i : x2_j) -
                (x1_i > x1_j ? x1_i : x1_j);

            int intersection_height =
                (y2_i < y2_j ? y2_i : y2_j) -
                (y1_i > y1_j ? y1_i : y1_j);

            if (intersection_width <= 0 || intersection_height <= 0)
                continue;

            int square_side =
                intersection_width < intersection_height
                    ? intersection_width
                    : intersection_height;

            if (square_side > max_square_side)
                max_square_side = square_side;
        }
    }

    return max_square_side * max_square_side;
}
