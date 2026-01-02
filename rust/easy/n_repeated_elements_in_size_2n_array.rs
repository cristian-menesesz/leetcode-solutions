use std::collections::HashSet;

pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
    
    let mut seen = HashSet::new();
    
    for &number in &nums {
        if !seen.insert(number) {
            return number;
        }
    }
    
    -1
}