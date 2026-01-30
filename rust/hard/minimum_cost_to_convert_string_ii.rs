use std::collections::{HashMap, HashSet};

pub fn minimum_cost(
    source: &str,
    target: &str,
    original: Vec<String>,
    changed: Vec<String>,
    cost: Vec<i64>,
) -> i64 {
    const INF: i64 = 1_000_000_000_000_000_000;
    let n = source.len();
    let m = original.len();

    let mut id: HashMap<String, usize> = HashMap::new();
    let mut valid_len: HashSet<usize> = HashSet::new();
    let mut next_id = 0;

    let max_nodes = 2 * m;
    let mut dist = vec![vec![INF; max_nodes]; max_nodes];

    for i in 0..m {
        let u = *id.entry(original[i].clone())
            .or_insert_with(|| {
                valid_len.insert(original[i].len());
                let v = next_id;
                next_id += 1;
                v
            });

        let v = *id.entry(changed[i].clone())
            .or_insert_with(|| {
                let v = next_id;
                next_id += 1;
                v
            });

        dist[u][v] = dist[u][v].min(cost[i]);
    }

    for i in 0..next_id {
        dist[i][i] = 0;
    }

    // Floyd–Warshall
    for k in 0..next_id {
        for i in 0..next_id {
            if dist[i][k] == INF { continue; }
            for j in 0..next_id {
                dist[i][j] = dist[i][j].min(dist[i][k] + dist[k][j]);
            }
        }
    }

    let mut dp = vec![INF; n + 1];
    dp[0] = 0;

    for i in 0..n {
        if dp[i] == INF { continue; }

        if source.as_bytes()[i] == target.as_bytes()[i] {
            dp[i + 1] = dp[i + 1].min(dp[i]);
        }

        for &len in &valid_len {
            if i + len > n { continue; }
            let s1 = &source[i..i + len];
            let s2 = &target[i..i + len];
            if let (Some(&u), Some(&v)) = (id.get(s1), id.get(s2)) {
                if dist[u][v] < INF {
                    dp[i + len] = dp[i + len].min(dp[i] + dist[u][v]);
                }
            }
        }
    }

    if dp[n] == INF { -1 } else { dp[n] }
}
