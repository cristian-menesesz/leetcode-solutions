IList<int> ProductQueries(int n, int[][] queries) {
        const int mod = 1_000_000_007;
        List<long> bins = new List<long>();
        long rep = 1;

        while (n > 0) {
            if ((n & 1) != 0) {
                bins.Add(rep);
            }
            n >>= 1;
            rep <<= 1;
        }

        int m = bins.Count;
        long[] prefix = new long[m];
        prefix[0] = bins[0] % mod;

        for (int i = 1; i < m; i++) {
            prefix[i] = (prefix[i - 1] * bins[i]) % mod;
        }

        long ModPow(long baseVal, long exp, long modVal) {
            long result = 1;
            baseVal %= modVal;
            while (exp > 0) {
                if ((exp & 1) != 0) result = (result * baseVal) % modVal;
                baseVal = (baseVal * baseVal) % modVal;
                exp >>= 1;
            }
            return result;
        }

        long ModInv(long x) {
            return ModPow(x, mod - 2, mod); // Fermat's little theorem
        }

        List<int> ans = new List<int>();
        foreach (var query in queries) {
            int left = query[0];
            int right = query[1];
            if (left == 0) {
                ans.Add((int)prefix[right]);
            } else {
                ans.Add((int)((prefix[right] * ModInv(prefix[left - 1])) % mod));
            }
        }

        return ans;
    }
