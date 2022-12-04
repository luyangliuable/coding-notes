fn main() {
    let number = 10;
    {
        let number = 22;
        println!("{}", number);
    }
    println!("{}", number);


    fn abc() -> String {
        "abc".to_string()
    }

    let letters = abc();
    let cloned_letters = abc().clone();

    println!("{}", letters);
    println!("{}", cloned_letters);
}
