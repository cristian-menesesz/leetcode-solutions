# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

# You can move according to these rules:

# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.
 

# Example 1:


# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds
# Example 2:

# Input: points = [[3,2],[-2,2]]
# Output: 5
 

# Constraints:

# points.length == n
# 1 <= n <= 100
# points[i].length == 2
# -1000 <= points[i][0], points[i][1] <= 1000


def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
    
    total_time = 0
    
    for i in range(len(points) - 1):

        (x1, y1), (x2, y2) = points[i], points[i + 1]

        total_time += max(abs(x2 - x1), abs(y2 - y1))

    return total_time


# solution worked on top of a greedy distance-accumulation approach, where the optimal path between consecutive points is determined by the dominant axis displacement

# 1. the movement between two consecutive points is independent of all other movements, meaning the total time is the sum of optimal local transitions
# 2. as diagonal movement is allowed, the minimal time between two points is governed by the maximum of the horizontal and vertical distances, not their sum
# 3. each step directly computes the optimal cost without requiring backtracking, memoization, or future-state dependency

# [!] notice that no intermediate points need to be simulated, since the distance formula already encodes the fastest path using diagonal and axis-aligned moves
# [!] notice that this approach relies on the problem guarantee that all points must be visited in the given order, otherwise a different strategy would be required

# this leads to a linear pass over the input, accumulating the Chebyshev distance between consecutive points to build the final answer


# time complexity: O(n) -> single traversal of the points list
# space complexity: O(1) -> constant extra space usage