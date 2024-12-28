// Generate random numbers

/*
Install the rand crate in a rust project:
``` sh
cargo add rand
```
*/

// only useful with rustc
use rand::Rng;

fn random(lower: u64, upper: u64) -> u64 {
    // use '=' to include the upper bound in the range
    rand::thread_rng().gen_range(lower..=upper) as u64
}

fn main() {
    let r = random(0, 100);
    println!("random number is {r}");
}
