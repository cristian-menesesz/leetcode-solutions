fn longest_consecutive_run(bars: &Vec<i32>) -> i32 {
    if bars.is_empty() {
        return 0;
    }

    let mut max_run = 1;
    let mut current_run = 1;

    for i in 1..bars.len() {
        if bars[i] == bars[i - 1] + 1 {
            current_run += 1;
        } else {
            max_run = max_run.max(current_run);
            current_run = 1;
        }
    }

    max_run.max(current_run)
}

fn maximize_square_hole_area(
    _n: i32,
    _m: i32,
    mut h_bars: Vec<i32>,
    mut v_bars: Vec<i32>,
) -> i32 {
    h_bars.sort();
    v_bars.sort();

    let max_horizontal_run = longest_consecutive_run(&h_bars);
    let max_vertical_run = longest_consecutive_run(&v_bars);

    let max_square_side = std::cmp::min(max_horizontal_run, max_vertical_run) + 1;
    max_square_side * max_square_side
}
