pub fn minimum_deletions(s: &str) -> i32 {
    let mut min_deletions = 0;
    let mut b_before_a = 0;

    for c in s.chars() {
        if c == 'b' {
            b_before_a += 1;
        } else if b_before_a > 0 {
            min_deletions += 1;
            b_before_a -= 1;
        }
    }

    min_deletions
}
