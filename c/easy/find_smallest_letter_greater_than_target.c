#include <stddef.h>

char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int left = 0, right = lettersSize;

    // binary search: upper_bound
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (letters[mid] <= target)
            left = mid + 1;
        else
            right = mid;
    }

    return (left < lettersSize) ? letters[left] : letters[0];
}
