use std::collections::HashMap;

struct Solution;

impl Solution {
    fn longest_single_char_run(s: &str) -> i32 {
        let bytes = s.as_bytes();
        if bytes.is_empty() {
            return 0;
        }

        let mut max_run = 1;
        let mut current_run = 1;

        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] {
                current_run += 1;
            } else {
                max_run = max_run.max(current_run);
                current_run = 1;
            }
        }

        max_run.max(current_run)
    }

    fn longest_balanced(s: String) -> i32 {
        let mut max_length = Self::longest_single_char_run(&s);

        let mut seen_abc: HashMap<(i32, i32), i32> = HashMap::new();
        let mut seen_ab: HashMap<(i32, i32), i32> = HashMap::new();
        let mut seen_bc: HashMap<(i32, i32), i32> = HashMap::new();
        let mut seen_ca: HashMap<(i32, i32), i32> = HashMap::new();

        seen_abc.insert((0, 0), -1);
        seen_ab.insert((0, 0), -1);
        seen_bc.insert((0, 0), -1);
        seen_ca.insert((0, 0), -1);

        let mut count_a = 0;
        let mut count_b = 0;
        let mut count_c = 0;

        for (index, ch) in s.chars().enumerate() {
            match ch {
                'a' => count_a += 1,
                'b' => count_b += 1,
                _ => count_c += 1,
            }

            let a = count_a;
            let b = count_b;
            let c = count_c;

            if let Some(&prev) = seen_abc.get(&(b - a, c - a)) {
                max_length = max_length.max(index as i32 - prev);
            } else {
                seen_abc.insert((b - a, c - a), index as i32);
            }

            if let Some(&prev) = seen_ab.get(&(a - b, c)) {
                max_length = max_length.max(index as i32 - prev);
            } else {
                seen_ab.insert((a - b, c), index as i32);
            }

            if let Some(&prev) = seen_bc.get(&(b - c, a)) {
                max_length = max_length.max(index as i32 - prev);
            } else {
                seen_bc.insert((b - c, a), index as i32);
            }

            if let Some(&prev) = seen_ca.get(&(c - a, b)) {
                max_length = max_length.max(index as i32 - prev);
            } else {
                seen_ca.insert((c - a, b), index as i32);
            }
        }

        max_length
    }
}


// beats 96% - 796ms

use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        if n == 0 {
            return 0;
        }

        // 1) Longest single-character run
        let mut max_run = 1;
        let mut current_run = 1;

        for i in 1..n {
            if chars[i] == chars[i - 1] {
                current_run += 1;
            } else {
                max_run = max_run.max(current_run);
                current_run = 1;
            }
        }
        max_run = max_run.max(current_run);

        let mut result = max_run;

        // 2) Two-character balanced
        result = result.max(Self::longest_two_balanced(&chars, 'a', 'b'));
        result = result.max(Self::longest_two_balanced(&chars, 'a', 'c'));
        result = result.max(Self::longest_two_balanced(&chars, 'b', 'c'));

        // 3) Three-character balanced
        result = result.max(Self::longest_three_balanced(&chars));

        result as i32
    }

    fn longest_two_balanced(chars: &[char], c1: char, c2: char) -> usize {
        let mut balance = 0;
        let mut max_length = 0;
        let mut first_occurrence = HashMap::new();
        first_occurrence.insert(0, -1);

        for (i, &ch) in chars.iter().enumerate() {
            if ch != c1 && ch != c2 {
                balance = 0;
                first_occurrence.clear();
                first_occurrence.insert(0, i as i32);
                continue;
            }

            if ch == c1 {
                balance += 1;
            } else {
                balance -= 1;
            }

            if let Some(&first_index) = first_occurrence.get(&balance) {
                max_length = max_length.max(i - first_index as usize);
            } else {
                first_occurrence.insert(balance, i as i32);
            }
        }

        max_length
    }

    fn longest_three_balanced(chars: &[char]) -> usize {
        let mut count_a = 0;
        let mut count_b = 0;
        let mut count_c = 0;

        let mut max_length = 0;
        let mut first_occurrence = HashMap::new();
        first_occurrence.insert((0, 0), -1);

        for (i, &ch) in chars.iter().enumerate() {
            match ch {
                'a' => count_a += 1,
                'b' => count_b += 1,
                _ => count_c += 1,
            }

            let state = (count_b - count_a, count_c - count_a);

            if let Some(&first_index) = first_occurrence.get(&state) {
                max_length = max_length.max(i - first_index as usize);
            } else {
                first_occurrence.insert(state, i as i32);
            }
        }

        max_length
    }
}
