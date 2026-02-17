#include <stdio.h>
#include <stdlib.h>

char** readBinaryWatch(int turnedOn, int* returnSize) {
    if (turnedOn == 0) {
        char** result = malloc(sizeof(char*));
        result[0] = malloc(6);
        sprintf(result[0], "0:00");
        *returnSize = 1;
        return result;
    }

    int MINUTE_MASK = (1 << 6) - 1;
    int combination = (1 << turnedOn) - 1;
    int max_combination = combination << (10 - turnedOn);

    char** result = malloc(1024 * sizeof(char*));
    int count = 0;

    while (combination <= max_combination) {
        int minutes = combination & MINUTE_MASK;
        int hours = combination >> 6;

        if (hours < 12 && minutes < 60) {
            result[count] = malloc(6);
            sprintf(result[count], "%d:%02d", hours, minutes);
            count++;
        }

        // Gosper's Hack
        int lowest_set_bit = combination & -combination;
        int next_value = combination + lowest_set_bit;
        combination = (((combination ^ next_value) / lowest_set_bit) >> 2) | next_value;
    }

    *returnSize = count;
    return result;
}
