pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
    let r = grid.len();
    let c = grid[0].len();
    let mut row = vec![vec![0; c+1]; r+1];
    let mut col = vec![vec![0; c+1]; r+1];
    let mut diag = vec![vec![0; c+1]; r+1];
    let mut anti = vec![vec![0; c+1]; r+1];

    for i in 0..r {
        for j in 0..c {
            let v = grid[i][j];
            row[i+1][j+1] = row[i+1][j] + v;
            col[i+1][j+1] = col[i][j+1] + v;
            diag[i+1][j+1] = diag[i][j] + v;
            anti[i+1][j] = anti[i][j+1] + v;
        }
    }

    for size in (2..=r.min(c)).rev() {
        for top in 0..=r-size {
            for left in 0..=c-size {
                let d1 = diag[top+size][left+size] - diag[top][left];
                let d2 = anti[top+size][left] - anti[top][left+size];
                if d1 != d2 { continue; }

                let mut ok = true;
                for k in 0..size {
                    if row[top+k+1][left+size] - row[top+k+1][left] != d1 ||
                       col[top+size][left+k+1] - col[top][left+k+1] != d1 {
                        ok = false;
                        break;
                    }
                }
                if ok { return size as i32; }
            }
        }
    }
    1
}
