#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *next = NULL;
int i = 0;
/* the list is empty or has only one node, it is a palindrome */
if (!head || !(*head))
return (1);
/* searching for the middle of the list */
while (fast && fast->next)
{
prev = slow;
slow = slow->next;
fast = fast->next->next;
}
/* the middle node is skipped if the list has an odd number of nodes */
if (fast)
slow = slow->next;
/* reversing the second half of the list*/
while (slow)
{
next = slow->next;
slow->next = prev;
prev = slow;
slow = next;
i++;
}
/* Where the comparison from head to a reversed second half */
while (prev && i > 0)
{
if ((*head)->n == prev->n)
{
*head = (*head)->next;
prev = prev->next;
}
i--;
}
return (i == 0 ? 1 : 0);
}
