#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int x;
    int y;
    int index;
} Entry;

typedef struct {
    Entry* data;
    int size;
    int capacity;
} Map;

void map_init(Map* map, int capacity) {
    map->data = (Entry*)malloc(sizeof(Entry) * capacity);
    map->size = 0;
    map->capacity = capacity;
}

void map_free(Map* map) {
    free(map->data);
}

int map_get(Map* map, int x, int y, int* out) {
    for (int i = 0; i < map->size; i++) {
        if (map->data[i].x == x && map->data[i].y == y) {
            *out = map->data[i].index;
            return 1;
        }
    }
    return 0;
}

void map_put(Map* map, int x, int y, int index) {
    if (map->size < map->capacity) {
        map->data[map->size++] = (Entry){x, y, index};
    }
}

int longest_single_char_run(const char* s) {
    int n = strlen(s);
    if (n == 0) return 0;

    int max_run = 1;
    int current_run = 1;

    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) {
            current_run++;
        } else {
            if (current_run > max_run)
                max_run = current_run;
            current_run = 1;
        }
    }

    if (current_run > max_run)
        max_run = current_run;

    return max_run;
}

int longestBalanced(const char* s) {
    int n = strlen(s);
    if (n == 0) return 0;

    int max_length = longest_single_char_run(s);

    Map seen_abc, seen_ab, seen_bc, seen_ca;
    map_init(&seen_abc, n + 1);
    map_init(&seen_ab, n + 1);
    map_init(&seen_bc, n + 1);
    map_init(&seen_ca, n + 1);

    map_put(&seen_abc, 0, 0, -1);
    map_put(&seen_ab, 0, 0, -1);
    map_put(&seen_bc, 0, 0, -1);
    map_put(&seen_ca, 0, 0, -1);

    int count_a = 0, count_b = 0, count_c = 0;

    for (int i = 0; i < n; i++) {
        if (s[i] == 'a') count_a++;
        else if (s[i] == 'b') count_b++;
        else count_c++;

        int A = count_a, B = count_b, C = count_c;
        int prev_index;

        // A = B = C
        if (map_get(&seen_abc, B - A, C - A, &prev_index)) {
            if (i - prev_index > max_length)
                max_length = i - prev_index;
        } else {
            map_put(&seen_abc, B - A, C - A, i);
        }

        // A = B, no C
        if (map_get(&seen_ab, A - B, C, &prev_index)) {
            if (i - prev_index > max_length)
                max_length = i - prev_index;
        } else {
            map_put(&seen_ab, A - B, C, i);
        }

        // B = C, no A
        if (map_get(&seen_bc, B - C, A, &prev_index)) {
            if (i - prev_index > max_length)
                max_length = i - prev_index;
        } else {
            map_put(&seen_bc, B - C, A, i);
        }

        // C = A, no B
        if (map_get(&seen_ca, C - A, B, &prev_index)) {
            if (i - prev_index > max_length)
                max_length = i - prev_index;
        } else {
            map_put(&seen_ca, C - A, B, i);
        }
    }

    map_free(&seen_abc);
    map_free(&seen_ab);
    map_free(&seen_bc);
    map_free(&seen_ca);

    return max_length;
}


// beats 96% - 796ms

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 100000

// ---------- Utility max ----------
int max(int a, int b) {
    return a > b ? a : b;
}

// ---------- 2-character balanced ----------
int longest_two_balanced(const char* s, int n, char c1, char c2) {
    int balance = 0;
    int max_length = 0;
    int last_invalid = -1;

    // Since balance range is [-n, n], we shift by n
    int* first = (int*)malloc(sizeof(int) * (2*n + 1));
    for (int i = 0; i <= 2*n; i++) first[i] = -2;

    first[n] = -1; // balance 0 at index -1

    for (int i = 0; i < n; i++) {
        char ch = s[i];

        if (ch != c1 && ch != c2) {
            balance = 0;
            for (int j = 0; j <= 2*n; j++) first[j] = -2;
            first[n] = i;
            last_invalid = i;
            continue;
        }

        if (ch == c1) balance++;
        else balance--;

        int idx = balance + n;

        if (first[idx] != -2) {
            max_length = max(max_length, i - first[idx]);
        } else {
            first[idx] = i;
        }
    }

    free(first);
    return max_length;
}

// ---------- 3-character balanced ----------
typedef struct {
    int x;
    int y;
    int index;
} Pair;

int longest_three_balanced(const char* s, int n) {
    int count_a = 0, count_b = 0, count_c = 0;
    int max_length = 0;

    Pair* states = (Pair*)malloc(sizeof(Pair) * (2*n + 1));
    int size = 0;

    states[size++] = (Pair){0, 0, -1};

    for (int i = 0; i < n; i++) {
        if (s[i] == 'a') count_a++;
        else if (s[i] == 'b') count_b++;
        else count_c++;

        int x = count_b - count_a;
        int y = count_c - count_a;

        int found = 0;
        for (int j = 0; j < size; j++) {
            if (states[j].x == x && states[j].y == y) {
                max_length = max(max_length, i - states[j].index);
                found = 1;
                break;
            }
        }

        if (!found) {
            states[size++] = (Pair){x, y, i};
        }
    }

    free(states);
    return max_length;
}

// ---------- Main function ----------
int longestBalanced(const char* s) {
    int n = strlen(s);
    if (n == 0) return 0;

    // 1) Longest single run
    int max_run = 1, current = 1;
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i-1]) current++;
        else {
            max_run = max(max_run, current);
            current = 1;
        }
    }
    max_run = max(max_run, current);

    int result = max_run;

    // 2) Two-character balanced
    result = max(result, longest_two_balanced(s, n, 'a', 'b'));
    result = max(result, longest_two_balanced(s, n, 'a', 'c'));
    result = max(result, longest_two_balanced(s, n, 'b', 'c'));

    // 3) Three-character balanced
    result = max(result, longest_three_balanced(s, n));

    return result;
}
