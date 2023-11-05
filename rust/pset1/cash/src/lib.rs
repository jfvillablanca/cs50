use std::io::{self, Write};

pub fn get_int(prompt: &str) -> i32 {
    loop {
        print!("{prompt}");
        io::stdout().flush().unwrap();

        let mut input_text = String::new();
        match io::stdin().read_line(&mut input_text) {
            Ok(_) => match input_text.trim().parse() {
                Ok(input_int) => return input_int,
                Err(_) => continue,
            },
            Err(_) => continue,
        }
    }
}
