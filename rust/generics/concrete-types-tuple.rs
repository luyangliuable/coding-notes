struct A;

struct S(String, i32, A);

fn main() {
    // Create an instance of 'A'.
    // let a = A;
    let a = "aasdad".to_string();
    let b = A;
    
    // Create an instance of 'S' that contains 'a'.
    let s = S(a, 12, b);

    print_struct(&s);
}

fn print_struct(_s: &S) {
    println!("S contains an instance of A!");
}
