# Make a CLI tool in rust

From my research I found out this can be a good approach:
    - `clap` for cli logic, coloring, help generation
    - `indicatif` to show spinners, progress bars
    - optional `owo-colors` to print colors, though clap maybe able to do it

Source: https://rust-cli.github.io/book/index.html

To run a command, the code will be more or less like this:

``` rs
use std::process::Command;

fn main() {
    // probably new("pwd") is enough
    let out = Command::new("sh")
        .arg("-c")
        .arg("pwd")
        .output()
        .expect("error!");
    println!(out);
}
```

