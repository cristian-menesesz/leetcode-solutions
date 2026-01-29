#include <stdio.h>
#include <string.h>
#include <limits.h>

#define ALPHABET_SIZE 26
#define INF 1000000000000000000LL

long long minimumCost(
    const char *source,
    const char *target,
    const char *original,
    const char *changed,
    const int *cost,
    int rulesCount
) {
    long long distance[ALPHABET_SIZE][ALPHABET_SIZE];
    long long total_cost = 0;

    // Initialize distances
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        for (int j = 0; j < ALPHABET_SIZE; j++) {
            distance[i][j] = INF;
        }
        distance[i][i] = 0;
    }

    for (int i = 0; i < rulesCount; i++) {
        int src = original[i] - 'a';
        int dst = changed[i] - 'a';
        if (cost[i] < distance[src][dst]) {
            distance[src][dst] = cost[i];
        }
    }

    for (int mid = 0; mid < ALPHABET_SIZE; mid++) {
        for (int start = 0; start < ALPHABET_SIZE; start++) {
            if (distance[start][mid] == INF) continue;
            for (int end = 0; end < ALPHABET_SIZE; end++) {
                long long new_cost = distance[start][mid] + distance[mid][end];
                if (new_cost < distance[start][end]) {
                    distance[start][end] = new_cost;
                }
            }
        }
    }

    int n = strlen(source);
    for (int i = 0; i < n; i++) {
        int s = source[i] - 'a';
        int t = target[i] - 'a';
        if (distance[s][t] == INF) {
            return -1;
        }
        total_cost += distance[s][t];
    }

    return total_cost;
}
