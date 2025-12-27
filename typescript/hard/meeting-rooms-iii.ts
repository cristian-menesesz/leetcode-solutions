// Min-heap implementation for TypeScript
class MinHeap<T> {
    private heap: T[] = [];

    constructor(private compareFn: (a: T, b: T) => number) {}

    push(item: T): void {
        this.heap.push(item);
        this.bubbleUp(this.heap.length - 1);
    }

    pop(): T | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const root = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.bubbleDown(0);
        return root;
    }

    peek(): T | undefined {
        return this.heap[0];
    }

    get size(): number {
        return this.heap.length;
    }

    private bubbleUp(index: number): void {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.compareFn(this.heap[index], this.heap[parentIndex]) >= 0)
                break;

            [this.heap[index], this.heap[parentIndex]] = [
                this.heap[parentIndex],
                this.heap[index],
            ];
            index = parentIndex;
        }
    }

    private bubbleDown(index: number): void {
        while (true) {
            let smallest = index;
            const leftChild = 2 * index + 1;
            const rightChild = 2 * index + 2;

            if (
                leftChild < this.heap.length &&
                this.compareFn(this.heap[leftChild], this.heap[smallest]) < 0
            ) {
                smallest = leftChild;
            }

            if (
                rightChild < this.heap.length &&
                this.compareFn(this.heap[rightChild], this.heap[smallest]) < 0
            ) {
                smallest = rightChild;
            }

            if (smallest === index) break;

            [this.heap[index], this.heap[smallest]] = [
                this.heap[smallest],
                this.heap[index],
            ];
            index = smallest;
        }
    }
}

interface BusyRoom {
    finishTime: number;
    roomId: number;
}

function mostBooked(n: number, meetings: number[][]): number {
    // Sort meetings by start time
    meetings.sort((a, b) => a[0] - b[0]);

    // Initialize free rooms heap (min-heap by room number)
    const freeRooms = new MinHeap<number>((a, b) => a - b);
    for (let i = 0; i < n; i++) {
        freeRooms.push(i);
    }

    // Initialize busy rooms heap (min-heap by finish time, then by room id)
    const busyRooms = new MinHeap<BusyRoom>((a, b) => {
        if (a.finishTime !== b.finishTime) {
            return a.finishTime - b.finishTime;
        }
        return a.roomId - b.roomId;
    });

    // Initialize booking count
    const bookingCount = new Array(n).fill(0);

    // Process each meeting
    for (const [start, end] of meetings) {
        const duration = end - start;

        // Release rooms that finished before current meeting starts
        while (busyRooms.size > 0 && busyRooms.peek()!.finishTime <= start) {
            const { roomId } = busyRooms.pop()!;
            freeRooms.push(roomId);
        }

        let roomId: number;

        if (freeRooms.size > 0) {
            // Assign to free room with lowest number
            roomId = freeRooms.pop()!;
            busyRooms.push({ finishTime: end, roomId });
        } else {
            // Delay meeting to earliest finishing room
            const { finishTime, roomId: busyRoomId } = busyRooms.pop()!;
            roomId = busyRoomId;
            busyRooms.push({
                finishTime: finishTime + duration,
                roomId,
            });
        }

        bookingCount[roomId]++;
    }

    // Find room with maximum bookings (return lowest number if tie)
    let maxBookings = 0;
    let result = 0;

    for (let i = 0; i < n; i++) {
        if (bookingCount[i] > maxBookings) {
            maxBookings = bookingCount[i];
            result = i;
        }
    }

    return result;
}
