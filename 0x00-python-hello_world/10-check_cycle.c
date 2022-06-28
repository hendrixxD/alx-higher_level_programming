#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks a list for a loop
 *
 * @list: list to be checked
 * Return: 1 if there is loop or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *egg, *stone;

	if (!list || !list->next)
		return (0);

	egg = stone = list;
	egg = egg->next;
	stone = stone->next->next;
	while (egg && stone && stone->next)
	{
		if (egg == stone)
			return (1); /* Loop found */
		egg = egg->next;
		stone = stone->next->next;
	}
	/* No loop/cycle found */
	return (0);
}
