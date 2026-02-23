pub fn has_all_codes(s: &str, k: usize) -> bool {
    let n = s.len();

    if n < k {
        return false;
    }

    let total_codes = 1usize << k;
    let mut window_mask: usize = 0;
    let lower_bits_mask = (1usize << (k - 1)) - 1;

    let mut seen = vec![false; total_codes];
    let mut seen_count = 0usize;

    let bytes = s.as_bytes();

    // ---- build first window ----
    for i in 0..k {
        window_mask = (window_mask << 1) | ((bytes[i] == b'1') as usize);
    }

    seen[window_mask] = true;
    seen_count = 1;

    // ---- sliding window ----
    for right in k..n {
        // remove highest bit
        window_mask &= lower_bits_mask;

        // shift + add new bit
        window_mask =
            (window_mask << 1) | ((bytes[right] == b'1') as usize);

        if !seen[window_mask] {
            seen[window_mask] = true;
            seen_count += 1;

            if seen_count == total_codes {
                return true;
            }
        }
    }

    seen_count == total_codes
}