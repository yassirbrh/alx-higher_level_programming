#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Function
 *
 * Description: Checks if a singly linked list has a cycle in it.
 *
 * @list: Pointer to the singly linked list.
 *
 * Return: 0 if there is no cycle,
 *         1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *firstNode = list, *secNode = list;

	while (secNode != NULL && secNode->next != NULL)
	{
		firstNode = firstNode->next;
		secNode = (secNode->next)->next;
		if (firstNode == secNode)
			return (1);
	}
	return (0);
}
