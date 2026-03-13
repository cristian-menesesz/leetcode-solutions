using System;
using System.Collections.Generic;

public class Solution
{
    private long MaxHeightInTime(long time, IList<int> workerTimes)
    {
        long totalHeight = 0;

        foreach (long workerTime in workerTimes)
        {
            long limit = (8 * time) / workerTime + 1;
            long k = ((long)Math.Sqrt(limit) - 1) / 2;
            totalHeight += k;
        }

        return totalHeight;
    }

    public long MinNumberOfSeconds(int mountainHeight, IList<int> workerTimes)
    {
        if (workerTimes.Count == 1)
        {
            long w = workerTimes[0];
            return w * mountainHeight * (mountainHeight + 1L) / 2;
        }

        long left = 1;
        long right = (1000000000000L * mountainHeight) / workerTimes.Count;

        while (left < right)
        {
            long mid = left + (right - left) / 2;

            if (MaxHeightInTime(mid, workerTimes) >= mountainHeight)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
}