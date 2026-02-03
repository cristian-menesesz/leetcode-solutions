pub fn is_trionic(nums: &[i32]) -> bool {
    let n = nums.len();
    if n < 4 {
        return false;
    }
    if nums[0] >= nums[1] {
        return false;
    }

    let mut first_increase_finished = false;
    let mut decrease_finished = false;
    let mut increasing = true;

    for i in 1..n {
        if nums[i] == nums[i - 1] {
            return false;
        }

        if increasing {
            if nums[i] < nums[i - 1] {
                if !first_increase_finished {
                    first_increase_finished = true;
                    increasing = false;
                } else {
                    return false;
                }
            }
        } else {
            if nums[i] > nums[i - 1] {
                if !decrease_finished {
                    decrease_finished = true;
                    increasing = true;
                } else {
                    return false;
                }
            }
        }
    }

    first_increase_finished && decrease_finished
}
