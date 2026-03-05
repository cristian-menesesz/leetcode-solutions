pub fn min_operations(s: &str) -> i32 {
    let mut mismatches_starting_with_zero = 0;

    for (index, byte) in s.bytes().enumerate() {
        mismatches_starting_with_zero += (((byte & 1) ^ (index as u8)) & 1) as i32;
    }

    let length = s.len() as i32;
    let mismatches_starting_with_one = length - mismatches_starting_with_zero;

    mismatches_starting_with_zero.min(mismatches_starting_with_one)
}