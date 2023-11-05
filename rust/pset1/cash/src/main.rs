use cash::get_int;

fn main() {
    let mut cents = loop {
        let x = get_int("Change owed: ");
        if x >= 0 {
            break x;
        }
    };

    let quarters = calculate_quarters(cents);
    cents -= quarters * 25;

    let dimes = calculate_dimes(cents);
    cents -= dimes * 10;

    let nickels = calculate_nickels(cents);
    cents -= nickels * 5;

    let pennies = calculate_pennies(cents);

    println!("{}", quarters + dimes + nickels + pennies);
}

fn calculate_quarters(cents: i32) -> i32 {
    cents / 25
}

fn calculate_dimes(cents: i32) -> i32 {
    cents / 10
}

fn calculate_nickels(cents: i32) -> i32 {
    cents / 5
}

fn calculate_pennies(cents: i32) -> i32 {
    cents
}
