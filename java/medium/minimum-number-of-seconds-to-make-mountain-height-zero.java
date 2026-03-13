class Solution {

    private static long maxHeightInTime(long time, long[] workerTimes) {
        long totalHeight = 0;

        for (long workerTime : workerTimes) {
            long limit = (8 * time) / workerTime + 1;
            long k = ((long)Math.sqrt(limit) - 1) / 2;
            totalHeight += k;
        }

        return totalHeight;
    }

    public static long minNumberOfSeconds(long mountainHeight, long[] workerTimes) {

        if (workerTimes.length == 1) {
            long w = workerTimes[0];
            return w * mountainHeight * (mountainHeight + 1) / 2;
        }

        long left = 1;
        long right = (1_000_000_000_000L * mountainHeight) / workerTimes.length;

        while (left < right) {
            long mid = (left + right) / 2;

            if (maxHeightInTime(mid, workerTimes) >= mountainHeight) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}