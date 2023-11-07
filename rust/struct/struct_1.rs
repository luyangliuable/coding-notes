// Fix the error
struct Person {
    name: String,
    age: u8,
    hobby: Option<String>
}

fn main() {
    let age = 30;
    let p = Person {
        name: String::from("sunface"),
        age,
        hobby: None
    };

    println!("Success!");
} 

