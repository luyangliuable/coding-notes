struct Owner(i32);

impl Owner {
    fn add_one<'a>(&'a mut self) { self.0 += 1; }

    fn print<'a>(&'a self) {
        println!("`print`: {}", self.0);
    }
}

fn main() {
    let mut owner = Owner(18);
    owner.add_one();
    owner.print();
}

/* Make it work by adding proper lifetime annotations */
struct ImportantExcerpt<'a> {
    part: &'a str,
}

impl <'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}
