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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
