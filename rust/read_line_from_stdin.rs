// Read a line from stdin

fn main() {
    println!("Write something:");

    let mut line = String::new();
    std::io::stdin()
        .read_line(&mut line)
        // This cause the program to abort with a stack trace
        .expect("cannot read line");

    println!("echo - {line}");
}
