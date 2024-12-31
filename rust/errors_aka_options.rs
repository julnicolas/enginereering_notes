// This program shows a simple way to handle errors

// This function returns a value, it never fails
fn value() -> Option<u64> {
    Some(2)
}

// This function always returns an invalid value, None.
// It always fails
fn error() -> Option<u64> {
    None
}

fn main() {
    // Check if None or if we received some value
    match value() {
        None => {
            println!("error!")
        }
        Some(v) => {
            println!("int is {}", v)
        }
    }

    match error() {
        None => {
            println!("error!")
        }
        Some(v) => {
            println!("{}", v)
        }
    }
}
