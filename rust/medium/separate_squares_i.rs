fn area_above_y(squares: &Vec<[i32; 3]>, cut_y: f64) -> f64 {
    let mut total_area = 0.0;

    for s in squares {
        let bottom_y = s[1] as f64;
        let side = s[2] as f64;
        let top_y = bottom_y + side;

        if cut_y >= top_y {
            continue;
        }

        let visible_height = side.min(top_y - cut_y);
        total_area += side * visible_height;
    }

    total_area
}

fn separate_squares(squares: &Vec<[i32; 3]>) -> f64 {
    let total_area = area_above_y(squares, -1e18);
    let half_area = total_area / 2.0;

    let mut min_y = f64::INFINITY;
    let mut max_y = f64::NEG_INFINITY;

    for s in squares {
        let bottom_y = s[1] as f64;
        let side = s[2] as f64;
        min_y = min_y.min(bottom_y);
        max_y = max_y.max(bottom_y + side);
    }

    let mut left = min_y;
    let mut right = max_y;
    let epsilon = 1e-5;

    while right - left > epsilon {
        let mid = (left + right) / 2.0;
        let area_above = area_above_y(squares, mid);

        if area_above > half_area {
            left = mid;
        } else {
            right = mid;
        }
    }

    left
}
