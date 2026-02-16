pub fn reverse_bits(mut n: u32) -> u32 {
    let mut result: u32 = 0;

    for _ in 0..32 {
        result = (result << 1) | (n & 1);
        n >>= 1;
    }

    result
}
