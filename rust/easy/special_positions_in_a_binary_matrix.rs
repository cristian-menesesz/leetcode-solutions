pub fn num_special(matrix: Vec<Vec<i32>>) -> i32 {
    let rows = matrix.len();
    let cols = matrix[0].len();

    let mut special_count = 0;
    let mut column_checked = vec![false; cols];

    for r in 0..rows {
        let mut one_count = 0;
        let mut col_index = 0;

        // count ones in row
        for (c, &value) in matrix[r].iter().enumerate() {
            if value == 1 {
                one_count += 1;
                col_index = c;
            }
        }

        // Case 1: exactly one '1'
        if one_count == 1 {
            if !column_checked[col_index] {
                column_checked[col_index] = true;

                let column_sum: i32 =
                    (0..rows).map(|rr| matrix[rr][col_index]).sum();

                if column_sum == 1 {
                    special_count += 1;
                }
            }
        }
        // Case 2: multiple ones
        else if one_count > 1 {
            for (c, &value) in matrix[r].iter().enumerate() {
                if value == 1 {
                    column_checked[c] = true;
                }
            }
        }
    }

    special_count
}