#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int time;
    int room;
} Pair;

typedef struct {
    Pair* data;
    int size;
} Heap;

void heap_push(Heap* h, Pair p) {
    int i = h->size++;
    h->data[i] = p;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (h->data[parent].time <= h->data[i].time) break;
        Pair tmp = h->data[parent];
        h->data[parent] = h->data[i];
        h->data[i] = tmp;
        i = parent;
    }
}

Pair heap_pop(Heap* h) {
    Pair res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2*i + 1, r = 2*i + 2, smallest = i;
        if (l < h->size && h->data[l].time < h->data[smallest].time)
            smallest = l;
        if (r < h->size && h->data[r].time < h->data[smallest].time)
            smallest = r;
        if (smallest == i) break;
        Pair tmp = h->data[i];
        h->data[i] = h->data[smallest];
        h->data[smallest] = tmp;
        i = smallest;
    }
    return res;
}

int mostBooked(int n, int** meetings, int meetingsSize, int* meetingsColSize){
    Heap free_rooms = {malloc(n * sizeof(Pair)), 0};
    Heap busy_rooms = {malloc(meetingsSize * sizeof(Pair)), 0};
    for (int i = 0; i < n; i++) {
        heap_push(&free_rooms, (Pair){0, i});
    }
    
    int* booking_count = calloc(n, sizeof(int));
    
    // Sort meetings by start time
    for (int i = 0; i < meetingsSize - 1; i++) {
        for (int j = i + 1; j < meetingsSize; j++) {
            if (meetings[i][0] > meetings[j][0]) {
                int* temp = meetings[i];
                meetings[i] = meetings[j];
                meetings[j] = temp;
            }
        }
    }
    
    for (int i = 0; i < meetingsSize; i++) {
        int start = meetings[i][0];
        int end = meetings[i][1];
        
        while (busy_rooms.size > 0 && busy_rooms.data[0].time <= start) {
            Pair freed_room = heap_pop(&busy_rooms);
            heap_push(&free_rooms, (Pair){0, freed_room.room});
        }
        
        if (free_rooms.size > 0) {
            Pair room = heap_pop(&free_rooms);
            booking_count[room.room]++;
            heap_push(&busy_rooms, (Pair){end, room.room});
        } else {
            Pair room = heap_pop(&busy_rooms);
            int new_end = room.time + (end - start);
            booking_count[room.room]++;
            heap_push(&busy_rooms, (Pair){new_end, room.room});
        }
    }
    
    free(free_rooms.data);
    free(busy_rooms.data);
    
    int max_bookings = 0;
    int result_room = 0;
    for (int i = 0; i < n; i++) {
        if (booking_count[i] > max_bookings) {
            max_bookings = booking_count[i];
            result_room = i;
        }
    }
    free(booking_count);
    return result_room;
}