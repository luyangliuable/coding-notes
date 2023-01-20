// This stub file contains items that aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

/// various log levels
#[derive(Clone, PartialEq, Eq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
}

/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    // unimplemented!("return a message for the given log level")
    match level {
        LogLevel::Info => {
            let mut result: String = "[INFO]: ".to_string();
            result.push_str(message);
            result
        },
        LogLevel::Warning => {
            let mut result: String = "[WARNING]: ".to_string();
            result.push_str(message);
            result
        },
        LogLevel::Error => {
            let mut result: String = "[ERROR]: ".to_string();
            result.push_str(message);
            result
        }
    }
}
pub fn info(message: &str) -> String {
    // unimplemented!("return a message for info log level")

    log(LogLevel::Info, message)
}
pub fn warn(message: &str) -> String {
    // unimplemented!("return a message for warn log level")

    log(LogLevel::Warning, message)
}
pub fn error(message: &str) -> String {
    // unimplemented!("return a message for error log level")

    log(LogLevel::Error, message)
}
