use std::cmp::{min, max};

pub fn max_product(nums: Vec<i32>) -> i32 {
    // 1ms beats 67.07% of users with Rust
    // Memory beats 73.17% of users with Rust

    let mut prev_min = nums[0];
    let mut prev_max = nums[0];
    let mut ans = nums[0];

    for i in 1..nums.len() {
        let n = nums[i];

        let tmp = prev_min;

        prev_min = min(prev_min*n, min(n, prev_max*n));
        prev_max = max(prev_max*n, max( n, tmp*n ));

        ans = max(prev_max, ans);
    }

    ans
}

fn main() {
    println!("{:?}", max_product(vec![2,3,-2,4]))
}
