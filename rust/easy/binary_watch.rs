impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        if turned_on == 0 {
            return vec!["0:00".to_string()];
        }

        let minute_mask = (1 << 6) - 1;
        let mut combination = (1 << turned_on) - 1;
        let max_combination = combination << (10 - turned_on);

        let mut valid_times = Vec::new();

        while combination <= max_combination {
            let minutes = combination & minute_mask;
            let hours = combination >> 6;

            if hours < 12 && minutes < 60 {
                valid_times.push(format!("{}:{:02}", hours, minutes));
            }

            // Gosper's Hack
            let lowest_set_bit = combination & -combination;
            let next_value = combination + lowest_set_bit;
            combination =
                (((combination ^ next_value) / lowest_set_bit) >> 2) | next_value;
        }

        valid_times
    }
}
