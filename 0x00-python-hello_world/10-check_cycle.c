#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in a singly-linked list
 * @list: the linked list to be checked
 *
 * Return: 1 if there is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *nasra, *mycode;

	if (!list)
		return (0);

	nasra = list->next;
	mycode = list->next->next;

	while (nasra && mycode && mycode->next)
	{
		if (nasra == mycode)
			return (1);

		nasra = nasra->next;
		mycode = mycode->next->next;
	}

	return (0);
}
