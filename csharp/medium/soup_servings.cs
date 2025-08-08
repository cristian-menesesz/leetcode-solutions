double SoupServings(int n) {

    int m = (int)Math.Ceiling(n / 25.0);
    var dp = new Dictionary<int, Dictionary<int, double>>();

    double CalculateDP(int i, int j) {
        if (i <= 0 && j <= 0) return 0.5;
        if (i <= 0) return 1.0;
        if (j <= 0) return 0.0;
        if (dp.ContainsKey(i) && dp[i].ContainsKey(j)) return dp[i][j];

        if (!dp.ContainsKey(i)) dp[i] = new Dictionary<int, double>();

        dp[i][j] = (
            CalculateDP(i - 4, j) +
            CalculateDP(i - 3, j - 1) +
            CalculateDP(i - 2, j - 2) +
            CalculateDP(i - 1, j - 3)
        ) / 4.0;

        return dp[i][j];
    }

    for (int k = 1; k <= m; k++) {
        if (CalculateDP(k, k) > 1 - 1e-5) {
            return 1.0;
        }
    }

    return CalculateDP(m, m);
}
