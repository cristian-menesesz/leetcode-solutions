fn construct_transformed_array(nums: &Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut result = vec![0; n];

    for i in 0..n {
        let j = ((i as i32 + nums[i]) % n as i32) as usize;
        result[i] = nums[j];
    }

    result
}
