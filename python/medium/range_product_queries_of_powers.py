# Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

# You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

 

# Example 1:

# Input: n = 15, queries = [[0,1],[2,2],[0,3]]
# Output: [2,4,64]
# Explanation:
# For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
# Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
# Answer to 2nd query: powers[2] = 4.
# Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
# Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.
# Example 2:

# Input: n = 2, queries = [[0,0]]
# Output: [2]
# Explanation:
# For n = 2, powers = [2].
# The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.
 

# Constraints:

# 1 <= n <= 109
# 1 <= queries.length <= 105
# 0 <= starti <= endi < powers.length


def productQueries(n: int, queries: list[list[int]]) -> list[int]:
    
    mod = 10**9 + 7
    bins, rep = [], 1

    while n > 0:
        if n & 1:
            bins.append(rep)
        n >>= 1
        rep <<= 1

    m = len(bins)

    prefix = [1] * m
    prefix[0] = bins[0] % mod
    for i in range(1, m):
        prefix[i] = (prefix[i-1] * bins[i]) % mod

    def mod_inv(x):
        return pow(x, mod - 2, mod)  # Fermat's little theorem

    ans = []
    for left, right in queries:
        if left == 0:
            ans.append(prefix[right])
        else:
            ans.append((prefix[right] * mod_inv(prefix[left-1])) % mod)

    return ans

def main():
    print(productQueries(15, [[0,1],[2,2],[0,3]]))
    print(productQueries(2, [[0,0]]))

if __name__ == "__main__":
    main()


# solution built on the principle of binary decomposition with prefix product optimization

# 1. binary decomposition for minimal powers array – n is decomposed into the minimal set of powers of two that sum exactly to n by inspecting its binary representation. Each set bit corresponds to a unique power of two, ensuring the smallest possible array length.
# 2. prefix product preprocessing for range queries – a prefix product array modulo 10^9 + 7 is computed so that each query for the product of powers in a given range can be answered in constant time using modular inverses.
# 3. modular inverse via Fermat's Little Theorem – instead of recomputing products for every query, the algorithm uses the modular inverse of the prefix up to left-1 to efficiently derive the product for any [left, right] range.

# [!] powers array is strictly derived from the binary representation of n, so it is both unique and minimal by definition.
# [!] the use of modular inverses is only valid because the modulus is prime, allowing Fermat’s theorem to apply.
# [!] prefix product computation is linear in the number of powers, independent of the number of queries.


# time complexity: O(log n + q) – binary decomposition: O(log n), prefix computation: O(log n), queries: O(q)
# space complexity: O(log n) – storage for powers array and prefix products 
