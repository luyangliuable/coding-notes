mod functions;
mod string;
mod datetime;
mod enums;
mod arithmetic;

use enums::semi_structured_logs::{log, info, error, warn, LogLevel};

// functions::lucian_luscious_lasagna;

fn main() {
    arithmetic::assembly_line::production_rate_per_hour(6);
    arithmetic::assembly_line::working_items_per_minute(6);
}
