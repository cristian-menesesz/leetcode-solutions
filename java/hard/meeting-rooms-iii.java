import java.util.*;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(a -> a[0]));

        PriorityQueue<Integer> free = new PriorityQueue<>();
        PriorityQueue<long[]> busy = new PriorityQueue<>(
            (a,b) -> a[0] == b[0] ? Long.compare(a[1], b[1]) : Long.compare(a[0], b[0])
        );

        for (int i = 0; i < n; i++) free.add(i);
        int[] count = new int[n];

        for (int[] m : meetings) {
            long start = m[0], end = m[1];
            long dur = end - start;

            while (!busy.isEmpty() && busy.peek()[0] <= start) {
                free.add((int)busy.poll()[1]);
            }

            int room;
            if (!free.isEmpty()) {
                room = free.poll();
                busy.add(new long[]{end, room});
            } else {
                long[] r = busy.poll();
                room = (int)r[1];
                busy.add(new long[]{r[0] + dur, room});
            }
            count[room]++;
        }

        int res = 0;
        for (int i = 1; i < n; i++)
            if (count[i] > count[res]) res = i;
        return res;
    }
}
