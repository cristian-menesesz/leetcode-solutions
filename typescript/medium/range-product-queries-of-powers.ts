function productQueries(n: number, queries: number[][]): number[] {
    const mod = 1_000_000_007;
    let bins: number[] = [];
    let rep = 1;

    while (n > 0) {
        if ((n & 1) !== 0) {
            bins.push(rep);
        }
        n >>= 1;
        rep <<= 1;
    }

    const m = bins.length;
    let prefix: number[] = Array(m).fill(1);
    prefix[0] = bins[0] % mod;

    for (let i = 1; i < m; i++) {
        prefix[i] = (prefix[i - 1] * bins[i]) % mod;
    }

    function modInv(x: number): number {
        return powMod(x, mod - 2, mod); // Fermat's little theorem
    }

    function powMod(base: number, exp: number, mod: number): number {
        let result = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) !== 0) result = (result * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }

    let ans: number[] = [];
    for (let [left, right] of queries) {
        if (left === 0) {
            ans.push(prefix[right]);
        } else {
            ans.push((prefix[right] * modInv(prefix[left - 1])) % mod);
        }
    }

    return ans;
}
