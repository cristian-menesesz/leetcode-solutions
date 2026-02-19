pub fn count_binary_substrings(s: String) -> i32 {
    let bytes = s.as_bytes();
    let mut total_substrings = 0;
    let mut previous_run_length = 0;
    let mut current_run_length = 1;

    for i in 1..bytes.len() {
        if bytes[i] == bytes[i - 1] {
            current_run_length += 1;
        } else {
            previous_run_length = current_run_length;
            current_run_length = 1;
        }

        if current_run_length <= previous_run_length {
            total_substrings += 1;
        }
    }

    total_substrings
}
