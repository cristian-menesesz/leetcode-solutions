use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub fn most_booked(n: usize, mut meetings: Vec<Vec<i32>>) -> usize {
    meetings.sort_by_key(|m| m[0]);

    let mut free = BinaryHeap::new();
    let mut busy = BinaryHeap::new();

    for i in (0..n).rev() {
        free.push(i);
    }

    let mut count = vec![0; n];

    for m in meetings {
        let start = m[0] as i64;
        let end = m[1] as i64;
        let dur = end - start;

        while let Some(&Reverse((t, r))) = busy.peek() {
            if t > start { break; }
            busy.pop();
            free.push(r);
        }

        let room;
        if let Some(r) = free.pop() {
            room = r;
            busy.push(Reverse((end, room)));
        } else {
            let Reverse((t, r)) = busy.pop().unwrap();
            room = r;
            busy.push(Reverse((t + dur, room)));
        }
        count[room] += 1;
    }

    count.iter().enumerate().max_by_key(|(_,v)| *v).unwrap().0
}
