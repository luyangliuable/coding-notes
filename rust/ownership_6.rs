fn main() {
    let x = Box::new(5);
    
    let mut y = Box::new(i32::MAX);
    
    *y = 4;
    
    assert_eq!(*x, 5);

    println!("Success!");
}
