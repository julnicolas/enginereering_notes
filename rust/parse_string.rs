fn main() {
    // parse returns an Result<u64>, unwrap panics if
    // Result<u64> is None
    //
    // parse needs a compiler hint to parse to the right
    // destination type.
    // Two methods can be used, either using the 'turbo fish'
    // operator (the resolution operator with explicit typing).
    // Or, it is possible to define i as let i: u64 = ...
    let i = "4".trim().parse::<u64>().unwrap();
    println!("{}", i);

    // Another way to do it, panicking if None is the following
    let j: u64 = "5".parse().expect("error - str is not an unsigned int");
    println!("{}", j);

    // The recomended way therefore to deal with parsing is handle the None
    // case. Here is a way to do it
    match "-7".parse::<u64>() {
        Err(err) => {
            println!("error - couldn't parse int - {}", err)
        }
        Ok(i) => {
            println!("{}", i)
        }
    }
}
