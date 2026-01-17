pub fn largest_square_area(
    bottom_left: &Vec<Vec<i32>>,
    top_right: &Vec<Vec<i32>>,
) -> i32 {
    let rectangle_count = bottom_left.len();
    let mut max_square_side = 0;

    for i in 0..rectangle_count - 1 {
        let (x1_i, y1_i) = (bottom_left[i][0], bottom_left[i][1]);
        let (x2_i, y2_i) = (top_right[i][0], top_right[i][1]);

        for j in i + 1..rectangle_count {
            let (x1_j, y1_j) = (bottom_left[j][0], bottom_left[j][1]);
            let (x2_j, y2_j) = (top_right[j][0], top_right[j][1]);

            let intersection_width =
                std::cmp::min(x2_i, x2_j) - std::cmp::max(x1_i, x1_j);
            let intersection_height =
                std::cmp::min(y2_i, y2_j) - std::cmp::max(y1_i, y1_j);

            if intersection_width <= 0 || intersection_height <= 0 {
                continue;
            }

            let square_side =
                std::cmp::min(intersection_width, intersection_height);
            max_square_side =
                std::cmp::max(max_square_side, square_side);
        }
    }

    max_square_side * max_square_side
}
