#include <string.h>

int minOperations(const char *s) {
    int mismatches_starting_with_zero = 0;
    int length = strlen(s);

    for (int index = 0; index < length; index++) {
        mismatches_starting_with_zero += ((s[index] & 1) ^ index) & 1;
    }

    int mismatches_starting_with_one = length - mismatches_starting_with_zero;

    return mismatches_starting_with_zero < mismatches_starting_with_one
        ? mismatches_starting_with_zero
        : mismatches_starting_with_one;
}