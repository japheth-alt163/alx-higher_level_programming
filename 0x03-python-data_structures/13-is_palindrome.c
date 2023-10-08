#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int arr[1000]; /* Assuming a maximum of 1000 elements in the list */
int i = 0, j = 0;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Store the elements in an array */
while (current != NULL)
{
arr[i] = current->n;
i++;
current = current->next;
}

/* Compare the elements in the array to check for a palindrome */
i--;
while (i > j)
{
if (arr[i] != arr[j])
return (0);
i--;
j++;
}

return (1);
}
