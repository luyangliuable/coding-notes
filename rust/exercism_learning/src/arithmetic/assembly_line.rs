// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub fn production_rate_per_hour(speed: u8) -> f64 {
    // unimplemented!("calculate hourly production rate at speed: {}", speed)
    let mut a = (speed as f64);
    if ( a >= 0.0 && a <= 4.0 ) {
        a = a * (221 as f64);
    } else if (a > 4.0 && a <= 8.0) {
        a = a * (221 as f64)*0.90;
    } else if (a > 8.0 && a <= 10.0) {
        a = a * (221 as f64)*0.77;
    } else {
        panic!("Invalid speed");
    }
    println!("The value of a is: {}", a);
    a
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    // unimplemented!("calculate the amount of working items at speed: {}", speed)
    let cars = production_rate_per_hour(speed as u8) as u32;
    let cars_per_minute = cars / 60;
    println!("cars per minute is: {}", cars_per_minute);
    cars_per_minute
}
