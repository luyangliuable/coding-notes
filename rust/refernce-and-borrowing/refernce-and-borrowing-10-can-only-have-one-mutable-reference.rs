// Comment one line to make it work
fn main() {
    let mut s = String::from("hello, ");

    let r1 = &mut s;
    r1.push_str("world");
    // let r2 = &mut s;
    // r2 -> r1
    r1.push_str("!");
    
    println!("{}",r1);
}
