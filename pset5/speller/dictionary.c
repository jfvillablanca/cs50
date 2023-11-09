// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Dictionary file
FILE *dictionary_file = NULL;
int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// FUNCTION PROTOTYPES
void free_linked_list(node *head);

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hash_index = hash(word);

    node *current_node = table[hash_index];
    while (current_node != NULL)
    {
        if (strcasecmp(word, current_node->word) == 0)
        {
            return true;
        }
        current_node = current_node->next;
    }

    return false;
}

// Hashes word to a number
// The function used here is a *polynomial rolling hash function*
// Reference: https://cp-algorithms.com/string/string-hashing.html
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    dictionary_file = fopen(dictionary, "r");

    char word_buffer[LENGTH + 1];
    if (dictionary_file != NULL)
    {
        while (fscanf(dictionary_file, "%s", word_buffer) == 1)
        {
            node *new_node = calloc(1, sizeof(node));
            word_count++;

            // Set the next of a new_node to NULL by default
            // new_node->next = NULL;

            if (new_node != NULL)
            {
                strcpy(new_node->word, word_buffer);
                int hash_index = hash(new_node->word);

                // First instance to the specific index
                if (table[hash_index] == NULL)
                {
                    table[hash_index] = new_node;
                    // printf("first head: %s\n", new_node->word);
                }
                else
                {
                    // Point new_node to the current head at index
                    new_node->next = table[hash_index];
                    // Then point the head to the new node
                    table[hash_index] = new_node;
                    // printf("new head: %s | old head: %s\n", table[hash_index]->word, table[hash_index]->next->word);
                }
            }
        }
        return true;
    }

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            free_linked_list(table[i]);
        }
    }

    if (fclose(dictionary_file) == 0)
    {
        return true;
    }
    return false;
}

void free_linked_list(node *head)
{
    node *tmp;
    while (head != NULL)
    {
        tmp = head;
        head = head->next;
        free(tmp);
    }
}
