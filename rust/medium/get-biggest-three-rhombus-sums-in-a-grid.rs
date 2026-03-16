const OFFSET: i32 = 50;

#[inline]
fn rhombus_sum(
    r: usize,
    c: usize,
    d: usize,
    grid: &Vec<Vec<i32>>,
    diag_prefix: &Vec<Vec<i32>>,
    anti_prefix: &Vec<Vec<i32>>,
) -> i32 {

    if d == 0 {
        return grid[r][c];
    }

    let left = c - d;
    let right = c + d;
    let top = r - d;
    let bottom = r + d;

    let mut total = 0;

    let diag0 = (top as i32 - c as i32 + OFFSET) as usize;
    let diag1 = (r as i32 - left as i32 + OFFSET) as usize;

    total += diag_prefix[diag0][right + 1] - diag_prefix[diag0][c];
    total += diag_prefix[diag1][c + 1] - diag_prefix[diag1][left];

    let anti0 = top + c;
    let anti1 = bottom + c;

    total += anti_prefix[anti0][r] - anti_prefix[anti0][top + 1];
    total += anti_prefix[anti1][bottom] - anti_prefix[anti1][r + 1];

    total
}

pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {

    let rows = grid.len();
    let cols = grid[0].len();

    let mut diag_prefix = vec![vec![0; cols + 1]; 100];
    let mut anti_prefix = vec![vec![0; rows + 1]; 100];

    for r in 0..rows {
        for c in 0..cols {

            let val = grid[r][c];

            let diag_idx = (r as i32 - c as i32 + OFFSET) as usize;
            let anti_idx = r + c;

            diag_prefix[diag_idx][c + 1] =
                diag_prefix[diag_idx][c] + val;

            anti_prefix[anti_idx][r + 1] =
                anti_prefix[anti_idx][r] + val;
        }
    }

    let mut best = [-1, -1, -1];
    let max_radius = rows.min(cols) / 2;

    for d in 0..=max_radius {
        for r in d..rows - d {
            for c in d..cols - d {

                let val = rhombus_sum(r, c, d, &grid, &diag_prefix, &anti_prefix);

                if best.contains(&val) {
                    continue;
                }

                if val > best[0] {
                    best[2] = best[1];
                    best[1] = best[0];
                    best[0] = val;
                } else if val > best[1] {
                    best[2] = best[1];
                    best[1] = val;
                } else if val > best[2] {
                    best[2] = val;
                }
            }
        }
    }

    best.into_iter().filter(|&x| x != -1).collect()
}