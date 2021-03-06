#include "menger.h"
/**
 *menger - a function used to create a 2d Menger Sponge
 *@level: the level of the 2D sponge
 *Return: void
 */

void menger(int level)
{
	int row, col, size, r, c, a;

	size = pow(3, level);
	for (row = 0; row < size; row++)
	{
		for (col = 0; col < size; col++)
		{
			a = 35; /* # */
			r = row;
			c = col;
			while (r > 0 || c > 0)
			{
				if (r % 3 == 1 && c % 3 == 1)
					a = 32; /* [space] */
				r /= 3;
				c /= 3;
			}
			putchar(a);
		}
		putchar('\n');
	}
}
