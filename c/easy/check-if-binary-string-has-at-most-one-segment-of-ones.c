#include <stdbool.h>

bool checkOnesSegment(const char *s) {
    for (int i = 1; s[i] != '\0'; i++) {
        if (s[i - 1] == '0' && s[i] == '1') {
            return false;
        }
    }
    return true;
}