use std::collections::HashSet;

fn compute_gaps(fences: &[i32], max_coordinate: i32) -> HashSet<i32> {
    let mut points = Vec::with_capacity(fences.len() + 2);
    points.push(1);
    points.push(max_coordinate);
    points.extend_from_slice(fences);
    points.sort_unstable();

    let mut gaps = HashSet::new();
    for i in 0..points.len() {
        for j in i + 1..points.len() {
            gaps.insert(points[j] - points[i]);
        }
    }
    gaps
}

fn maximize_square_area(
    m: i32,
    n: i32,
    h_fences: &[i32],
    v_fences: &[i32],
) -> i64 {
    const MOD: i64 = 1_000_000_007;

    let h_gaps = compute_gaps(h_fences, m);
    let v_gaps = compute_gaps(v_fences, n);

    let max_side = h_gaps
        .intersection(&v_gaps)
        .copied()
        .max()
        .unwrap_or(0);

    if max_side == 0 {
        -1
    } else {
        ((max_side as i64 * max_side as i64) % MOD)
    }
}
