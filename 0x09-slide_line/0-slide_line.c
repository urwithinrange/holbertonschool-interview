#include "slide_line.h"

/**
 * slide_line - function that merges an array if integers
 * @line: is the arrray of ints being used
 * @size: the size of the array
 * @direction: the input recieved to determine which way the merge ocurs
 * Return: 1on success or 0 on failure
 */
int slide_line(int *line, size_t size, int direction)
{
	if (direction == SLIDE_LEFT)
		left(line, size);
	else if (direction == SLIDE_RIGHT)
		right(line, size);
	else
		return (0);
	return (1);
}


/**
 * left - the function to handle left shift line
 * @line: the int array
 * @size: size of array
 */
void left(int *line, size_t size)
{
	size_t i, j;

	j = 0;
	for (i = 1; i < size; i++)
	{
		if (line[i] == 0)
			continue;
		if (line[i] == line[j])
		{
			line[j] += line[i];
			line[i] = 0;
			j++;
		}
		else if (line[j] == 0)
		{
			line[j] = line[i];
			line[i] = 0;
		}
		else
			j++;
	}
}


/**
 * right - the function to handle right shift line
 * @line: the int array
 * @size: size of array
 */
void right(int *line, size_t size)
{
	size_t i = size - 2;
	size_t j = size - 1;

	if (size > 1)
	{	for (; i != 0; i--)
		{
			if (line[i] == 0)
				continue;
			if (line[i] == line[j])
			{
				line[j] += line[i];
				line[i] = 0;
				j--;
			}
			else if (line[j] == 0)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			else
				j--;
		}
		if (line[j] == 0 || line[j] == line[i])
		{
			line[j] += line[i];
			line[i] = 0;
		}
	}
	return;
}
