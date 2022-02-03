#ifndef SLIDE_LINE
#define SLIDE_LINE
#include <stdio.h>
#include <stdlib.h>
#define SLIDE_RIGHT 'R'
#define SLIDE_LEFT 'L'
int slide_line (int *line, size_t size, int direction);
void left(int *line, size_t size);
void right(int *line, size_t size);
#endif
