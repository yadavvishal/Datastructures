#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};

struct node *insertlinkedlistdata(struct node *head,int data)
{
    struct node *newnode=malloc(sizeof(struct node));
    newnode->data=data;
    newnode->next=NULL;
    if(head==NULL)
    {
        head=newnode;
    }
    else
    {

                struct node *trav=head;
                while(trav->next!=NULL)
                {

                        trav=trav->next;
                }
                trav->next=newnode;
    }
    return head;
}
int display(struct node *head)
{
    struct node *trav=head;
    while(trav)
    {
        printf("%d->",trav->data);
        trav=trav->next;
    }printf("NULL");

}
int main()
{
    int i,n,data;

    printf("Enter the number of input:");
    scanf("%d",&n);
    struct node *head=NULL;
    for(i=0;i<n;i++)
    {
        scanf("%d",&data);
        head= insertlinkedlistdata(head,data);
    }
    display(head);

}
