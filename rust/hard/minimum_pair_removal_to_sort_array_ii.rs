use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn minimum_pair_removal(mut nums: Vec<i32>) -> i32 {
    let n = nums.len();
    
    if Self::is_non_decreasing(&nums) {
        return 0;
    }
    
    let mut removed = vec![false; n];
    let mut prev_idx: Vec<i32> = (0..n as i32).map(|i| i - 1).collect();
    let mut next_idx: Vec<i32> = (0..n as i32).map(|i| if i + 1 < n as i32 { i + 1 } else { -1 }).collect();
    let mut values: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
    
    let mut heap = BinaryHeap::new();
    
    for i in 0..n - 1 {
        heap.push(Reverse((values[i] + values[i + 1], i)));
    }
    
    let mut violations: i32 = nums.windows(2).filter(|w| w[0] > w[1]).count() as i32;
    
    let mut operations = 0;
    
    while violations > 0 && !heap.is_empty() {
        let Reverse((pair_sum, left)) = heap.pop().unwrap();
        
        if removed[left] || next_idx[left] == -1 {
            continue;
        }
        
        let right = next_idx[left] as usize;
        
        if removed[right] || values[left] + values[right] != pair_sum {
            continue;
        }
        
        let left_prev = prev_idx[left];
        let right_next = next_idx[right];
        
        if left_prev != -1 && values[left_prev as usize] > values[left] {
            violations -= 1;
        }
        if values[left] > values[right] {
            violations -= 1;
        }
        if right_next != -1 && values[right] > values[right_next as usize] {
            violations -= 1;
        }
        
        values[left] = pair_sum;
        removed[right] = true;
        
        next_idx[left] = right_next;
        if right_next != -1 {
            prev_idx[right_next as usize] = left as i32;
        }
        
        if left_prev != -1 && values[left_prev as usize] > values[left] {
            violations += 1;
        }
        if right_next != -1 && values[left] > values[right_next as usize] {
            violations += 1;
        }
        
        if left_prev != -1 {
            heap.push(Reverse((values[left_prev as usize] + values[left], left_prev as usize)));
        }
        if right_next != -1 {
            heap.push(Reverse((values[left] + values[right_next as usize], left)));
        }
        
        operations += 1;
    }
    
    operations
}

fn is_non_decreasing(arr: &[i32]) -> bool {
    arr.windows(2).all(|w| w[0] <= w[1])
}
