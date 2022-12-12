#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
	int data;
	struct Node *next;
	struct Node *prev;
}Node;

typedef struct DoublyLinkedList
{
	Node *head;
	Node *tail;
	int memory_effiecient;
}DoublyLinkedList;

void insert_at_end(Node *head, Node *tail, int data)
{
	Node newNode = {data, NULL, NULL}
	if tail
	{
		tail->next
	}
	else
	{
		head = &newNode;
		tail = &newNode;
	}
}

void print_it(Node *head)
{
	// 
}

void make_memory_efficient(Node *head){
	// 
}

int main(int argc, char const *argv[])
{
	DoublyLinkedList dll, *d;
	d = &dll;
	d->head = NULL;
	d->tail = NULL;

	for (int i = 1; i <= 10; ++i)
	{
		insert_at_end(d->tail, i)
	}
	return 0;
}