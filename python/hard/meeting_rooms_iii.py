# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:

# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

# Example 1:

# Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
# Output: 0
# Explanation:
# - At time 0, both rooms are not being used. The first meeting starts in room 0.
# - At time 1, only room 1 is not being used. The second meeting starts in room 1.
# - At time 2, both rooms are being used. The third meeting is delayed.
# - At time 3, both rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
# - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
# Both rooms 0 and 1 held 2 meetings, so we return 0. 
# Example 2:

# Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
# Output: 1
# Explanation:
# - At time 1, all three rooms are not being used. The first meeting starts in room 0.
# - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
# - At time 3, only room 2 is not being used. The third meeting starts in room 2.
# - At time 4, all three rooms are being used. The fourth meeting is delayed.
# - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
# - At time 6, all three rooms are being used. The fifth meeting is delayed.
# - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
# Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
 

# Constraints:

# 1 <= n <= 100
# 1 <= meetings.length <= 105
# meetings[i].length == 2
# 0 <= starti < endi <= 5 * 105
# All the values of starti are unique.


import heapq
from typing import List


def mostBooked(n: int, meetings: List[List[int]]) -> int:

    meetings.sort(key=lambda m: m[0])
    free_rooms = list(range(n))
    heapq.heapify(free_rooms)
    busy_rooms = []
    booking_count = [0] * n

    for start, end in meetings:
        
        duration = end - start

        while busy_rooms and busy_rooms[0][0] <= start:
            _, room_id = heapq.heappop(busy_rooms)
            heapq.heappush(free_rooms, room_id)
        if free_rooms:
            room_id = heapq.heappop(free_rooms)
            heapq.heappush(busy_rooms, (end, room_id))
        else:
            finish_time, room_id = heapq.heappop(busy_rooms)
            heapq.heappush(
                busy_rooms,
                (finish_time + duration, room_id)
            )
        booking_count[room_id] += 1

    return booking_count.index(max(booking_count))


# solution works on top of a greedy scheduling strategy reinforced by priority queues (heaps), ensuring optimal room assignment while preserving ordering constraints imposed by time. it has been taken into account three main principles of the approach:

# 1. meetings are processed in chronological order (sorted by start time), so decisions are made greedily with full knowledge of all rooms that have become available up to that moment. this guarantees that no future meeting can invalidate a past optimal assignment.
# 2. room allocation is split into two independent states managed by heaps: free rooms are always selected by smallest room index (min-heap), busy rooms are always selected by earliest finishing time (min-heap). this enforces both the problem constraint (lowest-index room preference) and optimal reuse of rooms when delays are unavoidable.
# 3. when no room is available at a meeting's start time, the meeting is delayed to the earliest finishing room, extending its finish time by the original meeting duration. this preserves meeting order while minimizing the delay impact.

# [!] notice that rooms are released lazily: a room is only moved from busy to free when its finish time is less than or equal to the current meeting's start time. this avoids unnecessary heap operations and keeps the state consistent.
# [!] notice that the meeting duration is preserved even when delayed; only the start time shifts implicitly via the earliest available finish time.
# [!] the algorithm never scans rooms linearly; all decisions are made via heap tops, which ensures logarithmic-time operations per meeting.

# this leads to counting how many times each room is booked while simulating the real
# scheduling process, and finally selecting the room with the maximum number of bookings.


# time complexity: O(m log n) -> sorting meetings + heap operations per meeting
# space complexity: O(n) -> heaps and booking count arrays
