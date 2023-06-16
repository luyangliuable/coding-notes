use std::io::{self, BufRead};

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

fn plusMinus(arr: &[i32]) {
    let mut p: f64 = 0.0;
    let mut n: f64 = 0.0;
    let mut z: f64 = 0.0;

    for &item in arr {
        match item {
            item if item < 0 => {
                n += 1.0;
            },
            item if item == 0 => {
                z += 1.0;
            },
            item if item > 0 => {
                p += 1.0;
            },
            _ => {}
        }
    }

    println!("{:.6}", ((p/arr.len() as f64) * 1e6).round() / 1e6);
    println!("{:.6}", ((n/arr.len() as f64) * 1e6).round() / 1e6);
    println!("{:.6}", ((z/arr.len() as f64) * 1e6).round() / 1e6);
}

fn main() {
    let test_array1: [i32; 6] = [-4, 3, -9, 0, 4, 1];

    plusMinus(&test_array1);
}
