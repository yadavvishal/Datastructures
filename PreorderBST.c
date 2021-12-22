#include <stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *left, *right;
};
struct node *createnode(int data)
{
    struct node *newnode=malloc(sizeof(struct node));
    newnode->data=data;
    newnode->left=NULL;
    newnode->right=NULL;
    return newnode;

}
void Preorder(struct node *root)
{
    if(root!=NULL)
    {
        printf("%d",root->data);
        Preorder(root->left);
        Preorder(root->right);
    }

}
int main()
{
    struct node *p=createnode(4);
    struct node *p1=createnode(5);
    struct node *p2=createnode(7);
    struct node *p3=createnode(8);
    struct node *p4=createnode(9);
    p->left=p1;
    p->right=p2;
    p1->left=p3;
    p1->right=p4;
    Preorder(p);
    return 0;

}

