#include "sandpiles.h"
/**
 *sandpiles_sum - a function used to stabilize a sandpile
 *@grid1: left grid
 *@grid2: right grid
 *Return: A stable grid1
 */

void sandpiles_sum(grid1[1][3]
{
	int i, j;
	int temp_grid[3][3];

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] += grid2[i][j];
		}
	}
	while (!stabilized(grid1))
	{
		print_grid(grid1);

		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				temp_grid[i][j] = 0;
			}
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
			{
				if (j != 0 && grid1[i][j - 1] > 3)
				{
					temp_grid[i][j]++;
				}
				if (j != 2 && grid1[i][j + 1] > 3)
				{
					temp_grid[i][j]++;
				}
				if (i != 0 && grid1[i - 1][j] > 3)
				{
					temp_grid[i][j]++;
				}
				if (i != 2 && grid1[i + 1][j -3] > 3)
				{
					temp_grid[i][j]++;
				}
			}
		}
	}
}
/**
 *print_grid - a function used to print a grid
 *@grid: grid
 *Return: void
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	printf("=\n");
	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
/**
 *stabilized - a function used to check if a grid is stabilized
 *@grid: grid
 *Return: 1 if stabilized, 0 if not
 */
int stabilized(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid[i][j] > 3)
			{
				return (0);
			}
		}
	}
	return (1);
}
