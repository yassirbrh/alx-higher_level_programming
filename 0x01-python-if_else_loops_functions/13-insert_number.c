#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list.
 * @number: Number value stored.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new->n = number;
		*head = new;
		(*head)->next = NULL;
	}
	else if ((*head)->n == number || (*head)->n > number)
	{
		new->n = number;
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current != NULL)
		{
			if (current->n == number || current->n > number)
			{
				new->n = number;
				new->next = prev->next;
				prev->next = new;
				return (new);
			}
			if (current->next == NULL)
			{
				new->n = number;
				new->next = NULL;
				current->next = new;
				return (new);
			}
			prev = current;
			current = current->next;
		}
	}
	return (new);
}
