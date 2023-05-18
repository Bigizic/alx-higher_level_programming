#include "lists.h"
/* header */

/**
 * insert_node - a function in C that inserts a number into a sorted singly linked list.
 *
 * @head: double pointer to first node of listint_t list
 *
 * @number: number to insert into the list
 *
 * Return: the address of the newNode or NUll if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev_node, *current_node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	prev_node = NULL;
	current_node = *head;
	while (current_node != NULL && current_node->n < number)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}
	if (current_node == NULL)
	{
		prev_node->next = new_node;
	}
	else
	{
		new_node->next = current_node;
	}

	if (prev_node != NULL)
	{
		prev_node->next = new_node;
	}
	else
		*head = new_node;

	return (new_node);
}
