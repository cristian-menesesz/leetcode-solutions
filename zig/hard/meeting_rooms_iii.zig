const std = @import("std");
const Allocator = std.mem.Allocator;
const PriorityQueue = std.PriorityQueue;

const Meeting = struct {
    start: i32,
    end: i32,
};

const BusyRoom = struct {
    finish_time: i32,
    room_id: i32,
};

fn compareMeetings(_: void, a: Meeting, b: Meeting) bool {
    return a.start < b.start;
}

fn compareFreeRooms(_: void, a: i32, b: i32) std.math.Order {
    return std.math.order(a, b);
}

fn compareBusyRooms(_: void, a: BusyRoom, b: BusyRoom) std.math.Order {
    if (a.finish_time != b.finish_time) {
        return std.math.order(a.finish_time, b.finish_time);
    }
    return std.math.order(a.room_id, b.room_id);
}

pub fn mostBooked(allocator: Allocator, n: i32, meetings: []Meeting) !i32 {
    // Sort meetings by start time
    std.mem.sort(Meeting, meetings, {}, compareMeetings);
    
    // Initialize free rooms heap
    var free_rooms = PriorityQueue(i32, void, compareFreeRooms).init(allocator, {});
    defer free_rooms.deinit();
    
    var i: i32 = 0;
    while (i < n) : (i += 1) {
        try free_rooms.add(i);
    }
    
    // Initialize busy rooms heap
    var busy_rooms = PriorityQueue(BusyRoom, void, compareBusyRooms).init(allocator, {});
    defer busy_rooms.deinit();
    
    // Initialize booking count
    const booking_count = try allocator.alloc(i32, @intCast(n));
    defer allocator.free(booking_count);
    @memset(booking_count, 0);
    
    // Process each meeting
    for (meetings) |meeting| {
        const start = meeting.start;
        const end = meeting.end;
        const duration = end - start;
        
        // Release rooms that finished before current meeting starts
        while (busy_rooms.peek()) |top| {
            if (top.finish_time <= start) {
                const busy = busy_rooms.remove();
                try free_rooms.add(busy.room_id);
            } else {
                break;
            }
        }
        
        var room_id: i32 = undefined;
        
        if (free_rooms.peek()) |_| {
            // Assign to free room with lowest number
            room_id = free_rooms.remove();
            try busy_rooms.add(.{ .finish_time = end, .room_id = room_id });
        } else {
            // Delay meeting to earliest finishing room
            const busy = busy_rooms.remove();
            room_id = busy.room_id;
            try busy_rooms.add(.{
                .finish_time = busy.finish_time + duration,
                .room_id = room_id,
            });
        }
        
        booking_count[@intCast(room_id)] += 1;
    }
    
    // Find room with maximum bookings
    var max_bookings: i32 = 0;
    var result: i32 = 0;
    
    i = 0;
    while (i < n) : (i += 1) {
        if (booking_count[@intCast(i)] > max_bookings) {
            max_bookings = booking_count[@intCast(i)];
            result = i;
        }
    }
    
    return result;
}
