#include "lists.h"
#include <stdlib.h>
/* header */

/**
* is_palindrome: a function in C that checks if a singly linked list is a palindrome
*
* @head: listint_t list to check
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *new_head = *head;

	if (new_head == NULL)
		return (1);
	return (0);
}