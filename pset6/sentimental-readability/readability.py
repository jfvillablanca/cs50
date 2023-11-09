from cs50 import get_string


def main():
    text = get_string("Text: ")
    grade = coleman_liau(count_letters(text), count_words(text), count_sentences(text))

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count


def count_words(text):
    # Assumptions that a sentence:
    # - will contain at least one word;
    # - will not start or end with a space; and
    # - will not have multiple spaces in a row.

    count = 1
    for char in text:
        if char == " ":
            count += 1
    return count


def count_sentences(text):
    # Assumptions that a sentence:
    # - is any sequence of characters that ends with a . or a ! or a ?;
    # Sentence boundary detection here is rudimentary

    count = 0
    for char in text:
        if char in [".", "?", "!"]:
            count += 1
    return count


def coleman_liau(letter_count, word_count, sentence_count):
    L = letter_count / word_count * 100
    S = sentence_count / word_count * 100
    return round(0.0588 * L - 0.296 * S - 15.8)


if __name__ == "__main__":
    main()

