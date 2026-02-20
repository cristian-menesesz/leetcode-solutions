pub fn make_largest_special(s: String) -> String {
    if s.len() <= 2 {
        return s;
    }

    let mut blocks = Vec::new();
    let mut balance = 0;
    let mut start = 0;

    let chars: Vec<char> = s.chars().collect();

    for i in 0..chars.len() {
        if chars[i] == '1' {
            balance += 1;
        } else {
            balance -= 1;
        }

        if balance == 0 {
            let inner: String = chars[start + 1..i].iter().collect();
            let optimized = make_largest_special(inner);
            blocks.push(format!("1{}0", optimized));
            start = i + 1;
        }
    }

    blocks.sort_by(|a, b| b.cmp(a));

    blocks.concat()
}