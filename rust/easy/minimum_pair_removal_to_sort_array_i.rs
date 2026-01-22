use std::i32::{MAX, MIN};

const REMOVED: i32 = MAX;

fn is_non_decreasing_ignoring_removed(arr: &Vec<i32>) -> bool {
    let mut prev = MIN;

    for &v in arr {
        if v == REMOVED {
            continue;
        }
        if v < prev {
            return false;
        }
        prev = v;
    }
    true
}

fn minimum_pair_removal(nums: &mut Vec<i32>) -> i32 {
    let mut operations = 0;
    let n = nums.len();

    while !is_non_decreasing_ignoring_removed(nums) {
        let mut min_pair_sum = MAX;
        let mut left: isize = -1;
        let mut right: isize = -1;

        let mut i = 0;
        while i + 1 < n {
            if nums[i] == REMOVED {
                i += 1;
                continue;
            }

            let mut j = i + 1;
            while j < n && nums[j] == REMOVED {
                j += 1;
            }

            if j < n {
                let sum = nums[i] + nums[j];
                if sum < min_pair_sum {
                    min_pair_sum = sum;
                    left = i as isize;
                    right = j as isize;
                }
            }

            i += 1;
        }

        if left == -1 {
            break;
        }

        let l = left as usize;
        let r = right as usize;

        nums[l] += nums[r];
        nums[r] = REMOVED;
        operations += 1;
    }

    operations
}
