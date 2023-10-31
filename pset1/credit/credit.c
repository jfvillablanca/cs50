#include <cs50.h>
#include <stdio.h>

bool luhn(long cc);
int num_digits(long cc);
long power_of_10(int n);

int main(void)
{
    long cc_number = get_long("Number: ");
    
    int cc_num_digits = num_digits(cc_number);
    if (luhn(cc_number)) 
    {
        if (cc_num_digits == 15) 
        {
            int leading_digits = cc_number / power_of_10(13);
            if (leading_digits == 34 || leading_digits == 37) 
            {
                printf("AMEX\n");
                return 0;
            }
        }
        if (cc_num_digits == 16) 
        {
            int leading_digits = cc_number / power_of_10(14);
            if (leading_digits >= 51 && leading_digits <= 55) 
            {
                printf("MASTERCARD\n");
                return 0;
            }
        }
        if (cc_num_digits == 13 || cc_num_digits == 16) 
        {
            int leading_digits = (cc_num_digits == 13) ? cc_number / power_of_10(12) : cc_number / power_of_10(15);
            if (leading_digits == 4)
            {
                printf("VISA\n");
                return 0;
            }
        }
    }
    printf("INVALID\n");
}

bool luhn(long cc)
{
    int cumsum_one = 0;
    int cumsum_two = 0;

    while (cc > 0) 
    {
        cumsum_two += cc % 10;
        cc /= 10;
        int sum = 2 * (cc % 10);
        if (sum >= 10) 
        {
            cumsum_one += sum % 10;
            sum /= 10;
        }
        cumsum_one += sum;
        cc /= 10;
    }

    return (cumsum_one + cumsum_two) % 10 == 0;
}

int num_digits(long cc)
{
    int digits = 0;
    if (cc < 0) 
    {
        digits = 1;
    }
    while (cc) 
    {
        cc /= 10;
        digits++;
    }
    return digits;
}

long power_of_10(int n) 
{
    long result = 1;
    while (n > 0) 
    {
        result *= 10;
        n--;
    }
    return result;
}
