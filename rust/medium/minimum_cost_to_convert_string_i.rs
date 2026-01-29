pub fn minimum_cost(
    source: &str,
    target: &str,
    original: &[char],
    changed: &[char],
    cost: &[i32],
) -> i64 {
    const ALPHABET_SIZE: usize = 26;
    const INF: i64 = 1_000_000_000_000_000_000;

    let mut distance = vec![vec![INF; ALPHABET_SIZE]; ALPHABET_SIZE];

    for i in 0..ALPHABET_SIZE {
        distance[i][i] = 0;
    }

    for i in 0..original.len() {
        let src = (original[i] as u8 - b'a') as usize;
        let dst = (changed[i] as u8 - b'a') as usize;
        distance[src][dst] = distance[src][dst].min(cost[i] as i64);
    }

    for mid in 0..ALPHABET_SIZE {
        for start in 0..ALPHABET_SIZE {
            if distance[start][mid] == INF {
                continue;
            }
            for end in 0..ALPHABET_SIZE {
                let new_cost = distance[start][mid] + distance[mid][end];
                if new_cost < distance[start][end] {
                    distance[start][end] = new_cost;
                }
            }
        }
    }

    let mut total_cost: i64 = 0;
    for (s_char, t_char) in source.chars().zip(target.chars()) {
        let s = (s_char as u8 - b'a') as usize;
        let t = (t_char as u8 - b'a') as usize;
        if distance[s][t] == INF {
            return -1;
        }
        total_cost += distance[s][t];
    }

    total_cost
}
