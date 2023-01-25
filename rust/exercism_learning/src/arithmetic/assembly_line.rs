// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

/**
 * This function calculates the hourly production rate at a given speed.
 *
 * @param speed The speed at which the production rate should be calculated.
 * @return The hourly production rate.
 */
pub fn production_rate_per_hour(speed: u8) -> f64 {
    // The variable a will hold the production rate
    let mut a = (speed as f64);
    // Check if speed is between 0 and 4
    if ( a >= 0.0 && a <= 4.0 ) {
        // If speed is between 0 and 4, production rate is 221 * speed
        a = a * (221 as f64);
    }
    // Check if speed is between 4 and 8
    else if (a > 4.0 && a <= 8.0) {
        // If speed is between 4 and 8, production rate is 221 * speed * 0.90
        a = a * (221 as f64)*0.90;
    }
    // Check if speed is between 8 and 10
    else if (a > 8.0 && a <= 10.0) {
        // If speed is between 8 and 10, production rate is 221 * speed * 0.77
        a = a * (221 as f64)*0.77;
    }
    // If speed is not between 0 and 10
    else {
        // Panic, as the speed is invalid
        panic!("Invalid speed");
    }
    // Print the production rate
    println!("The value of a is: {}", a);
    // Return the production rate
    a
}

/**
 * This function calculates the amount of working items per minute at a given speed.
 *
 * @param speed The speed at which the working items per minute should be calculated.
 * @return The amount of working items per minute.
 */
pub fn working_items_per_minute(speed: u8) -> u32 {
    // Get the production rate per hour using the production_rate_per_hour function
    let cars = production_rate_per_hour(speed as u8) as u32;
    // Calculate the amount of working items per minute
    let cars_per_minute = cars / 60;
    // Print the amount of working items per minute
    println!("cars per minute is: {}", cars_per_minute);
    // Return the amount of working items per minute
    cars_per_minute
}
