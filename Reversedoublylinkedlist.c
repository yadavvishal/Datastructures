i#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node *prev;
	struct node *next;
};

void display(struct node *head)
{
	struct node *temp=head;
	while(temp!=NULL)
	{
		printf("%d ->",temp->data);
		temp=temp->next;
	}
	printf("NULL\n");
}
void reversedisplay(struct node *head)
{
	struct node *trav=head;
	while(trav->next!=NULL)
	{
		trav=trav->next;
	}
	printf("Doubly linked list in reverse order:\n");
	while(trav!=NULL)
	{
		printf("%d->",trav->data);
		trav=trav->prev;
	}
	printf("NULL\n");
}	
int main()
{
	int n,i,data;
	printf("Enter the number of input data:");
	scanf("%d",&n);
	struct node *head=NULL;
	printf("the number of doubly linked list are:\n");
	for(i=0;i<n;i++)
	
	{
		struct node *newnode=malloc(sizeof(struct node));
		scanf("%d",&newnode->data);
		newnode->next=head;
		newnode->prev=NULL;
		
		if(head==NULL)
		{
			head=newnode;
		}
		else
		{
			head->prev=newnode;
			newnode->next=head;
			head=newnode;
		}
	}
	display(head);
	reversedisplay(head);
	return 0;
}
