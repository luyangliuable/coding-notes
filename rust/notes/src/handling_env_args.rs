use std::env::{ args, Args };

fn main() {
    let mut args: Args = args();

    // let first = args.nth(0).unwrap();
    // println!("The first argument is {:?}", first);


    // let third = args.nth(2);
    // println!("The third argument is {:?}", third);


    let first = args.nth(1).unwrap();
    let operator = args.nth(0).unwrap().chars().next().unwrap();
    let second = args.nth(0).unwrap();

    // To different ways to convert to number
    let first_number = first.parse::<f32>().unwrap();
    let second_number: f32 = second.parse().unwrap();

    println!("{} {} {}", first_number, operator, second_number);

    let result = operate(operator, first_number, second_number);

    println!("Result is {}.", output(first_number, operator, second_number, result));
}

fn operate(operator: char, first_number: f32, second_number: f32) -> f32 {
    // if operator == '+' {
    //     return first_number+second_number;
    // } else if operator == '-' {
    //     return first_number-second_number;
    // } else if operator == '*' {
    //     return first_number*second_number;
    // } else if operator == '/' {
    //     return first_number/second_number;
    // } else {
    //     0.0
    // }

    match operator{
        '+' => first_number + second_number,
        '-' => first_number - second_number,
        '/' => first_number - second_number,
        '*' => first_number - second_number,
        _ => panic!("Invalid operator used.") // base case
    }
}


fn output(first_number: f32, operator: char, second_number: f32, result: f32) -> String {
    format!("{} {} {} = {}", first_number, operator, second_number, result)
}
