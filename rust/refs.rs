fn main() {
    ///////////////////////////////////////////////////////////////////////////
    //                                  Ref                                  //
    ///////////////////////////////////////////////////////////////////////////
    let starship: Option<String> = Some("Omaha".to_string());

    match starship {
        Some(ref name) => println!("{}", name),
        None => {}
    }

    // Without the use of the `ref` keyword above, this next line would not compile:
    println!("{:?}", starship);
}


