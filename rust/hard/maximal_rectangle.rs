impl Solution {
    fn find_max_rectangle_area(heights: &Vec<i32>) -> i32 {
        let n = heights.len();
        if n == 0 {
            return 0;
        }

        let mut left = vec![-1; n];
        let mut right = vec![n as i32; n];

        for i in 1..n {
            let mut boundary = (i - 1) as i32;
            while boundary >= 0 && heights[boundary as usize] >= heights[i] {
                boundary = left[boundary as usize];
            }
            left[i] = boundary;
        }

        let mut max_area =
            heights[n - 1] * (right[n - 1] - left[n - 1] - 1);

        for i in (0..n - 1).rev() {
            let mut boundary = (i + 1) as i32;
            while boundary < n as i32 && heights[boundary as usize] >= heights[i] {
                boundary = right[boundary as usize];
            }
            right[i] = boundary;

            let width = right[i] - left[i] - 1;
            let area = heights[i] * width;
            if area > max_area {
                max_area = area;
            }
        }

        max_area
    }

    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }

        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut heights = vec![0; cols];
        let mut max_area = 0;

        for r in 0..rows {
            for c in 0..cols {
                heights[c] = if matrix[r][c] == '0' {
                    0
                } else {
                    heights[c] + 1
                };
            }
            max_area = max_area.max(Self::find_max_rectangle_area(&heights));
        }

        max_area
    }
}
