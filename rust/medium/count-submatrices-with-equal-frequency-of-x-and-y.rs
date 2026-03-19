pub fn number_of_submatrices(grid: Vec<Vec<char>>) -> i32 {
    let rows = grid.len();
    let cols = grid[0].len();

    let mut col_x = vec![0; cols];
    let mut col_y = vec![0; cols];
    let mut result = 0;

    for r in 0..rows {
        let mut row_x = 0;
        let mut row_y = 0;

        for c in 0..cols {
            match grid[r][c] {
                'X' => row_x += 1,
                'Y' => row_y += 1,
                _ => {}
            }

            col_x[c] += row_x;
            col_y[c] += row_y;

            if col_x[c] > 0 && col_x[c] == col_y[c] {
                result += 1;
            }
        }
    }

    result
}