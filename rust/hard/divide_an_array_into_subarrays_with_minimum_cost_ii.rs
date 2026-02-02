use std::collections::BTreeSet;

fn minimum_cost(nums: Vec<i32>, k: usize, dist: usize) -> i32 {
    let required = k - 1;
    let mut chosen = BTreeSet::new();
    let mut overflow = BTreeSet::new();
    let mut chosen_sum: i32 = 0;

    let mut add = |x: (i32, usize)| {
        chosen.insert(x);
        chosen_sum += x.0;
        if chosen.len() > required {
            let largest = *chosen.iter().next_back().unwrap();
            chosen.remove(&largest);
            chosen_sum -= largest.0;
            overflow.insert(largest);
        }
    };

    let mut remove = |x: (i32, usize)| {
        if chosen.remove(&x) {
            chosen_sum -= x.0;
            if let Some(&smallest) = overflow.iter().next() {
                overflow.remove(&smallest);
                chosen.insert(smallest);
                chosen_sum += smallest.0;
            }
        } else {
            overflow.remove(&x);
        }
    };

    for i in 1..=dist + 1 {
        add((nums[i], i));
    }

    let mut ans = nums[0] + chosen_sum;
    let mut left = 1;

    for right in dist + 2..nums.len() {
        remove((nums[left], left));
        left += 1;
        add((nums[right], right));
        ans = ans.min(nums[0] + chosen_sum);
    }

    ans
}
