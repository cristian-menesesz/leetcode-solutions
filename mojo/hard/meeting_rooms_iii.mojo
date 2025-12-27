fn mostBooked(n: Int, meetings: List[List[Int]]) -> Int:
    
    meetings.sort(key=lambda x: x[0])

    var free_rooms = MinHeap[Int]()
    var busy_rooms = MinHeap[(Int, Int)]()
    var count = [0] * n

    for i in range(n):
        free_rooms.push(i)

    for m in meetings:
        let start = m[0]
        let end = m[1]
        let dur = end - start

        while busy_rooms and busy_rooms.peek()[0] <= start:
            let (_, r) = busy_rooms.pop()
            free_rooms.push(r)

        var room: Int
        if free_rooms:
            room = free_rooms.pop()
            busy_rooms.push((end, room))
        else:
            let (t, r) = busy_rooms.pop()
            room = r
            busy_rooms.push((t + dur, room))

        count[room] += 1

    return argmax(count)
