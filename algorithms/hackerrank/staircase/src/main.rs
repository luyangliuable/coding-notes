use std::io::{self, BufRead};

/*
 * Complete the 'staircase' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

fn staircase(n: i32) {
    for i in 1..=n {
        let mut a = String::new();
        
        for _ in 0..(n-i) {
            a.push(' ');
        }

        for _ in 0..i {
            a.push('#');
        }

        println!("{}", a);
    }
}

fn main() {
    staircase(12);
}
