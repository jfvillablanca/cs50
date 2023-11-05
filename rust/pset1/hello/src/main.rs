use hello::get_string;

fn main() {
    let name = get_string("Give me your name: ");
    println!("hello, {name}");
}
