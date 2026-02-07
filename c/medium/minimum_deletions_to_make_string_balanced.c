#include <stdio.h>

int minimumDeletions(char* s) {
    int min_deletions = 0;
    int b_before_a = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'b') {
            b_before_a++;
        } else if (b_before_a > 0) {
            min_deletions++;
            b_before_a--;
        }
    }

    return min_deletions;
}
