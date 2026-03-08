
pub fn find_different_binary_string(binary_strings: Vec<String>) -> String {
    let n = binary_strings.len();
    let mut result = Vec::with_capacity(n);

    for (i, s) in binary_strings.iter().enumerate() {
        let bit = s.as_bytes()[i];
        result.push(if bit == b'0' { b'1' } else { b'0' });
    }

    String::from_utf8(result).unwrap()
}
