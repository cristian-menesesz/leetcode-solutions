pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
    let mut left = 0;
    let mut right = letters.len();

    while left < right {
        let mid = (left + right) / 2;
        if letters[mid] <= target {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    if left < letters.len() {
        letters[left]
    } else {
        letters[0]
    }
}
