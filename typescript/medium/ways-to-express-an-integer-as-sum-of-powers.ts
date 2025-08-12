function numberOfWays(n: number, x: number): number {
    const MOD = 1_000_000_007;
    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        const val = Math.pow(i, x);
        if (val > n) break;
        for (let j = n; j >= val; j--) {
            dp[j] = (dp[j] + dp[j - val]) % MOD;
        }
    }

    return dp[n];
}
