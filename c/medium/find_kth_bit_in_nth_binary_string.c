#include <stdio.h>

// Recursive function
char findKthBit(int n, int k) {
    // Base case: S1 = "0"
    if (k == 1)
        return '0';

    // Compute bit length of k
    int bit_size = 0;
    int temp = k;
    while (temp > 0) {
        bit_size++;
        temp >>= 1;
    }

    // Mirror index across power-of-two boundary
    int mirrored_index = (1 << bit_size) - k;

    // Symmetry center
    if (mirrored_index == k)
        return '1';

    // Recursive call
    char mirrored_bit = findKthBit(n, mirrored_index);

    // Invert bit
    return (mirrored_bit == '1') ? '0' : '1';
}