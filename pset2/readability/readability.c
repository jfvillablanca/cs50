#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int coleman_liau(int letter_count, int word_count, int sentence_count);

int main(void)
{
    string text = get_string("Text: ");
    int index = coleman_liau(count_letters(text), count_words(text), count_sentences(text));

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int sum = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            sum++;
        }
    }
    return sum;
}

int count_words(string text)
{
    // Assumptions that a sentence:
    // - will contain at least one word;
    // - will not start or end with a space; and
    // - will not have multiple spaces in a row.

    int sum = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            sum++;
        }
    }
    return sum;
}

int count_sentences(string text)
{
    // Assumptions that a sentence:
    // - is any sequence of characters that ends with a . or a ! or a ?;
    // Sentence boundary detection here is rudimentary

    int sum = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sum++;
        }
    }
    return sum;
}

int coleman_liau(int letter_count, int word_count, int sentence_count)
{
    float L = letter_count / (float) word_count * 100.0;
    float S = sentence_count / (float) word_count * 100.0;
    return (int) round(0.0588 * L - 0.296 * S - 15.8);
}
