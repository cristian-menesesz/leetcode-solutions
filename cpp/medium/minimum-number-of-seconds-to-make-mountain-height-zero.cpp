#include <vector>
#include <cmath>
using namespace std;

class Solution {
private:
    long long maxHeightInTime(long long time, const vector<int>& workerTimes) {
        long long totalHeight = 0;

        for (long long workerTime : workerTimes) {
            long long limit = (8LL * time) / workerTime + 1;
            long long k = ((long long)sqrt(limit) - 1) / 2;
            totalHeight += k;
        }

        return totalHeight;
    }

public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {

        if (workerTimes.size() == 1) {
            long long w = workerTimes[0];
            return w * (long long)mountainHeight * (mountainHeight + 1) / 2;
        }

        long long left = 1;
        long long right = (1000000000000LL * mountainHeight) / workerTimes.size();

        while (left < right) {
            long long mid = left + (right - left) / 2;

            if (maxHeightInTime(mid, workerTimes) >= mountainHeight)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
};