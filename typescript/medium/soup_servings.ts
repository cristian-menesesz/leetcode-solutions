function soupServings(n: number): number {
    const m = Math.ceil(n / 25);
    const dp: Record<number, Record<number, number>> = {};

    function calculateDP(i: number, j: number): number {
        if (i <= 0 && j <= 0) return 0.5;
        if (i <= 0) return 1.0;
        if (j <= 0) return 0.0;
        if (dp[i]?.[j] !== undefined) return dp[i][j];

        dp[i] = dp[i] || {};
        dp[i][j] =
            (calculateDP(i - 4, j) +
                calculateDP(i - 3, j - 1) +
                calculateDP(i - 2, j - 2) +
                calculateDP(i - 1, j - 3)) /
            4.0;

        return dp[i][j];
    }

    for (let k = 1; k <= m; k++) {
        if (calculateDP(k, k) > 1 - 1e-5) {
            return 1.0;
        }
    }

    return calculateDP(m, m);
}
