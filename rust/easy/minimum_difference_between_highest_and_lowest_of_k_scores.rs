pub fn minimum_difference(mut nums: Vec<i32>, k: usize) -> i32 {
    if k == 1 {
        return 0;
    }

    let k = k as usize;

    nums.sort();

    let mut min_difference = i32::MAX;

    for left in 0..=nums.len() - k {
        let right = left + k - 1;
        let current_difference = nums[right] - nums[left];
        min_difference = min_difference.min(current_difference);
    }

    min_difference
}
