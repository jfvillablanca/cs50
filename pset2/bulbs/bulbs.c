#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
void print_binary_representation(int n);
int power_of_2(int n);

int main(void)
{
    string message = get_string("Message: ");
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        print_binary_representation(message[i]);
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

void print_binary_representation(int n)
{
    for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
    {
        int pow = power_of_2(j);
        if (pow > n)
        {
            print_bulb(0);
        }
        else
        {
            print_bulb(1);
            n -= pow;
        }
    }
}

int power_of_2(int n)
{
    long result = 1;
    while (n > 0)
    {
        result *= 2;
        n--;
    }
    return result;
}
