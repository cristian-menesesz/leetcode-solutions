pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
    
    let mut total_sum: i64 = 0;
    let mut min_abs: i32 = i32::MAX;
    let mut negative_count = 0;

    for row in matrix.iter() {
        for &value in row.iter() {
            let abs_val = value.abs();
            total_sum += abs_val as i64;

            if abs_val < min_abs {
                min_abs = abs_val;
            }

            if value < 0 {
                negative_count += 1;
            }
        }
    }

    if negative_count % 2 == 0 {
        total_sum
    } else {
        total_sum - 2 * min_abs as i64
    }
}
