#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int ALPHABET_LEN = 26;

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);

    string plaintext = get_string("plaintext:  ");
    string ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        int current_char = plaintext[i];
        if (isalpha(current_char))
        {
            if (islower(current_char))
            {
                int normalized = (current_char - 'a' + key) % ALPHABET_LEN;
                ciphertext[i] = 'a' + normalized;
            }
            if (isupper(current_char))
            {
                int normalized = (current_char - 'A' + key) % ALPHABET_LEN;
                ciphertext[i] = 'A' + normalized;
            }
        }
        else
        {
            ciphertext[i] = current_char;
        }
    }

    printf("ciphertext: %s\n", ciphertext);
    return 0;
}
