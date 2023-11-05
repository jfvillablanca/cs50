use std::io::{self, Write};

pub fn get_string(prompt: &str) -> String {
    loop {
        print!("{prompt}");
        io::stdout().flush().unwrap();

        let mut input_text = String::new();
        match io::stdin().read_line(&mut input_text) {
            Ok(_) => return input_text.trim().to_string(),
            Err(_) => continue,
        }
    }
}
