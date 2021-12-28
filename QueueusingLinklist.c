#include<stdio.h>
#include<stdlib.h>
struct node *front=NULL;
struct node *rear=NULL;
struct node{
    int data;
    struct node *next;
};
struct node *enqueue(int data)
{
    struct node *newnode=malloc(sizeof(struct node));
   
    if(newnode==NULL)
    {
        printf("Queue is full\n");
    }
    else{
         newnode->data=data;
    newnode->next=NULL;
    if(front==NULL)
    {
        front=rear=newnode;

    }
    else{
        rear->next=newnode;
        rear=newnode;
    }
       
    }
    
}
int dequeue()
{
    int val=-1;
    struct node *temp=front;
    if(front==NULL)
    {
        printf("Queue is empty\n");
    }
    else{
        front=front->next;
        val=temp->data;
        free(temp);
    }
    return val;
}
int display()
{
    struct node *trav=front;
    while(trav!=NULL)
    {
        printf("%d\n",trav->data);
        trav=trav->next;
    }

}
int main()
{
   int data;
   printf("Dequeuing element:%d\n",dequeue());
   
    enqueue(4);
    enqueue(2);
    enqueue(3);
    enqueue(5);
    display(front);
    printf("Dequeuing element:%d\n",dequeue());
    
    return 0;
}
