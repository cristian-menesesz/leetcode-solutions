#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAXN 400
#define INF 1000000000000000000LL

long long minll(long long a, long long b) {
    return a < b ? a : b;
}

int find_id(char table[][64], int size, const char *s) {
    for (int i = 0; i < size; i++) {
        if (strcmp(table[i], s) == 0) return i;
    }
    return -1;
}

long long minimumCost(
    const char *source,
    const char *target,
    char original[][64],
    char changed[][64],
    long long cost[],
    int m
) {
    int n = strlen(source);

    char string_table[MAXN][64];
    int valid_len[MAXN];
    int valid_len_cnt = 0;

    int next_id = 0;
    long long dist[MAXN][MAXN];

    for (int i = 0; i < MAXN; i++)
        for (int j = 0; j < MAXN; j++)
            dist[i][j] = INF;

    for (int i = 0; i < m; i++) {
        int u = find_id(string_table, next_id, original[i]);
        if (u == -1) {
            strcpy(string_table[next_id], original[i]);
            valid_len[valid_len_cnt++] = strlen(original[i]);
            u = next_id++;
        }

        int v = find_id(string_table, next_id, changed[i]);
        if (v == -1) {
            strcpy(string_table[next_id], changed[i]);
            v = next_id++;
        }

        dist[u][v] = minll(dist[u][v], cost[i]);
    }

    for (int i = 0; i < next_id; i++)
        dist[i][i] = 0;

    // Floyd–Warshall
    for (int k = 0; k < next_id; k++)
        for (int i = 0; i < next_id; i++)
            if (dist[i][k] < INF)
                for (int j = 0; j < next_id; j++)
                    if (dist[k][j] < INF)
                        dist[i][j] = minll(dist[i][j], dist[i][k] + dist[k][j]);

    long long dp[n + 1];
    for (int i = 0; i <= n; i++) dp[i] = INF;
    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        if (dp[i] == INF) continue;

        if (source[i] == target[i])
            dp[i + 1] = minll(dp[i + 1], dp[i]);

        for (int k = 0; k < valid_len_cnt; k++) {
            int len = valid_len[k];
            if (i + len > n) continue;

            char s1[64], s2[64];
            strncpy(s1, source + i, len); s1[len] = 0;
            strncpy(s2, target + i, len); s2[len] = 0;

            int u = find_id(string_table, next_id, s1);
            int v = find_id(string_table, next_id, s2);
            if (u != -1 && v != -1 && dist[u][v] < INF)
                dp[i + len] = minll(dp[i + len], dp[i] + dist[u][v]);
        }
    }

    return dp[n] == INF ? -1 : dp[n];
}
