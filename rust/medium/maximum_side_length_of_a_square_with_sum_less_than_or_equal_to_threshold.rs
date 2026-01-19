fn submatrix_sum(
    r0: usize, r1: usize,
    c0: usize, c1: usize,
    prefix: &Vec<Vec<i32>>
) -> i32 {
    let mut total = prefix[r1][c1];
    if r0 > 0 { total -= prefix[r0 - 1][c1]; }
    if c0 > 0 { total -= prefix[r1][c0 - 1]; }
    if r0 > 0 && c0 > 0 { total += prefix[r0 - 1][c0 - 1]; }
    total
}

fn max_square_from_diagonal(
    sr: usize, sc: usize,
    rows: usize, cols: usize,
    prefix: &Vec<Vec<i32>>,
    threshold: i32
) -> usize {
    let max_possible = (rows - sr).min(cols - sc);
    let mut best = 0usize;
    let mut left = 0usize;

    for right in 0..max_possible {
        let mut r0 = sr + left;
        let r1 = sr + right;
        let mut c0 = sc + left;
        let c1 = sc + right;

        let mut sum = submatrix_sum(r0, r1, c0, c1, prefix);

        while left < right && sum > threshold {
            left += 1;
            r0 += 1;
            c0 += 1;
            sum = submatrix_sum(r0, r1, c0, c1, prefix);
        }

        if sum <= threshold {
            best = best.max(right - left + 1);
        }
    }

    best
}

fn max_side_length(mut mat: Vec<Vec<i32>>, threshold: i32) -> usize {
    let rows = mat.len();
    let cols = mat[0].len();

    for j in 1..cols {
        mat[0][j] += mat[0][j - 1];
    }

    for i in 1..rows {
        mat[i][0] += mat[i - 1][0];
        for j in 1..cols {
            mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1];
        }
    }

    let mut best = 0;

    for i in 0..rows {
        if rows - i <= best { break; }
        best = best.max(max_square_from_diagonal(i, 0, rows, cols, &mat, threshold));
    }

    for j in 1..cols {
        if cols - j <= best { break; }
        best = best.max(max_square_from_diagonal(0, j, rows, cols, &mat, threshold));
    }

    best
}
