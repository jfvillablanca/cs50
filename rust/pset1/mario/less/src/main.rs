use less::get_int;
use std::iter::repeat;

fn main() {
    let height = loop {
        let x = get_int("Height: ");
        if x >= 1 && x <= 8 {
            break x;
        }
    };

    for i in 1..height + 1 {
        let spaces = repeat(' ').take((height - i) as usize).collect::<String>();
        let bricks = repeat('#').take(i as usize).collect::<String>();
        println!("{spaces}{bricks}");
    }
}
