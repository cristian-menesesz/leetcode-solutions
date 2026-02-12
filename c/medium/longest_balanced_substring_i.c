#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int longestBalanced(char* s) {
    int length = strlen(s);
    int longest_length = 1;

    for (int left = 0; left < length; left++) {

        int char_frequency[26] = {0};
        int distinct_count = 0;
        int max_frequency = 0;
        int num_chars_with_max_frequency = 0;

        for (int right = left; right < length; right++) {

            int char_index = s[right] - 'a';
            char_frequency[char_index]++;
            int current_frequency = char_frequency[char_index];

            if (current_frequency == 1)
                distinct_count++;

            if (current_frequency > max_frequency) {
                max_frequency = current_frequency;
                num_chars_with_max_frequency = 1;
            } else if (current_frequency == max_frequency) {
                num_chars_with_max_frequency++;
            }

            if (distinct_count == num_chars_with_max_frequency) {
                longest_length = max(longest_length, right - left + 1);
            }
        }
    }

    return longest_length;
}
