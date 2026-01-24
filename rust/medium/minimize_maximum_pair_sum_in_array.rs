pub fn min_pair_sum(nums: Vec<i32>) -> i32 {
    const MAX_VALUE: usize = 100_000;
    let mut frequency = vec![0; MAX_VALUE + 1];

    let mut min_value = MAX_VALUE;
    let mut max_value = 0;

    for &num in &nums {
        let n = num as usize;
        frequency[n] += 1;
        min_value = min_value.min(n);
        max_value = max_value.max(n);
    }

    let pairs_needed = nums.len() / 2;
    let mut smallest_used = 0;
    let mut largest_used = 0;

    let mut left = min_value;
    let mut right = max_value;
    let mut worst_pair_sum = 0;

    for pair_number in 1..=pairs_needed {

        while smallest_used < pair_number {
            smallest_used += frequency[left];
            left += 1;
        }

        while largest_used < pair_number {
            largest_used += frequency[right];
            right -= 1;
        }

        worst_pair_sum = worst_pair_sum.max((left + right) as i32);
    }

    worst_pair_sum
}
