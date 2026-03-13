fn max_height_in_time(time: u64, worker_times: &[u64]) -> u64 {
    worker_times.iter().map(|&worker_time| {
        let limit = (8 * time) / worker_time + 1;
        let k = (limit as f64).sqrt() as u64;
        (k - 1) / 2
    }).sum()
}

pub fn min_number_of_seconds(mountain_height: u64, worker_times: &[u64]) -> u64 {

    if worker_times.len() == 1 {
        let w = worker_times[0];
        return w * mountain_height * (mountain_height + 1) / 2;
    }

    let mut left: u64 = 1;
    let mut right: u64 = (1_000_000_000_000u64 * mountain_height) / worker_times.len() as u64;

    while left < right {
        let mid = left + (right - left) / 2;

        if max_height_in_time(mid, worker_times) >= mountain_height {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    left
}