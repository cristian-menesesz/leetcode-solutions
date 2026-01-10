pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
    if s1.len() < s2.len() {
        return minimum_delete_sum(s2, s1);
    }

    let a = s1.as_bytes();
    let b = s2.as_bytes();

    let len_a = a.len();
    let len_b = b.len();

    let mut dp = vec![vec![0i32; len_b + 1]; 2];

    for i in 0..len_a {
        let curr = (i + 1) & 1;
        let prev = curr ^ 1;

        for j in 0..len_b {
            if a[i] == b[j] {
                dp[curr][j + 1] = a[i] as i32 + dp[prev][j];
            } else {
                dp[curr][j + 1] = dp[prev][j + 1].max(dp[curr][j]);
            }
        }
    }

    let total: i32 = a.iter().map(|&c| c as i32).sum::<i32>()
        + b.iter().map(|&c| c as i32).sum::<i32>();

    let max_common = dp[len_a & 1][len_b];
    total - 2 * max_common
}
