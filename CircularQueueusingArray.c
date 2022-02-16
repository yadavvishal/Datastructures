
#include<stdio.h>

#define SIZE 5
int items[SIZE];


int rear=-1,front=-1;

int isFull()
{
	if((rear==SIZE-1 && front==0) || (front==rear+1))
	return 1;
	return 0;
}
int isEmpty()
{
	if(front==-1)
	return 1;
	return 0;
}
void enQueue(int value)
{
	if(isFull())
	{
		printf("Queue is full:\n");
	}
	else
	{
		if(front==-1)
		front=0;
		rear=(rear+1)%SIZE;
		items[rear]=value;
		printf("Inserted-> %d\n",value);
	}
}
int deQueue()
{
	int value;
	if(isEmpty())
	{
		printf("Queue is empty:\n");
		return (-1);
	}
	else
	{
		value=items[front];
		if(front==rear)
		{
			front=-1;
			rear=-1;
		}	
		else
		{
			front=(front+1)%SIZE;
		}
		printf("\n Deleted element ->%d",value);
	return (value);
	}
}
void display()
{
	int i;
	if(isEmpty())
	{
		printf("Queue is empty:\n");
	}
	else
	{
		 printf("\n Front -> %d ", front);
    printf("\n Items -> ");
		for(i=front;i!=rear;i=(i+1)%SIZE)
		{
			printf("%d\n",items[i]);
		}
		 printf("%d ", items[i]);
    printf("\n Rear -> %d \n", rear);
	}
}
int main()
{
	deQueue();
	enQueue(1);
	enQueue(2);
	enQueue(3);
	enQueue(4);
	enQueue(5);
	enQueue(6);
	display();
	deQueue();
	enQueue(7);
	display();
	
	
	return 0;
	
}
