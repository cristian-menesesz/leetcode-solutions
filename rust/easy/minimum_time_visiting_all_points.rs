impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut total_time = 0;

        for i in 0..points.len() - 1 {
            let dx = (points[i + 1][0] - points[i][0]).abs();
            let dy = (points[i + 1][1] - points[i][1]).abs();
            total_time += dx.max(dy);
        }

        total_time
    }
}
