struct SegmentTree {
    x_coords: Vec<i32>,
    segment_count: usize,
    coverage_count: Vec<i32>,
    covered_length: Vec<i32>,
}

impl SegmentTree {
    fn new(x_coords: Vec<i32>) -> Self {
        let segment_count = x_coords.len() - 1;
        SegmentTree {
            x_coords,
            segment_count,
            coverage_count: vec![0; 4 * segment_count],
            covered_length: vec![0; 4 * segment_count],
        }
    }

    fn update(
        &mut self,
        x_left: i32,
        x_right: i32,
        delta: i32,
        left: usize,
        right: usize,
        node: usize,
    ) {
        if self.x_coords[right + 1] <= x_left ||
           self.x_coords[left] >= x_right {
            return;
        }

        if x_left <= self.x_coords[left] &&
           self.x_coords[right + 1] <= x_right {
            self.coverage_count[node] += delta;
        } else {
            let mid = (left + right) / 2;
            self.update(x_left, x_right, delta, left, mid, node * 2 + 1);
            self.update(x_left, x_right, delta, mid + 1, right, node * 2 + 2);
        }

        if self.coverage_count[node] > 0 {
            self.covered_length[node] =
                self.x_coords[right + 1] - self.x_coords[left];
        } else if left == right {
            self.covered_length[node] = 0;
        } else {
            self.covered_length[node] =
                self.covered_length[node * 2 + 1] +
                self.covered_length[node * 2 + 2];
        }
    }

    fn query(&self) -> i32 {
        self.covered_length[0]
    }
}
