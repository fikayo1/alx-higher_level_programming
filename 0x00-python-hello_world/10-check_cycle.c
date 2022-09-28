#include "lists.h"
/**
 * check_cycle - checks if a singly linked list is a cycle
 * @list - pointer to the head of the list
 * Return: 0 if there's no cycle and 1 if there is
 */
int check_cycle(listint_t *list)
{
listint_t *fast, *slow;
fast = list;
slow = list;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
slow = slow->next;
if (fast == slow)
	return(1);
}
return(0);
}
