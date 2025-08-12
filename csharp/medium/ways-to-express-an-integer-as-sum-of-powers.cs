int NumberOfWays(int n, int x)
    {
        const int MOD = 1_000_000_007;
        int[] dp = new int[n + 1];
        dp[0] = 1;

        for (int i = 1; i <= n; i++)
        {
            long val = (long)Math.Pow(i, x);
            if (val > n) break;
            for (int j = n; j >= val; j--)
            {
                dp[j] = (int)((dp[j] + dp[j - (int)val]) % MOD);
            }
        }

        return dp[n];
    }
