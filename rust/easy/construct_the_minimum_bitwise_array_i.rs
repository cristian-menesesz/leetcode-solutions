pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
    let mut result = Vec::with_capacity(nums.len());

    for target in nums {
        if target & 1 == 0 {
            result.push(-1);
            continue;
        }

        let lowest_changed_bit = ((target + 1) & !target) >> 1;
        let minimal_candidate = target & !lowest_changed_bit;
        result.push(minimal_candidate);
    }

    result
}
