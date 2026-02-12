pub fn longest_balanced(s: &str) -> usize {
    let bytes = s.as_bytes();
    let length = bytes.len();
    let mut longest_length = 1;

    for left in 0..length {

        let mut char_frequency = [0usize; 26];
        let mut distinct_count = 0usize;
        let mut max_frequency = 0usize;
        let mut num_chars_with_max_frequency = 0usize;

        for right in left..length {

            let char_index = (bytes[right] - b'a') as usize;
            char_frequency[char_index] += 1;
            let current_frequency = char_frequency[char_index];

            if current_frequency == 1 {
                distinct_count += 1;
            }

            if current_frequency > max_frequency {
                max_frequency = current_frequency;
                num_chars_with_max_frequency = 1;
            } else if current_frequency == max_frequency {
                num_chars_with_max_frequency += 1;
            }

            if distinct_count == num_chars_with_max_frequency {
                longest_length = longest_length.max(right - left + 1);
            }
        }
    }

    longest_length
}
