int bitwiseComplement(int n) {
    if (n == 0) return 1;

    int bit_length = 0;
    int temp = n;

    while (temp) {
        bit_length++;
        temp >>= 1;
    }

    int mask = (1 << bit_length) - 1;
    return (~n) & mask;
}
