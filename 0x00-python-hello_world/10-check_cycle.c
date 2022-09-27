#include "lists.h"
/**
 * check_cycle - checks if a singly linked list is a cycle
 * @list - pointer to the head of the list
 * Return: 0 if there's no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
listint_t *current;
current = list;

while (list != NULL)
{
if (list->next == current)
	return(1);
list = list->next;
}
return(0);
}
