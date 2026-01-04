pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
    fn is_prime(n: i32) -> bool {
        if n < 2 { return false; }
        if n == 2 { return true; }
        if n % 2 == 0 { return false; }

        let sqrt_n = (n as f64).sqrt() as i32;
        for i in (3..=sqrt_n).step_by(2) {
            if n % i == 0 {
                return false;
            }
        }
        true
    }

    let primes = [
        2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,
        53,59,61,67,71,73,79,83,89,97,101,103,107,
        109,113,127,131,137,139,149,151,157,163,167,
        173,179,181,191,193,197,199,211,223,227,229,
        233,239,241,251,257,263,269,271,277,281,283,293,
        307,311,313,317
    ];

    let mut total_sum = 0;

    for x in nums {
        if x <= 1 { continue; }
        let sqrt_x = (x as f64).sqrt() as i32;

        for &p in primes.iter() {
            if p > sqrt_x { break; }
            if x % p == 0 {
                let q = x / p;
                if q != p && is_prime(q) {
                    total_sum += 1 + p + q + x;
                    break;
                }
                if q == p * p {
                    total_sum += 1 + p + q + x;
                    break;
                }
            }
        }
    }

    total_sum
}
