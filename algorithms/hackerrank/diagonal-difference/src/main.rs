use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

fn diagonalDifference(arr: &[Vec<i32>]) -> i32 {
    let mut res: i32 = 0;

    let mut x: i32 = 0;

    let mut y: i32 = 0;

    
    for i in 0..arr.len() {
        x += arr[i][i];
        y += arr[i][arr.len() - 1 - i];
    }

    println!("{} - {}", x, y);

    (x-y).abs()
}

fn main() {
    let testarr: [Vec<i32>; 3] = [
        vec![11, 2, 4],
        vec![4, 5, 6],
        vec![10, 8, -12],
    ];
    println!("{}", diagonalDifference(&testarr));
}
