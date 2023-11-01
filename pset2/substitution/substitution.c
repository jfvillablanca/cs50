#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char ALPHABET[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int check_key_failed(string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];

    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }

    if (check_key_failed(key))
    {
        return 1;
    }

    string plaintext = get_string("plaintext:  ");
    string ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        int current_char = plaintext[i];
        if (isalpha(current_char))
        {
            int letter_index = toupper(current_char) - 'A';
            ciphertext[i] = (islower(current_char)) ? tolower(key[letter_index]) : toupper(key[letter_index]);
        }
        else
        {
            ciphertext[i] = current_char;
        }
    }

    printf("ciphertext: %s\n", ciphertext);
    return 0;
}

int check_key_failed(string key)
{
    char local[sizeof(ALPHABET)];
    memcpy(local, ALPHABET, sizeof(ALPHABET));

    for (int i = 0, n = strlen(key); i < n; i++)
    {
        int current_letter = toupper(key[i]);
        int letter_index = current_letter - 'A';
        if (!isalpha(current_letter))
        {
            printf("Key must only contain alphabetic characters\n");
            return 1;
        }
        if (current_letter == local[letter_index])
        {
            local[letter_index] = '\0';
        }
        else
        {
            printf("Key must contain all %i unique letters\n", (int) sizeof(ALPHABET));
            return 1;
        }
    }
    return 0;
}
