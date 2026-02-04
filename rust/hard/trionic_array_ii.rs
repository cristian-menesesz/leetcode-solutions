pub fn max_trionic_subarray_sum(nums: Vec<i32>) -> i64 {
    let neg_inf: i64 = -(1i64 << 50);

    let mut inc1 = neg_inf;
    let mut dec  = neg_inf;
    let mut inc2 = neg_inf;
    let mut best = neg_inf;

    let mut prev = nums[0];

    for &curr in nums.iter().skip(1) {
        let mut next_inc1 = neg_inf;
        let mut next_dec  = neg_inf;
        let mut next_inc2 = neg_inf;

        if curr > prev {
            next_inc1 = std::cmp::max(inc1, prev as i64) + curr as i64;
            next_inc2 = std::cmp::max(dec, inc2) + curr as i64;
        } else if curr < prev {
            next_dec = std::cmp::max(inc1, dec) + curr as i64;
        }

        inc1 = next_inc1;
        dec  = next_dec;
        inc2 = next_inc2;

        best = std::cmp::max(best, inc2);
        prev = curr;
    }

    best
}
