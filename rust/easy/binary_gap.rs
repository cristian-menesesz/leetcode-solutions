pub fn binary_gap(mut n: i32) -> i32 {

    // Remove trailing zeros so the first bit is 1
    n /= n & -n;

    if n == 1 {
        return 0;
    }

    let mut longest_distance = 0;
    let mut zeros_since_last_one = 0;

    while n != 0 {
        if (n & 1) == 1 {
            longest_distance =
                longest_distance.max(zeros_since_last_one);
            zeros_since_last_one = 0;
        } else {
            zeros_since_last_one += 1;
        }

        n >>= 1;
    }

    longest_distance + 1
}