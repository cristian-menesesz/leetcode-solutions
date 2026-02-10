pub fn longest_balanced(nums: &[i32]) -> i32 {
    let n = nums.len();
    let max_val = *nums.iter().max().unwrap() as usize;

    let mut last_seen = vec![0usize; max_val + 1];
    let mut max_length = 0usize;

    for start in 0..n {
        if n - start <= max_length {
            break;
        }

        let mut distinct_counts = [0usize; 2];

        for end in start..n {
            let value = nums[end] as usize;

            if last_seen[value] != start + 1 {
                last_seen[value] = start + 1;
                let parity = value & 1;
                distinct_counts[parity] += 1;
            }

            if distinct_counts[0] == distinct_counts[1] {
                max_length = max_length.max(end - start + 1);
            }
        }
    }

    max_length as i32
}
