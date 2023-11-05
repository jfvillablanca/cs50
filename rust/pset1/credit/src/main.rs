use credit::get_long;

fn main() {
    let cc_number = get_long("Number: ");
    let cc_num_digits = cc_number.to_string().len() as u64;

    if luhn(cc_number) {
        let leading_digits = cc_number / 10_u64.pow((cc_num_digits - 2) as u32);
        if cc_num_digits == 15 {
            if leading_digits == 34 || leading_digits == 37 {
                println!("AMEX");
                return;
            }
        }
        if cc_num_digits == 16 {
            if leading_digits >= 51 && leading_digits <= 55 {
                println!("MASTERCARD");
                return;
            }
        }
        if cc_num_digits == 13 || cc_num_digits == 16 {
            let leading_digits = cc_number / 10_u64.pow((cc_num_digits - 1) as u32);
            if leading_digits == 4 {
                println!("VISA");
                return;
            }
        }
    }
    println!("INVALID");
}

fn luhn(cc_number: u64) -> bool {
    let cc_string = cc_number.to_string();
    let mut cumsum_one = 0;
    let mut cumsum_two = 0;

    for (i, val) in cc_string
        .chars()
        .rev()
        .enumerate()
        .map(|(i, x)| (i, x.to_digit(10).unwrap_or(0)))
    {
        if i % 2 != 0 {
            let mut sum = 2 * val;
            if sum >= 10 {
                cumsum_one += sum % 10;
                sum /= 10;
            }
            cumsum_one += sum;
        } else {
            cumsum_two += val;
        }
    }
    (cumsum_one + cumsum_two) % 10 == 0
}
