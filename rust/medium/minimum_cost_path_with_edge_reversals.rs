use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn min_cost(n: usize, edges: Vec<Vec<i32>>) -> i32 {
    let mut adj = vec![Vec::new(); n];

    for e in edges {
        let (u, v, w) = (e[0] as usize, e[1] as usize, e[2]);
        adj[u].push((w, v));
        adj[v].push((w << 1, u));
    }

    let mut dist = vec![i32::MAX; n];
    let mut heap = BinaryHeap::new();

    dist[0] = 0;
    heap.push(Reverse((0, 0)));

    while let Some(Reverse((cost, u))) = heap.pop() {
        if cost > dist[u] { continue; }
        if u == n - 1 { return cost; }

        for &(w, v) in &adj[u] {
            let nc = cost + w;
            if nc < dist[v] {
                dist[v] = nc;
                heap.push(Reverse((nc, v)));
            }
        }
    }
    -1
}
