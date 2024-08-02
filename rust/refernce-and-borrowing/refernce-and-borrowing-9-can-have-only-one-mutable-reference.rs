// Comment one line to make it work
fn main() {
    // You can have exactly one mutable reference (`&mut T`) to a value in a particular scope.

    let mut s = String::from("hello, ");

    let r1 = &mut s;
    r1.push_str("world");

    // let r2 = &mut s;
    r1.push_str("!");
    
    println!("{}",r1);
}
