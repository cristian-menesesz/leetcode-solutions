class Solution {
    public int bitwiseComplement(int n) {
        if (n == 0) return 1;

        int bitLength = 32 - Integer.numberOfLeadingZeros(n);
        int mask = (1 << bitLength) - 1;

        return (~n) & mask;
    }
}
