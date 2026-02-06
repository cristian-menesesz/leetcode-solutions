fn min_removal(mut nums: Vec<i32>, k: i32) -> i32 {
    nums.sort();
    let n = nums.len();

    if (nums[0] as i64) * (k as i64) >= nums[n - 1] as i64 {
        return 0;
    }

    let mut min_removals = n as i32;
    let mut left = 0usize;

    for right in 0..n {
        while left < right && (nums[left] as i64) * (k as i64) < nums[right] as i64 {
            left += 1;
        }

        let window_size = (right - left + 1) as i32;
        min_removals = min_removals.min(n as i32 - window_size);
    }

    min_removals
}
