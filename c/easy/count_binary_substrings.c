#include <stdio.h>
#include <string.h>

int countBinarySubstrings(const char *s) {
    int total_substrings = 0;
    int previous_run_length = 0;
    int current_run_length = 1;
    int len = strlen(s);

    for (int i = 1; i < len; i++) {
        if (s[i] == s[i - 1]) {
            current_run_length++;
        } else {
            previous_run_length = current_run_length;
            current_run_length = 1;
        }

        if (current_run_length <= previous_run_length) {
            total_substrings++;
        }
    }

    return total_substrings;
}
