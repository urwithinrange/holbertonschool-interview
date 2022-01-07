#include "palindrome.h"

/**
 * is_palindrome - checks if a unsigned long int is a palindrome
 * @n: integer to check
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(unsigned long int n)
{
        unsigned long int tmp = 0, n_copy;

        if (n < 0 || n % 10 == 0)
                return (0);
        n_copy = n;
        while (n_copy > 0)
        {
                tmp = tmp * 10 + n_copy % 10;
                n_copy /= 10;
        }
        if (tmp == n)
                return (1);
        else
                return (0);
}
