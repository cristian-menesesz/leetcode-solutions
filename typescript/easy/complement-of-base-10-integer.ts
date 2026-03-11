function bitwiseComplement(n: number): number {
    if (n === 0) return 1;

    const bitLength = 32 - Math.clz32(n);
    const mask = (1 << bitLength) - 1;

    return ~n & mask;
}
