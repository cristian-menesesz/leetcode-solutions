fn cups_until_half(row: usize) -> usize {
    (row * row + 2 * row + (row % 2)) / 4
}

fn overflow(x: f64) -> f64 {
    if x > 1.0 { x - 1.0 } else { 0.0 }
}

pub fn champagne_tower(poured: i32, query_row: usize, query_glass: usize) -> f64 {
    if poured == 0 {
        return 0.0;
    }

    let col = query_glass.min(query_row - query_glass);

    let total_cups = cups_until_half(query_row) + col + 1;
    let mut cups = vec![0.0f64; total_cups];

    cups[0] = poured as f64;
    let mut prev_row_start = 0;

    // build rows up to query_row - 1
    for r in 1..query_row {
        let row_start = cups_until_half(r);

        // left edge
        cups[row_start] = overflow(cups[prev_row_start]) / 2.0;

        // middle
        for j in 1..((r + 1) / 2) {
            cups[row_start + j] =
                (overflow(cups[prev_row_start + j - 1]) +
                 overflow(cups[prev_row_start + j])) / 2.0;
        }

        // center when even width
        if r % 2 == 0 {
            cups[row_start + r / 2] =
                overflow(cups[prev_row_start + r / 2 - 1]);
        }

        prev_row_start = row_start;
    }

    // final row
    let final_row_start = cups_until_half(query_row);

    if query_row > 0 {
        cups[final_row_start] = overflow(cups[prev_row_start]) / 2.0;

        for j in 1..col {
            cups[final_row_start + j] =
                (overflow(cups[prev_row_start + j - 1]) +
                 overflow(cups[prev_row_start + j])) / 2.0;
        }
    }

    let result = if col == 0 {
        cups[final_row_start]
    } else if col * 2 == query_row {
        overflow(cups[prev_row_start + col - 1])
    } else {
        (overflow(cups[prev_row_start + col - 1]) +
         overflow(cups[prev_row_start + col])) / 2.0
    };

    result.min(1.0)
}


// beats 99.76%

pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {

    let target_col = query_glass.min(query_row - query_glass) as usize;

    let mut flow = vec![0.0f64; target_col + 1];
    flow[0] = poured as f64;

    let max_left_reach = query_row - target_col as i32 + 1;
    let mut dry_cutoff: i32 = -1;

    for row in 0..query_row {

        let mut center = (row >> 1) as usize;
        let row_is_odd: bool;

        if center >= target_col {
            center = target_col;
            row_is_odd = false;
        } else {
            row_is_odd = (row & 1) == 1;
        }

        let mut overflow = (flow[center] - 1.0).max(0.0);

        if overflow == 0.0 {
            return 0.0;
        }

        if row_is_odd {
            flow[center + 1] += overflow;
        }

        flow[center] = overflow * 0.5;

        let lower_bound = (row - max_left_reach).max(dry_cutoff);

        let mut col = center as i32 - 1;
        while col > lower_bound {
            let idx = col as usize;

            let spill = ((flow[idx] - 1.0).max(0.0)) * 0.5;

            if spill == 0.0 {
                dry_cutoff = col;
                break;
            }

            flow[idx + 1] += spill;
            flow[idx] = spill;

            col -= 1;
        }
    }

    flow[target_col].min(1.0)
}
