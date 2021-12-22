#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */

int is_palindrome(listint_t **head)
{
	/* the list is empty or has only one node, it is a palindrome */
	if (!head || !(*head))
		return (1);
	return (palindrome_recur(head, *head));
}
/**
 * palindrome_recur - recursivly checks for a palindrome list
 * @head: pointer to the head of the list
 * @cur_node: the position in the list that is being compared to head pos
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int palindrome_recur(listint_t **head, listint_t *cur_node)
{
	if (!cur_node)
	return (1);
	/*Using recursion to avoid creating a second list to be freed*/
	if (palindrome_recur(head, cur_node->next) && (*head)->n == cur_node->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
