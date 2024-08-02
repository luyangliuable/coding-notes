# Rust Ownership and Borrowing Rules

## Ownership Rules

1. **Single Ownership**:  
    Every value in Rust has a single "owner" — a variable that holds it. When the owner goes out of scope, the value will be automatically deallocated.

    ```rust
    let x = 42;  // x is the owner of the value 42
    ```

2. **Move Semantics**:  
    Assigning a value to another variable or passing it to a function will move ownership unless the type implements the `Copy` trait. Once moved, the original variable can no longer be used.

    ```rust
    let s1 = String::from("hello");
    let s2 = s1;  // Ownership is moved from s1 to s2
    // println!("{}", s1);  // This would be an error
    ```

3. **Clone**:  
    If you do want to duplicate the data, you can use the `clone` method (if available for that type).

    ```rust
    let s1 = String::from("hello");
    let s2 = s1.clone();  // Data is duplicated
    ```

## Borrowing Rules

1. **Immutable Borrow**:  
    You can have multiple immutable references (`&T`) to a value as long as there are no mutable references to the same value.

    ```rust
    let s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    ```

2. **Mutable Borrow**:  
    You can have exactly one mutable reference (`&mut T`) to a value in a particular scope.

    ```rust
    let mut s = String::from("hello");
    let r1 = &mut s;
    // let r2 = &mut s;  // This would be an error
    ```

3. **Mutability Exclusivity**:  
    You cannot have both a mutable and an immutable reference to the same value at the same time.

    ```rust
    let mut s = String::from("hello");
    let r1 = &s;
    // let r2 = &mut s;  // This would be an error
    ```

4. **No Dangling References**:
    References must always be valid. You cannot create a reference that outlives the data it points to.

    ```rust
    // This would be an error
    // let r;
    // {
    //     let x = 42;
    //     r = &x;
    // }
    // println!("{}", r);
    ```

## Additional Constraints

1. **Interior Mutability**:  
    Rust has types like `RefCell` that allow you to bypass the standard borrowing rules, but they come with their own constraints (e.g., runtime checks).

2. **Concurrency**:  
    The ownership and borrowing rules also extend to multi-threading. For example, the `Arc` and `Mutex` types enable safe sharing of data between threads by providing atomic reference counting and mutual exclusion, respectively.

3. **Function Signatures**:  
    Function signatures often indicate the ownership and borrowing semantics. For example, passing a value by value (`T`) moves ownership, whereas passing it by immutable (`&T`) or mutable (`&mut T`) reference borrows it.
