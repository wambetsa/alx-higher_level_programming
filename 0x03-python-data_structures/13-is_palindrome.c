#include <stdlib.h>
#include <stdio.h>
#include "list.h"
/**
 * pal - checks palindrome
 * @arr: pointer
 * @index_a: primero indice
 * @index_b: seg indice
 * Return: return 1 if list is palindrome
 */
int pal(int *arr, int index_a, int index_b)
{
	if (index_a > index_b)
		return (1);
	if (arr[index_a] != arr[index_b])
	{
		return (0);
	}
	return (pal(arr, index_a + 1, index_b - 1));
}
/**
 * is_palindrome - check if s-linked list is palindrome
 * @head: pointer node
 * Return: return 1 if list is palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i = 0; /*, j = 0, node_a = 0, node_b = 0, index_a = 0, index_b = 0;*/
	const listint_t *temp = *head;
	int *arr;

	if (!*head)
		return (1);
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	for (i = 0; i <= (len - 1); i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}
	if (pal(arr, 0, len - 1) == 1)
	{
		free(arr);
		return (1);
	}
	free(arr);
	return (0);
}
