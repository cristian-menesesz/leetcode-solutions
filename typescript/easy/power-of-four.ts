function isPowerOfFour(n: number): boolean {
    return (n & (n - 1)) === 0 && n % 3 === 1;
}
