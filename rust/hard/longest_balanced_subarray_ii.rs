use std::collections::HashSet;

#[derive(Clone, Copy)]
struct SegmentNode {
    min_value: i32,
    max_value: i32,
    lazy: i32,
}

struct LazySegmentTree {
    n: usize,
    tree: Vec<SegmentNode>,
}

impl LazySegmentTree {
    fn new(arr: &Vec<i32>) -> Self {
        let n = arr.len();
        let mut st = Self {
            n,
            tree: vec![SegmentNode { min_value: 0, max_value: 0, lazy: 0 }; 4*n],
        };
        st.build(1, 0, n-1, arr);
        st
    }

    fn build(&mut self, idx: usize, l: usize, r: usize, arr: &Vec<i32>) {
        if l == r {
            self.tree[idx] = SegmentNode {
                min_value: arr[l],
                max_value: arr[l],
                lazy: 0
            };
            return;
        }

        let mid = (l + r) / 2;
        self.build(idx*2, l, mid, arr);
        self.build(idx*2+1, mid+1, r, arr);
        self.pull(idx);
    }

    fn pull(&mut self, idx: usize) {
        self.tree[idx].min_value =
            self.tree[idx*2].min_value.min(self.tree[idx*2+1].min_value);

        self.tree[idx].max_value =
            self.tree[idx*2].max_value.max(self.tree[idx*2+1].max_value);
    }

    fn push(&mut self, idx: usize, l: usize, r: usize) {
        if self.tree[idx].lazy == 0 { return; }

        let val = self.tree[idx].lazy;

        self.tree[idx].min_value += val;
        self.tree[idx].max_value += val;

        if l != r {
            self.tree[idx*2].lazy += val;
            self.tree[idx*2+1].lazy += val;
        }

        self.tree[idx].lazy = 0;
    }

    fn range_add(&mut self,
        ql: usize, qr: usize,
        idx: usize, l: usize, r: usize,
        val: i32) {

        self.push(idx, l, r);

        if r < ql || l > qr { return; }

        if ql <= l && r <= qr {
            self.tree[idx].lazy += val;
            self.push(idx, l, r);
            return;
        }

        let mid = (l + r) / 2;
        self.range_add(ql, qr, idx*2, l, mid, val);
        self.range_add(ql, qr, idx*2+1, mid+1, r, val);
        self.pull(idx);
    }

    fn find_rightmost_zero(&mut self,
        idx: usize, l: usize, r: usize) -> i32 {

        self.push(idx, l, r);

        if self.tree[idx].min_value > 0 ||
           self.tree[idx].max_value < 0 {
            return -1;
        }

        if l == r { return l as i32; }

        let mid = (l + r) / 2;

        let right = self.find_rightmost_zero(idx*2+1, mid+1, r);
        if right != -1 { return right; }

        self.find_rightmost_zero(idx*2, l, mid)
    }
}

/* ---------- Full Solution ---------- */

fn longest_balanced(nums: Vec<i32>) -> i32 {

    let n = nums.len();
    if n <= 2000 {
        return bruteforce(nums);
    }

    let mut last_occ = vec![n; 100001];
    let mut next_pos = vec![n; n];

    for i in (0..n).rev() {
        next_pos[i] = last_occ[nums[i] as usize];
        last_occ[nums[i] as usize] = i;
    }

    let mut seen = HashSet::new();
    let mut prefix = vec![0; n];
    let mut diff = 0;

    for i in 0..n {
        if seen.insert(nums[i]) {
            diff += if nums[i] % 2 == 1 { 1 } else { -1 };
        }
        prefix[i] = diff;
    }

    let mut st = LazySegmentTree::new(&prefix);

    let mut answer =
        match st.find_rightmost_zero(1, 0, n-1) {
            -1 => 0,
            x => x + 1
        };

    for i in 0..n-1 {
        let right_limit = next_pos[i].saturating_sub(1);

        if i+1 <= right_limit {
            let adj = if nums[i] % 2 == 1 { -1 } else { 1 };
            st.range_add(i+1, right_limit,
                         1, 0, n-1, adj);
        }

        let rightmost = st.find_rightmost_zero(1, 0, n-1);
        if rightmost != -1 {
            answer = answer.max(rightmost - i as i32);
        }
    }

    answer
}

fn bruteforce(nums: Vec<i32>) -> i32 {
    let n = nums.len();
    let mut best = 0;

    for start in 0..n {
        let mut seen = HashSet::new();
        let mut diff = 0;

        for end in start..n {
            if seen.insert(nums[end]) {
                diff += if nums[end] % 2 == 1 { -1 } else { 1 };
            }
            if diff == 0 {
                best = best.max((end - start + 1) as i32);
            }
        }
    }

    best
}
