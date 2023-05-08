#include "lists.h"
/* header */

/**
 * check_cycle - checks if a single linked list has a cycle in it
 *
 * @: list: list to check
 *
 * Return: 0 if there's no list else return 1
 */

int check_cycle(listint_t *list)
{
	listint_t *input = list;
	listint_t *word = list;

	if (list == NULL)
		return (0);

	while (input && input->next)
	{
		word = word->next;
		input = input->next->next;

		if (word == input)
		{
			return (1);
		}
	}
	return (0);
}
