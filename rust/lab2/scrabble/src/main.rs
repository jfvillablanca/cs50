use scrabble::get_string;

const POINTS: [u32; 26] = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10,
];

fn main() {
    let word_1 = get_string("Player 1: ");
    let word_2 = get_string("Player 2: ");

    let score_1 = compute_score(&word_1);
    let score_2 = compute_score(&word_2);

    if score_1 > score_2 {
        println!("Player 1 wins!")
    } else if score_1 < score_2 {
        println!("Player 2 wins!")
    } else {
        println!("Tie!")
    }
}

fn compute_score(word: &String) -> u32 {
    word.chars()
        .filter(|c| c.is_ascii_alphabetic())
        .fold(0, |acc, cur| {
            let scrabble_index = cur.to_ascii_uppercase() as u32 - 'A' as u32;
            acc + POINTS[scrabble_index as usize]
        })
}
