use std::io::{self, Write};

pub fn get_long(prompt: &str) -> u64 {
    loop {
        print!("{prompt}");
        io::stdout().flush().unwrap();

        let mut input_text = String::new();
        match io::stdin().read_line(&mut input_text) {
            Ok(_) => match input_text.trim().parse() {
                Ok(long_input) => return long_input,
                Err(_) => continue,
            },
            Err(_) => continue,
        }
    }
}
