#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int mostBooked(int n, vector<vector<int>>& meetings) {
    sort(meetings.begin(), meetings.end());

    priority_queue<int, vector<int>, greater<int>> freeRooms;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> busyRooms;

    for (int i = 0; i < n; i++) freeRooms.push(i);

    vector<int> count(n, 0);

    for (auto& m : meetings) {
        long long start = m[0], end = m[1];
        long long duration = end - start;

        while (!busyRooms.empty() && busyRooms.top().first <= start) {
            freeRooms.push(busyRooms.top().second);
            busyRooms.pop();
        }

        int room;
        if (!freeRooms.empty()) {
            room = freeRooms.top();
            freeRooms.pop();
            busyRooms.push({end, room});
        } else {
            auto [finish, r] = busyRooms.top();
            busyRooms.pop();
            room = r;
            busyRooms.push({finish + duration, room});
        }
        count[room]++;
    }

    return max_element(count.begin(), count.end()) - count.begin();
}
