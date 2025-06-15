/* Make it work */
#[derive(Debug)]
struct NoCopyType {}

#[derive(Debug)]
struct Example<'a, 'b> {
    a: &'a u32,
    b: &'b NoCopyType
}

fn main() {
    /* 'a tied to fn-main stackframe */
    let var_a = 35;
    let var_b;
    let example: Example;

    {
        /* Lifetime 'b tied to new stackframe/scope */
        var_b = NoCopyType {};
        example = Example { a: &var_a, b: &var_b };
    }

    println!("(Success!) {:?}", example);
}
