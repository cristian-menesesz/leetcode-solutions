public int BitwiseComplement(int n) {
    if (n == 0) return 1;

    int bitLength = (int)Math.Log(n, 2) + 1;
    int mask = (1 << bitLength) - 1;

    return (~n) & mask;
}
