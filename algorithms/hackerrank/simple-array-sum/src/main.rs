use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'simpleArraySum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY ar as parameter.
 */

fn simpleArraySum(ar: &[i32]) -> i32 {
    let mut res: i32 = 0;

    for i in ar {
        res += i;
    }

    res
}

fn main() {
    let test_array1: [i32; 5] = [1, 2, 3, 4, 5];

    println!("{}", simpleArraySum(&test_array1));
}
