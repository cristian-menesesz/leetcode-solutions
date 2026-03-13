# You are given an integer mountainHeight denoting the height of a mountain.

# You are also given an integer array workerTimes representing the work time of workers in seconds.

# The workers work simultaneously to reduce the height of the mountain. For worker i:

# To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
# To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
# To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
# Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.

 

# Example 1:

# Input: mountainHeight = 4, workerTimes = [2,1,1]

# Output: 3

# Explanation:

# One way the height of the mountain can be reduced to 0 is:

# Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
# Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds.
# Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
# Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.

# Example 2:

# Input: mountainHeight = 10, workerTimes = [3,2,2,4]

# Output: 12

# Explanation:

# Worker 0 reduces the height by 2, taking workerTimes[0] + workerTimes[0] * 2 = 9 seconds.
# Worker 1 reduces the height by 3, taking workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 seconds.
# Worker 2 reduces the height by 3, taking workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 seconds.
# Worker 3 reduces the height by 2, taking workerTimes[3] + workerTimes[3] * 2 = 12 seconds.
# The number of seconds needed is max(9, 12, 12, 12) = 12 seconds.

# Example 3:

# Input: mountainHeight = 5, workerTimes = [1]

# Output: 15

# Explanation:

# There is only one worker in this example, so the answer is workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15.

 

# Constraints:

# 1 <= mountainHeight <= 105
# 1 <= workerTimes.length <= 104
# 1 <= workerTimes[i] <= 106


from math import isqrt

def _max_height_in_time(self, time: int, worker_times: list[int]) -> int:
    """
    Returns the maximum mountain height that can be reduced
    by all workers within the given time.
    """
    
    total_height = 0

    for worker_time in worker_times:
        # Solve k(k+1)/2 * worker_time <= time
        # => k = floor((sqrt(1 + 8*time/worker_time) - 1) / 2)

        limit = (8 * time) // worker_time + 1
        k = (isqrt(limit) - 1) // 2
        total_height += k

    return total_height

def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
    """
    Finds the minimum time required to reduce the mountain
    height using the given workers.
    """

    # Fast path for single worker
    if len(workerTimes) == 1:
        w = workerTimes[0]
        return w * mountainHeight * (mountainHeight + 1) // 2

    left = 1
    right = (10**12 * mountainHeight) // len(workerTimes)

    while left < right:
        mid = (left + right) // 2

        if self._max_height_in_time(mid, workerTimes) >= mountainHeight:
            right = mid
        else:
            left = mid + 1

    return left


# solution worked on top of a parametric search (binary search on the answer) combined with a mathematical inversion of the triangular work relation, exploiting the monotonic growth of achievable work with respect to time

# 1. the total height a worker can reduce in time t follows the relation worker_time * (k(k+1)/2) <= t, meaning the time needed grows according to a triangular number sequence
# 2. by algebraically inverting the triangular relation it is possible to compute directly the maximum k (units of height reduced) a worker can complete within a given time, avoiding iterative simulation
# 3. since the total reducible height across all workers increases monotonically with respect to time, the minimum feasible time can be located using binary search over the time domain
# 4. each step of the search evaluates a candidate time by summing the maximum work achievable by every worker using the closed-form solution

# [!] notice that the triangular work relation models the increasing cost of removing successive height units, making the work non-linear in time
# [!] as the achievable height function is monotonic in time, binary search guarantees convergence to the minimum feasible time

# this leads to repeatedly testing candidate times through the mathematical inversion of the triangular constraint and accumulating the total height reduced by all workers until the minimum valid time is identified


# time complexity: O(n log T) -> binary search over time (log T) * worker evaluation (n)
# space complexity: O(1) -> constant auxiliary space
