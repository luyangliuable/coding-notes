pub fn brackets_are_balanced(string: &str) -> bool {
    // loop through every char in string

    let mut stack = Vec::new();

    for ch in string.chars() {
        match ch {
            '(' | '[' | '{' => stack.push(ch),

            ')' => {
                if stack.pop() != Some('(') {
                    return false;
                }
            }

            ']' => {
                if stack.pop() != Some('[') {
                    return false;
                }
            }

            '}' => {
                if stack.pop() != Some('{') {
                    return false;
                }
            }

            _ => (),
        }
    }

    stack.is_empty()
}
