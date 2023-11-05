use population::get_int;

fn main() {
    let start_size = loop {
        let size = get_int("Start size: ");
        if size >= 9 {
            break size;
        }
    };

    let end_size = loop {
        let end = get_int("End size: ");
        if end > start_size {
            break end;
        }
    };

    let mut no_of_years = 0;
    let mut current_population = start_size;

    while current_population < end_size {
        let born = current_population / 3;
        let dead = current_population / 4;
        current_population += born - dead;
        no_of_years += 1;
    }
    println!("Years: {no_of_years}");
}
