#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;
listint_t *insert_node(listint_t **head, int number);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif
