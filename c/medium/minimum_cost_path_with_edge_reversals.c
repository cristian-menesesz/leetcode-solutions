#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAXN 100000
#define MAXE 200000

typedef struct {
    int to;
    int cost;
} Edge;

typedef struct {
    int node;
    int dist;
} HeapNode;

Edge adj[MAXE];
int head[MAXN], next[MAXE], edge_cnt = 0;

void add_edge(int u, int v, int w) {
    adj[edge_cnt] = (Edge){v, w};
    next[edge_cnt] = head[u];
    head[u] = edge_cnt++;
}

void swap(HeapNode *a, HeapNode *b) {
    HeapNode t = *a;
    *a = *b;
    *b = t;
}

void heap_push(HeapNode *heap, int *size, HeapNode val) {
    heap[(*size)++] = val;
    for (int i = *size - 1; i > 0; ) {
        int p = (i - 1) / 2;
        if (heap[p].dist <= heap[i].dist) break;
        swap(&heap[p], &heap[i]);
        i = p;
    }
}

HeapNode heap_pop(HeapNode *heap, int *size) {
    HeapNode root = heap[0];
    heap[0] = heap[--(*size)];

    for (int i = 0;;) {
        int l = 2*i + 1, r = 2*i + 2, s = i;
        if (l < *size && heap[l].dist < heap[s].dist) s = l;
        if (r < *size && heap[r].dist < heap[s].dist) s = r;
        if (s == i) break;
        swap(&heap[i], &heap[s]);
        i = s;
    }
    return root;
}

int minCost(int n, int edges[][3], int m) {
    for (int i = 0; i < n; i++) head[i] = -1;

    for (int i = 0; i < m; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        add_edge(u, v, w);
        add_edge(v, u, w << 1);
    }

    int dist[n];
    for (int i = 0; i < n; i++) dist[i] = INT_MAX;
    dist[0] = 0;

    HeapNode heap[MAXE];
    int size = 0;
    heap_push(heap, &size, (HeapNode){0, 0});

    while (size) {
        HeapNode cur = heap_pop(heap, &size);
        if (cur.dist > dist[cur.node]) continue;
        if (cur.node == n - 1) return cur.dist;

        for (int e = head[cur.node]; e != -1; e = next[e]) {
            int nd = cur.dist + adj[e].cost;
            int v = adj[e].to;
            if (nd < dist[v]) {
                dist[v] = nd;
                heap_push(heap, &size, (HeapNode){v, nd});
            }
        }
    }
    return -1;
}
