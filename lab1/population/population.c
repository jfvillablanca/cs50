#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    int no_of_years = 0;
    int n = start;

    while (n < end)
    {
        int born = n / 3;
        int dead = n / 4;
        n = n + born - dead;
        no_of_years++;
    }
    printf("Years: %i\n", no_of_years);
}
