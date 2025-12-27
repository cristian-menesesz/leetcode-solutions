int MostBooked(int n, int[][] meetings) {
    
    Array.Sort(meetings, (a, b) => a[0] - b[0]);

    var free = new PriorityQueue<int, int>();
    var busy = new PriorityQueue<(long,long), long>();

    for (int i = 0; i < n; i++) free.Enqueue(i, i);

    int[] count = new int[n];

    foreach (var m in meetings) {
        long start = m[0], end = m[1];
        long dur = end - start;

        while (busy.Count > 0 && busy.Peek().Item1 <= start) {
            var (_, r) = busy.Dequeue();
            free.Enqueue(r, r);
        }

        int room;
        if (free.Count > 0) {
            room = free.Dequeue();
            busy.Enqueue((end, room), end);
        } else {
            var (finish, r) = busy.Dequeue();
            room = r;
            busy.Enqueue((finish + dur, room), finish + dur);
        }
        count[room]++;
    }

    int res = 0;
    for (int i = 1; i < n; i++)
        if (count[i] > count[res]) res = i;
    return res;
}
