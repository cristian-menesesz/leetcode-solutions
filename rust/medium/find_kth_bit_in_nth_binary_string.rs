fn find_kth_bit(n: i32, k: i32) -> char {
    // Base case
    if k == 1 {
        return '0';
    }

    // bit_length equivalent
    let bit_size = 32 - (k as u32).leading_zeros();

    // Mirror index
    let mirrored_index = (1 << bit_size) - k;

    // Symmetry center
    if mirrored_index == k {
        return '1';
    }

    // Recursive lookup
    let mirrored_bit = find_kth_bit(n, mirrored_index);

    // Invert
    if mirrored_bit == '1' { '0' } else { '1' }
}