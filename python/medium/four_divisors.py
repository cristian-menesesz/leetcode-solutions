# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# Example 2:

# Input: nums = [21,21]
# Output: 64
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105


def sumFourDivisors(self, nums: list[int]) -> int:

    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317
    ]
    total_sum = 0

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        sqrt_n = int(n**0.5)

        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
            
        return True
    
    for x in nums:
        if x <= 1:
            continue
        
        sqrt_x = int(x**0.5)
        
        for prime in primes:
            if prime > sqrt_x:
                break
            
            if x % prime == 0:
                quotient = x // prime
                
                if quotient != prime and is_prime(quotient):
                    total_sum += 1 + prime + quotient + x
                    break
                
                if quotient == prime * prime:
                    total_sum += 1 + prime + quotient + x
                    break
    
    return total_sum


# solution worked on top of number theory and prime factorization properties, it has been taken into account three main principles of the problem:

# 1. a number has exactly four divisors only if it's either the cube of a prime (p³) or the product of two distinct primes (p × q)
# 2. for p³ form: divisors are {1, p, p², p³}, and for p × q form: divisors are {1, p, q, p×q}, both yielding exactly four divisors
# 3. by checking if a number is divisible by a precomputed prime and verifying the quotient's properties (either equal to prime squared or being a distinct prime), we can identify numbers with exactly four divisors efficiently

# [!] notice that the algorithm breaks immediately after finding the first valid prime divisor, as numbers with exactly four divisors have at most two distinct prime factors
# [!] the precomputed prime list up to 317 covers all possible prime factors for numbers up to 10^5 (since sqrt(10^5) ≈ 316.23)

# this leads to iterating through each number, checking divisibility by precomputed primes up to its square root, and validating if the quotient forms either p³ or p×q pattern


# time complexity: O(n × π(√m)) where n is the length of nums and π(√m) is the count of primes up to sqrt of max value ≈ O(n)
# space complexity: O(1) -> precomputed prime list is constant size and doesn't scale with input