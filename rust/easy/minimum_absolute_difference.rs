fn minimum_abs_difference(mut arr: Vec<i32>) -> Vec<Vec<i32>> {
    arr.sort();
    let mut min_diff = i32::MAX;
    let mut result_pairs = Vec::new();

    for i in 1..arr.len() {
        let diff = arr[i] - arr[i - 1];
        if diff < min_diff {
            min_diff = diff;
            result_pairs.clear();
        }
        if diff == min_diff {
            result_pairs.push(vec![arr[i - 1], arr[i]]);
        }
    }

    result_pairs
}
