#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

void merge(pair array[], int left, int middle, int right);
void merge_sort(pair array[], int left, int right);
bool is_noncyclic(int winner, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // (NOT SURE IF NECESSARY) Initialize preferences to zero
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            preferences[i][j] = 0;
        }
    }

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // ASSUMPTIONS: no two candidates will have the same name
    for (int i = 0; i < candidate_count; i++)
    {
        if (strncmp(name, candidates[i], strlen(name)) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // ASSUMPTIONS: every voter will rank each of the candidates (len(ranks) == len(candidates))
    // The logic here is to loop over the ranks[] array
    for (int i = 0; i < candidate_count; i++)
    {
        // Let's say ranks[] looks like this = { 3, 0, 4, 1, 2 }
        // When i == 0, the remaining candidates is { 0, 4, 1, 2 }
        // When i == 1, the remaining candidates is { 4, 1, 2 }
        // And so on, and so forth
        int remaining_candidates = candidate_count - i;
        for (int j = i; j <= remaining_candidates; j++)
        {
            // No voter prefers some candidate over the same candidate
            // i.e No voter prefers Candidate John over Candidate John because that's absurd
            if (ranks[i] == ranks[j])
            {
                continue;
            }
            preferences[ranks[i]][ranks[j]] += 1;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count] = (pair){
                    .winner = i,
                    .loser = j,
                };
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    merge_sort(pairs, 0, pair_count - 1);
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        int winner = pairs[i].winner;
        int loser = pairs[i].loser;

        if (is_noncyclic(winner, loser))
        {
            locked[winner][loser] = true;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    bool won;
    int winner;

    // ASSUMPTION: There is only one source
    for (int i = 0; i < candidate_count; i++)
    {
        won = true;

        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i] == true)
            {
                won = false;
            }
        }

        if (won)
        {
            winner = i;
        }
    }

    printf("%s\n", candidates[winner]);

    return;
}

void merge(pair array[], int left, int middle, int right)
{
    int left_size = middle - left + 1;
    int right_size = right - middle;

    pair Left[left_size], Right[right_size];

    for (int i = 0; i < left_size; i++)
    {
        Left[i] = array[left + i];
    }
    for (int j = 0; j < right_size; j++)
    {
        Right[j] = array[middle + 1 + j];
    }

    int left_index = 0, right_index = 0, merge_index = left;

    while (left_index < left_size && right_index < right_size)
    {
        pair left_pair = Left[left_index];
        pair right_pair = Right[right_index];
        // Sort in descending order based on preferences array
        if (preferences[left_pair.winner][left_pair.loser] >= preferences[right_pair.winner][right_pair.loser])
        {
            array[merge_index] = Left[left_index];
            left_index++;
        }
        else
        {
            array[merge_index] = Right[right_index];
            right_index++;
        }
        merge_index++;
    }

    while (left_index < left_size)
    {
        array[merge_index] = Left[left_index];
        left_index++;
        merge_index++;
    }

    while (right_index < right_size)
    {
        array[merge_index] = Right[right_index];
        right_index++;
        merge_index++;
    }
}

void merge_sort(pair array[], int left, int right)
{
    if (left < right)
    {
        int middle = left + (right - left) / 2;

        merge_sort(array, left, middle);
        merge_sort(array, middle + 1, right);

        merge(array, left, middle, right);
    }
}

bool is_noncyclic(int winner, int loser)
{
    if (winner == loser)
    {
        return false;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[i][winner] == true)
        {
            if (is_noncyclic(i, loser) == false)
            {
                return false;
            }
        }
    }
    return true;
}

