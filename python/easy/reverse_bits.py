# Reverse bits of a given 32 bits signed integer.

 

# Example 1:

# Input: n = 43261596

# Output: 964176192

# Explanation:

# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000
# Example 2:

# Input: n = 2147483644

# Output: 1073741822

# Explanation:

# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110
 

# Constraints:

# 0 <= n <= 231 - 2
# n is even.
 

# Follow up: If this function is called many times, how would you optimize it?


def reverseBits(self, n: int) -> int:
    
    result = 0
    
    for i in range(32):
        
        result = (result << 1) | (n & 1)
        n = n >> 1
    
    return result


# solution worked on top of a bit manipulation iterative shifting approach, it has been taken into account three main principles of the problem:

# 1. as the integer is composed of 32 bits, it is possible to process it deterministically by iterating exactly 32 times, independently of the input value
# 2. at each iteration, the least significant bit (LSB) of n can be isolated using (n & 1), which allows extracting bits from right to left
# 3. the reversed number can be constructed progressively by shifting the result to the left and inserting the extracted bit into the least significant position

# [!] notice that the reconstruction is performed in reverse order because the original LSB becomes the most significant bit (MSB) in the result
# [!] as the number of bits is fixed (32), the loop does not depend on input magnitude, making the procedure constant in time

# this leads to the progressive extraction of bits from n and their mirrored insertion into result, effectively reversing the 32-bit representation


# time complexity: O(1) -> fixed 32 iterations
# space complexity: O(1) -> constant extra space
