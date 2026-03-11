fn bitwise_complement(n: Int) -> Int:
    if n == 0:
        return 1

    var bit_len = n.bit_length()
    var mask = (1 << bit_len) - 1

    return (~n) & mask