from math import isqrt

fn max_height_in_time(time: Int, worker_times: List[Int]) -> Int:
    var total_height: Int = 0

    for worker_time in worker_times:
        var limit = (8 * time) // worker_time + 1
        var k = (isqrt(limit) - 1) // 2
        total_height += k

    return total_height


fn min_number_of_seconds(mountain_height: Int, worker_times: List[Int]) -> Int:

    if len(worker_times) == 1:
        var w = worker_times[0]
        return w * mountain_height * (mountain_height + 1) // 2

    var left: Int = 1
    var right: Int = (10**12 * mountain_height) // len(worker_times)

    while left < right:
        var mid = (left + right) // 2

        if max_height_in_time(mid, worker_times) >= mountain_height:
            right = mid
        else:
            left = mid + 1

    return left