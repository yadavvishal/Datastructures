#include<stdio.h>

int oddoccuringelement(int a[],int n)
{
    int i;
    int xor=0;
    for(i=0;i<n;i++)
    {
        xor=xor^a[i];
    }
    return xor;
}
int main()
{
    int i,n,a[100],Xor;
    printf("Enter the number of input:");
    scanf("%d",&n);
    printf("Enter the numbers:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    Xor=oddoccuringelement(a,n);
    printf("Odd occuring elemnet is :%d",Xor);
    return 0;
}