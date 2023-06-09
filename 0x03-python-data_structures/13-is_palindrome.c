#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * add_nodeint_start - Function
 *
 * Description: add the new node to the head of the list.
 *
 * @head: Pointer to the pointer to the head of list.
 * @n: The number to add to the list.
 *
 * Return: the new created node.
 */
listint_t *add_nodeint_start(listint_t **head, int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
 * is_palindrome - Function
 *
 * Description: Checks if a singly linked list is a palindrome.
 *
 * @head: Pointer to the pointer to the head of list.
 *
 * Return: 0 if it is not a palindrome.
 *         1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_head = NULL;
	listint_t *current = *head, *new_current;

	if (*head == NULL)
		return (1);
	while (current != NULL)
	{
		add_nodeint_start(&new_head, current->n);
		current = current->next;
	}
	current = *head;
	new_current = new_head;
	while (current != NULL)
	{
		if (current->n != new_current->n)
		{
			free_listint(new_head);
			return (0);
		}
		current = current->next;
		new_current = new_current->next;
	}
	free_listint(new_head);
	return (1);
}
