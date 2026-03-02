pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
    let n = grid.len();

    // Count trailing zeros
    let mut trailing_zeros: Vec<usize> = grid
        .iter()
        .map(|row| {
            row.iter()
                .rev()
                .take_while(|&&x| x == 0)
                .count()
        })
        .collect();

    let mut swap_count = 0;

    for target_row in 0..n {
        let min_required_zeros = n - 1 - target_row;

        let candidate_row = trailing_zeros
            .iter()
            .position(|&z| z >= min_required_zeros);

        match candidate_row {
            Some(idx) => {
                swap_count += idx as i32;
                trailing_zeros.remove(idx);
            }
            None => return -1,
        }
    }

    swap_count
}