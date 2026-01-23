#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int sum;
    int idx;
} HeapNode;

typedef struct {
    HeapNode *data;
    int size;
    int capacity;
} MinHeap;

MinHeap* createHeap(int capacity) {
    MinHeap *heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->data = (HeapNode*)malloc(capacity * sizeof(HeapNode));
    heap->size = 0;
    heap->capacity = capacity;
    return heap;
}

void swap(HeapNode *a, HeapNode *b) {
    HeapNode temp = *a;
    *a = *b;
    *b = temp;
}

void heapifyUp(MinHeap *heap, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) / 2;
        if (heap->data[idx].sum < heap->data[parent].sum) {
            swap(&heap->data[idx], &heap->data[parent]);
            idx = parent;
        } else {
            break;
        }
    }
}

void heapifyDown(MinHeap *heap, int idx) {
    while (1) {
        int smallest = idx;
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;
        
        if (left < heap->size && heap->data[left].sum < heap->data[smallest].sum)
            smallest = left;
        if (right < heap->size && heap->data[right].sum < heap->data[smallest].sum)
            smallest = right;
        
        if (smallest != idx) {
            swap(&heap->data[idx], &heap->data[smallest]);
            idx = smallest;
        } else {
            break;
        }
    }
}

void heapPush(MinHeap *heap, int sum, int idx) {
    heap->data[heap->size].sum = sum;
    heap->data[heap->size].idx = idx;
    heapifyUp(heap, heap->size);
    heap->size++;
}

HeapNode heapPop(MinHeap *heap) {
    HeapNode result = heap->data[0];
    heap->size--;
    heap->data[0] = heap->data[heap->size];
    heapifyDown(heap, 0);
    return result;
}

bool isNonDecreasing(int *nums, int n) {
    for (int i = 0; i < n - 1; i++) {
        if (nums[i] > nums[i + 1])
            return false;
    }
    return true;
}

int minimumPairRemoval(int* nums, int numsSize) {
    int n = numsSize;
    
    if (isNonDecreasing(nums, n))
        return 0;
    
    bool *removed = (bool*)calloc(n, sizeof(bool));
    int *prev_idx = (int*)malloc(n * sizeof(int));
    int *next_idx = (int*)malloc(n * sizeof(int));
    
    for (int i = 0; i < n; i++) {
        prev_idx[i] = i - 1;
        next_idx[i] = (i + 1 < n) ? i + 1 : -1;
    }
    
    MinHeap *heap = createHeap(n * 3);
    
    for (int i = 0; i < n - 1; i++) {
        heapPush(heap, nums[i] + nums[i + 1], i);
    }
    
    int violations = 0;
    for (int i = 0; i < n - 1; i++) {
        if (nums[i] > nums[i + 1])
            violations++;
    }
    
    int operations = 0;
    
    while (violations > 0 && heap->size > 0) {
        HeapNode node = heapPop(heap);
        int pair_sum = node.sum;
        int left = node.idx;
        
        if (removed[left] || next_idx[left] == -1)
            continue;
        
        int right = next_idx[left];
        
        if (removed[right] || nums[left] + nums[right] != pair_sum)
            continue;
        
        int left_prev = prev_idx[left];
        int right_next = next_idx[right];
        
        if (left_prev != -1 && nums[left_prev] > nums[left])
            violations--;
        if (nums[left] > nums[right])
            violations--;
        if (right_next != -1 && nums[right] > nums[right_next])
            violations--;
        
        nums[left] = pair_sum;
        removed[right] = true;
        
        next_idx[left] = right_next;
        if (right_next != -1)
            prev_idx[right_next] = left;
        
        if (left_prev != -1 && nums[left_prev] > nums[left])
            violations++;
        if (right_next != -1 && nums[left] > nums[right_next])
            violations++;
        
        if (left_prev != -1)
            heapPush(heap, nums[left_prev] + nums[left], left_prev);
        if (right_next != -1)
            heapPush(heap, nums[left] + nums[right_next], left);
        
        operations++;
    }
    
    free(removed);
    free(prev_idx);
    free(next_idx);
    free(heap->data);
    free(heap);
    
    return operations;
}
