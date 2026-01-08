use std::cmp::max;

pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
    
    if nums1.len() < nums2.len() {
        return max_dot_product(nums2, nums1);
    }

    let n = nums1.len();
    let m = nums2.len();
    let neg_inf = i32::MIN / 2;
    let mut dp = vec![vec![neg_inf; m + 1]; 2];
    let mut max_result = neg_inf;

    for i in (0..n).rev() {
        
        let curr = i & 1;
        let next = (i + 1) & 1;

        for j in (0..m).rev() {
            
            let product = nums1[i] * nums2[j];

            let mut best = product;

            best = max(best, product + dp[next][j + 1]);

            best = max(best, dp[curr][j + 1]);
            
            dp[curr][j] = max(best, dp[next][j]);

            max_result = max(max_result, dp[curr][j]);
        }
    }

    max_result
}
