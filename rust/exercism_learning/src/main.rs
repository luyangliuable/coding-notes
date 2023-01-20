mod functions;
mod string;
mod datetime;
mod enums;

use enums::semi_structured_logs::{log, info, error, warn, LogLevel};

// functions::lucian_luscious_lasagna;

fn main() {
    // println!("Hello, world!");
    // println!("{}", functions::lucian_luscious_lasagna::expected_minutes_in_oven())
    // println!("{}", string::reverse_string::reverse("Hello"))
    // let DateTime a =

    println!("{}", log(enums::semi_structured_logs::LogLevel::Error, "Stack overflow"));
    // Returns: "[ERROR]: Stack overflow"}

    println!("{}", info( "Timezone changed" ))
    // Returns: "[INFO]: Timezone changed"
}
