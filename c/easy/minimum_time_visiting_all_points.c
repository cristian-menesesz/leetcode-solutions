#include <stdlib.h>

int minTimeToVisitAllPoints(int points[][2], int n) {
    int total_time = 0;

    for (int i = 0; i < n - 1; i++) {
        int x1 = points[i][0];
        int y1 = points[i][1];
        int x2 = points[i + 1][0];
        int y2 = points[i + 1][1];

        int dx = abs(x2 - x1);
        int dy = abs(y2 - y1);

        total_time += (dx > dy) ? dx : dy;
    }

    return total_time;
}
