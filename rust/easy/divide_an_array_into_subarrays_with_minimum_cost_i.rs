fn minimum_cost(nums: &[i32]) -> i32 {
    let first = nums[0];
    let mut min1 = i32::MAX;
    let mut min2 = i32::MAX;

    for &x in &nums[1..] {
        if x < min1 {
            min2 = min1;
            min1 = x;
        } else if x < min2 {
            min2 = x;
        }
    }

    first + min1 + min2
}
